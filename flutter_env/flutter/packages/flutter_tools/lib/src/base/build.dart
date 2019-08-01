// Copyright 2017 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'dart:async';

import 'package:meta/meta.dart';

import '../artifacts.dart';
import '../build_info.dart';
import '../bundle.dart';
import '../cache.dart';
import '../compile.dart';
import '../dart/package_map.dart';
import '../globals.dart';
import '../macos/xcode.dart';
import '../project.dart';
import '../usage.dart';
import 'context.dart';
import 'file_system.dart';
import 'fingerprint.dart';
import 'process.dart';

GenSnapshot get genSnapshot => context.get<GenSnapshot>();

/// A snapshot build configuration.
class SnapshotType {
  SnapshotType(this.platform, this.mode)
    : assert(mode != null);

  final TargetPlatform platform;
  final BuildMode mode;

  @override
  String toString() => '$platform $mode';
}

/// Interface to the gen_snapshot command-line tool.
class GenSnapshot {
  const GenSnapshot();

  static String getSnapshotterPath(SnapshotType snapshotType) {
    return artifacts.getArtifactPath(
        Artifact.genSnapshot, platform: snapshotType.platform, mode: snapshotType.mode);
  }

  Future<int> run({
    @required SnapshotType snapshotType,
    IOSArch iosArch,
    Iterable<String> additionalArgs = const <String>[],
  }) {
    final List<String> args = <String>[
      '--causal_async_stacks',
    ]..addAll(additionalArgs);

    final String snapshotterPath = getSnapshotterPath(snapshotType);

    // iOS gen_snapshot is a multi-arch binary. Running as an i386 binary will
    // generate armv7 code. Running as an x86_64 binary will generate arm64
    // code. /usr/bin/arch can be used to run binaries with the specified
    // architecture.
    if (snapshotType.platform == TargetPlatform.ios) {
      final String hostArch = iosArch == IOSArch.armv7 ? '-i386' : '-x86_64';
      return runCommandAndStreamOutput(<String>['/usr/bin/arch', hostArch, snapshotterPath]..addAll(args));
    }

    StringConverter outputFilter;
    if (additionalArgs.contains('--strip')) {
      // Filter out gen_snapshot's warning message about stripping debug symbols
      // from ELF library snapshots.
      const String kStripWarning = 'Warning: Generating ELF library without DWARF debugging information.';
      outputFilter = (String line) => line != kStripWarning ? line : null;
    }

    return runCommandAndStreamOutput(<String>[snapshotterPath]..addAll(args),
                                     mapFunction: outputFilter);
  }
}

class AOTSnapshotter {
  AOTSnapshotter({this.reportTimings = false});

  /// If true then AOTSnapshotter would report timings for individual building
  /// steps (Dart front-end parsing and snapshot generation) in a stable
  /// machine readable form. See [AOTSnapshotter._timedStep].
  final bool reportTimings;

  /// Builds an architecture-specific ahead-of-time compiled snapshot of the specified script.
  Future<int> build({
    @required TargetPlatform platform,
    @required BuildMode buildMode,
    @required String mainPath,
    @required String packagesPath,
    @required String outputPath,
    @required bool buildSharedLibrary,
    IOSArch iosArch,
    List<String> extraGenSnapshotOptions = const <String>[],
  }) async {
    FlutterProject flutterProject;
    if (fs.file('pubspec.yaml').existsSync()) {
      flutterProject = FlutterProject.current();
    }
    if (!_isValidAotPlatform(platform, buildMode)) {
      printError('${getNameForTargetPlatform(platform)} does not support AOT compilation.');
      return 1;
    }
    // TODO(cbracken): replace IOSArch with TargetPlatform.ios_{armv7,arm64}.
    assert(platform != TargetPlatform.ios || iosArch != null);

    // buildSharedLibrary is ignored for iOS builds.
    if (platform == TargetPlatform.ios)
      buildSharedLibrary = false;

    final PackageMap packageMap = PackageMap(packagesPath);
    final String packageMapError = packageMap.checkValid();
    if (packageMapError != null) {
      printError(packageMapError);
      return 1;
    }

    final Directory outputDir = fs.directory(outputPath);
    outputDir.createSync(recursive: true);

    final String skyEnginePkg = _getPackagePath(packageMap, 'sky_engine');
    final String uiPath = fs.path.join(skyEnginePkg, 'lib', 'ui', 'ui.dart');
    final String vmServicePath = fs.path.join(skyEnginePkg, 'sdk_ext', 'vmservice_io.dart');

    final List<String> inputPaths = <String>[uiPath, vmServicePath, mainPath];
    final Set<String> outputPaths = <String>{};

    final String depfilePath = fs.path.join(outputDir.path, 'snapshot.d');
    final List<String> genSnapshotArgs = <String>[
      '--deterministic',
    ];
    if (extraGenSnapshotOptions != null && extraGenSnapshotOptions.isNotEmpty) {
      printTrace('Extra gen_snapshot options: $extraGenSnapshotOptions');
      genSnapshotArgs.addAll(extraGenSnapshotOptions);
    }

    final String assembly = fs.path.join(outputDir.path, 'snapshot_assembly.S');
    if (platform == TargetPlatform.ios) {
      // Assembly AOT snapshot.
      outputPaths.add(assembly);
      genSnapshotArgs.add('--snapshot_kind=app-aot-assembly');
      genSnapshotArgs.add('--assembly=$assembly');
    } else if (buildSharedLibrary) {
      final String aotSharedLibrary = fs.path.join(outputDir.path, 'app.so');
      outputPaths.add(aotSharedLibrary);
      genSnapshotArgs.add('--snapshot_kind=app-aot-elf');
      genSnapshotArgs.add('--elf=$aotSharedLibrary');
      genSnapshotArgs.add('--strip');
    } else {
      // Blob AOT snapshot.
      final String vmSnapshotData = fs.path.join(outputDir.path, 'vm_snapshot_data');
      final String isolateSnapshotData = fs.path.join(outputDir.path, 'isolate_snapshot_data');
      final String vmSnapshotInstructions = fs.path.join(outputDir.path, 'vm_snapshot_instr');
      final String isolateSnapshotInstructions = fs.path.join(outputDir.path, 'isolate_snapshot_instr');
      outputPaths.addAll(<String>[vmSnapshotData, isolateSnapshotData, vmSnapshotInstructions, isolateSnapshotInstructions]);
      genSnapshotArgs.addAll(<String>[
        '--snapshot_kind=app-aot-blobs',
        '--vm_snapshot_data=$vmSnapshotData',
        '--isolate_snapshot_data=$isolateSnapshotData',
        '--vm_snapshot_instructions=$vmSnapshotInstructions',
        '--isolate_snapshot_instructions=$isolateSnapshotInstructions',
      ]);
    }

    if (platform == TargetPlatform.android_arm || iosArch == IOSArch.armv7) {
      // Use softfp for Android armv7 devices.
      // This is the default for armv7 iOS builds, but harmless to set.
      // TODO(cbracken): eliminate this when we fix https://github.com/flutter/flutter/issues/17489
      genSnapshotArgs.add('--no-sim-use-hardfp');

      // Not supported by the Pixel in 32-bit mode.
      genSnapshotArgs.add('--no-use-integer-division');
    }

    genSnapshotArgs.add(mainPath);

    // Verify that all required inputs exist.
    final Iterable<String> missingInputs = inputPaths.where((String p) => !fs.isFileSync(p));
    if (missingInputs.isNotEmpty) {
      printError('Missing input files: $missingInputs from $inputPaths');
      return 1;
    }

    // If inputs and outputs have not changed since last run, skip the build.
    final Fingerprinter fingerprinter = Fingerprinter(
      fingerprintPath: '$depfilePath.fingerprint',
      paths: <String>[mainPath]..addAll(inputPaths)..addAll(outputPaths),
      properties: <String, String>{
        'buildMode': buildMode.toString(),
        'targetPlatform': platform.toString(),
        'entryPoint': mainPath,
        'sharedLib': buildSharedLibrary.toString(),
        'extraGenSnapshotOptions': extraGenSnapshotOptions.join(' '),
        'engineHash': Cache.instance.engineRevision,
        'buildersUsed': '${flutterProject != null ? flutterProject.hasBuilders : false}',
      },
      depfilePaths: <String>[],
    );
    // TODO(jonahwilliams): re-enable once this can be proved correct.
    // if (await fingerprinter.doesFingerprintMatch()) {
    //   printTrace('Skipping AOT snapshot build. Fingerprint match.');
    //   return 0;
    // }

    final SnapshotType snapshotType = SnapshotType(platform, buildMode);
    final int genSnapshotExitCode =
      await _timedStep('snapshot(CompileTime)', 'aot-snapshot',
        () => genSnapshot.run(
      snapshotType: snapshotType,
      additionalArgs: genSnapshotArgs,
      iosArch: iosArch,
    ));
    if (genSnapshotExitCode != 0) {
      printError('Dart snapshot generator failed with exit code $genSnapshotExitCode');
      return genSnapshotExitCode;
    }

    // Write path to gen_snapshot, since snapshots have to be re-generated when we roll
    // the Dart SDK.
    final String genSnapshotPath = GenSnapshot.getSnapshotterPath(snapshotType);
    await outputDir.childFile('gen_snapshot.d').writeAsString('gen_snapshot.d: $genSnapshotPath\n');

    // On iOS, we use Xcode to compile the snapshot into a dynamic library that the
    // end-developer can link into their app.
    if (platform == TargetPlatform.ios) {
      final RunResult result = await _buildIosFramework(iosArch: iosArch, assemblyPath: assembly, outputPath: outputDir.path);
      if (result.exitCode != 0)
        return result.exitCode;
    }

    // Compute and record build fingerprint.
    await fingerprinter.writeFingerprint();
    return 0;
  }

  /// Builds an iOS framework at [outputPath]/App.framework from the assembly
  /// source at [assemblyPath].
  Future<RunResult> _buildIosFramework({
    @required IOSArch iosArch,
    @required String assemblyPath,
    @required String outputPath,
  }) async {
    final String targetArch = iosArch == IOSArch.armv7 ? 'armv7' : 'arm64';
    printStatus('Building App.framework for $targetArch...');
    final List<String> commonBuildOptions = <String>['-arch', targetArch, '-miphoneos-version-min=8.0'];

    final String assemblyO = fs.path.join(outputPath, 'snapshot_assembly.o');
    final RunResult compileResult = await xcode.cc(commonBuildOptions.toList()..addAll(<String>['-c', assemblyPath, '-o', assemblyO]));
    if (compileResult.exitCode != 0) {
      printError('Failed to compile AOT snapshot. Compiler terminated with exit code ${compileResult.exitCode}');
      return compileResult;
    }

    final String frameworkDir = fs.path.join(outputPath, 'App.framework');
    fs.directory(frameworkDir).createSync(recursive: true);
    final String appLib = fs.path.join(frameworkDir, 'App');
    final List<String> linkArgs = commonBuildOptions.toList()..addAll(<String>[
        '-dynamiclib',
        '-Xlinker', '-rpath', '-Xlinker', '@executable_path/Frameworks',
        '-Xlinker', '-rpath', '-Xlinker', '@loader_path/Frameworks',
        '-install_name', '@rpath/App.framework/App',
        '-o', appLib,
        assemblyO,
    ]);
    final RunResult linkResult = await xcode.clang(linkArgs);
    if (linkResult.exitCode != 0) {
      printError('Failed to link AOT snapshot. Linker terminated with exit code ${compileResult.exitCode}');
    }
    return linkResult;
  }

  /// Compiles a Dart file to kernel.
  ///
  /// Returns the output kernel file path, or null on failure.
  Future<String> compileKernel({
    @required TargetPlatform platform,
    @required BuildMode buildMode,
    @required String mainPath,
    @required String packagesPath,
    @required String outputPath,
    @required bool trackWidgetCreation,
    List<String> extraFrontEndOptions = const <String>[],
  }) async {
    final FlutterProject flutterProject = FlutterProject.current();
    final Directory outputDir = fs.directory(outputPath);
    outputDir.createSync(recursive: true);

    printTrace('Compiling Dart to kernel: $mainPath');

    if ((extraFrontEndOptions != null) && extraFrontEndOptions.isNotEmpty)
      printTrace('Extra front-end options: $extraFrontEndOptions');

    final String depfilePath = fs.path.join(outputPath, 'kernel_compile.d');
    final KernelCompiler kernelCompiler = await kernelCompilerFactory.create(flutterProject);
    final CompilerOutput compilerOutput =
      await _timedStep('frontend(CompileTime)', 'aot-kernel',
        () => kernelCompiler.compile(
      sdkRoot: artifacts.getArtifactPath(Artifact.flutterPatchedSdkPath, mode: buildMode),
      mainPath: mainPath,
      packagesPath: packagesPath,
      outputFilePath: getKernelPathForTransformerOptions(
        fs.path.join(outputPath, 'app.dill'),
        trackWidgetCreation: trackWidgetCreation,
      ),
      depFilePath: depfilePath,
      extraFrontEndOptions: extraFrontEndOptions,
      linkPlatformKernelIn: true,
      aot: true,
      trackWidgetCreation: trackWidgetCreation,
      targetProductVm: buildMode == BuildMode.release,
    ));

    // Write path to frontend_server, since things need to be re-generated when that changes.
    final String frontendPath = artifacts.getArtifactPath(Artifact.frontendServerSnapshotForEngineDartSdk);
    await fs.directory(outputPath).childFile('frontend_server.d').writeAsString('frontend_server.d: $frontendPath\n');

    return compilerOutput?.outputFilename;
  }

  bool _isValidAotPlatform(TargetPlatform platform, BuildMode buildMode) {
    if (buildMode == BuildMode.debug)
      return false;
    return const <TargetPlatform>[
      TargetPlatform.android_arm,
      TargetPlatform.android_arm64,
      TargetPlatform.ios,
    ].contains(platform);
  }

  String _getPackagePath(PackageMap packageMap, String package) {
    return fs.path.dirname(fs.path.fromUri(packageMap.map[package]));
  }

  /// This method is used to measure duration of an action and emit it into
  /// verbose output from flutter_tool for other tools (e.g. benchmark runner)
  /// to find.
  /// Important: external performance tracking tools expect format of this
  /// output to be stable.
  Future<T> _timedStep<T>(String marker, String analyticsVar, FutureOr<T> Function() action) async {
    final Stopwatch sw = Stopwatch()..start();
    final T value = await action();
    if (reportTimings) {
      printStatus('$marker: ${sw.elapsedMilliseconds} ms.');
    }
    flutterUsage.sendTiming('build', analyticsVar, Duration(milliseconds: sw.elapsedMilliseconds));
    return value;
  }
}

class JITSnapshotter {
  /// Builds a JIT VM snapshot of the specified kernel. This snapshot includes
  /// data as well as either machine code or DBC, depending on build configuration.
  Future<int> build({
    @required TargetPlatform platform,
    @required BuildMode buildMode,
    @required String mainPath,
    @required String packagesPath,
    @required String outputPath,
    @required String compilationTraceFilePath,
    List<String> extraGenSnapshotOptions = const <String>[],
  }) async {
    if (!_isValidJitPlatform(platform)) {
      printError('${getNameForTargetPlatform(platform)} does not support JIT snapshotting.');
      return 1;
    }

    final Directory outputDir = fs.directory(outputPath);
    outputDir.createSync(recursive: true);

    final String engineVmSnapshotData = artifacts.getArtifactPath(Artifact.vmSnapshotData, mode: buildMode);
    final String engineIsolateSnapshotData = artifacts.getArtifactPath(Artifact.isolateSnapshotData, mode: buildMode);
    final String isolateSnapshotData = fs.path.join(outputDir.path, 'isolate_snapshot_data');
    final String isolateSnapshotInstructions = fs.path.join(outputDir.path, 'isolate_snapshot_instr');

    final List<String> inputPaths = <String>[
      mainPath, compilationTraceFilePath, engineVmSnapshotData, engineIsolateSnapshotData,
    ];

    final String depfilePath = fs.path.join(outputDir.path, 'snapshot.d');
    final List<String> genSnapshotArgs = <String>[
      '--deterministic',
    ];
    if (buildMode == BuildMode.debug) {
      genSnapshotArgs.add('--enable_asserts');
    }
    if (extraGenSnapshotOptions != null && extraGenSnapshotOptions.isNotEmpty) {
      printTrace('Extra gen_snapshot options: $extraGenSnapshotOptions');
      genSnapshotArgs.addAll(extraGenSnapshotOptions);
    }

    final Set<String> outputPaths = <String>{};
    outputPaths.addAll(<String>[isolateSnapshotData, isolateSnapshotInstructions]);

    // There are a couple special cases below where we create a snapshot
    // with only the data section, which only contains interpreted code.
    bool supportsAppJit = true;

    if (platform == TargetPlatform.android_x64 &&
        getCurrentHostPlatform() == HostPlatform.windows_x64) {
      supportsAppJit = false;
      printStatus('Android x64 dynamic build on Windows x64 will use purely interpreted '
                  'code for now (see  https://github.com/flutter/flutter/issues/17489).');
    }

    if (platform == TargetPlatform.android_x86) {
      supportsAppJit = false;
      printStatus('Android x86 dynamic build will use purely interpreted code for now. '
                  'To optimize performance, consider using --target-platform=android-x64.');
    }

    genSnapshotArgs.addAll(<String>[
      '--snapshot_kind=${supportsAppJit ? 'app-jit' : 'app'}',
      '--load_compilation_trace=$compilationTraceFilePath',
      '--load_vm_snapshot_data=$engineVmSnapshotData',
      '--load_isolate_snapshot_data=$engineIsolateSnapshotData',
      '--isolate_snapshot_data=$isolateSnapshotData',
    ]);

    genSnapshotArgs.add('--isolate_snapshot_instructions=$isolateSnapshotInstructions');

    if (platform == TargetPlatform.android_arm) {
      // Use softfp for Android armv7 devices.
      // TODO(cbracken): eliminate this when we fix https://github.com/flutter/flutter/issues/17489
      genSnapshotArgs.add('--no-sim-use-hardfp');

      // Not supported by the Pixel in 32-bit mode.
      genSnapshotArgs.add('--no-use-integer-division');
    }

    genSnapshotArgs.add(mainPath);

    // Verify that all required inputs exist.
    final Iterable<String> missingInputs = inputPaths.where((String p) => !fs.isFileSync(p));
    if (missingInputs.isNotEmpty) {
      printError('Missing input files: $missingInputs from $inputPaths');
      return 1;
    }

    // If inputs and outputs have not changed since last run, skip the build.
    final Fingerprinter fingerprinter = Fingerprinter(
      fingerprintPath: '$depfilePath.fingerprint',
      paths: <String>[mainPath]..addAll(inputPaths)..addAll(outputPaths),
      properties: <String, String>{
        'buildMode': buildMode.toString(),
        'targetPlatform': platform.toString(),
        'entryPoint': mainPath,
        'extraGenSnapshotOptions': extraGenSnapshotOptions.join(' '),
      },
      depfilePaths: <String>[],
    );
    // TODO(jonahwilliams): re-enable once this can be proved correct.
    // if (await fingerprinter.doesFingerprintMatch()) {
    //   printTrace('Skipping JIT snapshot build. Fingerprint match.');
    //   return 0;
    // }

    final SnapshotType snapshotType = SnapshotType(platform, buildMode);
    final int genSnapshotExitCode = await genSnapshot.run(
      snapshotType: snapshotType,
      additionalArgs: genSnapshotArgs,
    );
    if (genSnapshotExitCode != 0) {
      printError('Dart snapshot generator failed with exit code $genSnapshotExitCode');
      return genSnapshotExitCode;
    }

    // Write path to gen_snapshot, since snapshots have to be re-generated when we roll
    // the Dart SDK.
    final String genSnapshotPath = GenSnapshot.getSnapshotterPath(snapshotType);
    await outputDir.childFile('gen_snapshot.d').writeAsString('gen_snapshot.d: $genSnapshotPath\n');

    // Compute and record build fingerprint.
    await fingerprinter.writeFingerprint();
    return 0;
  }

  bool _isValidJitPlatform(TargetPlatform platform) {
    return const <TargetPlatform>[
      TargetPlatform.android_arm,
      TargetPlatform.android_arm64,
      TargetPlatform.android_x86,
      TargetPlatform.android_x64,
    ].contains(platform);
  }
}
