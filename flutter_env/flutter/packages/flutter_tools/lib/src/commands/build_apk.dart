// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'dart:async';

import '../android/apk.dart';
import '../base/terminal.dart';
import '../build_info.dart';
import '../globals.dart';
import '../project.dart';
import '../runner/flutter_command.dart' show DevelopmentArtifact, FlutterCommandResult;
import 'build.dart';

class BuildApkCommand extends BuildSubCommand {
  BuildApkCommand({bool verboseHelp = false}) {
    usesTargetOption();
    addBuildModeFlags(verboseHelp: verboseHelp);
    usesFlavorOption();
    usesPubOption();
    usesBuildNumberOption();
    usesBuildNameOption();

    argParser
      ..addFlag('track-widget-creation', negatable: false, hide: !verboseHelp)
      ..addFlag('split-per-abi',
        negatable: false,
        help: 'Whether to split the APKs per ABIs.'
              'To learn more, see: https://developer.android.com/studio/build/configure-apk-splits#configure-abi-split',
      )
      ..addMultiOption('target-platform',
        splitCommas: true,
        defaultsTo: <String>['android-arm', 'android-arm64'],
        allowed: <String>['android-arm', 'android-arm64', 'android-x86', 'android-x64'],
        help: 'The target platform for which the app is compiled.',
      );
  }

  @override
  final String name = 'apk';

  @override
  Future<Set<DevelopmentArtifact>> get requiredArtifacts async => const <DevelopmentArtifact>{
    DevelopmentArtifact.universal,
    DevelopmentArtifact.android,
  };

  @override
  final String description = 'Build an Android APK file from your app.\n\n'
    'This command can build debug and release versions of your application. \'debug\' builds support '
    'debugging and a quick development cycle. \'release\' builds don\'t support debugging and are '
    'suitable for deploying to app stores.';

  @override
  Future<FlutterCommandResult> runCommand() async {
    final BuildInfo buildInfo = getBuildInfo();
    final AndroidBuildInfo androidBuildInfo = AndroidBuildInfo(buildInfo,
      splitPerAbi: argResults['split-per-abi'],
      targetArchs: argResults['target-platform'].map<AndroidArch>(getAndroidArchForName)
    );

    if (buildInfo.isRelease && !androidBuildInfo.splitPerAbi && androidBuildInfo.targetArchs.length > 1) {
      final String targetPlatforms = argResults['target-platform'].join(', ');

      printStatus('You are building a fat APK that includes binaries for '
                  '$targetPlatforms.', emphasis: true, color: TerminalColor.green);
      printStatus('If you are deploying the app to the Play Store, '
                  'it\'s recommended to use app bundles or split the APK to reduce the APK size.', emphasis: true);
      printStatus('To generate an app bundle, run:', emphasis: true, indent: 4);
      printStatus('flutter build appbundle '
                  '--target-platform ${targetPlatforms.replaceAll(' ', '')}',indent: 8);
      printStatus('Learn more on: https://developer.android.com/guide/app-bundle',indent: 8);
      printStatus('To split the APKs per ABI, run:', emphasis: true, indent: 4);
      printStatus('flutter build apk '
                  '--target-platform ${targetPlatforms.replaceAll(' ', '')} '
                  '--split-per-abi', indent: 8);
      printStatus('Learn more on:  https://developer.android.com/studio/build/configure-apk-splits#configure-abi-split',indent: 8);
    }
    await buildApk(
      project: FlutterProject.current(),
      target: targetFile,
      androidBuildInfo: androidBuildInfo,
    );
    return null;
  }
}
