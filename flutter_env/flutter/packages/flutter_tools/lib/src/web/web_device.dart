// Copyright 2019 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'package:meta/meta.dart';

import '../application_package.dart';
import '../base/file_system.dart';
import '../base/io.dart';
import '../base/platform.dart';
import '../base/process_manager.dart';
import '../build_info.dart';
import '../device.dart';
import '../project.dart';
import 'chrome.dart';
import 'workflow.dart';

class WebApplicationPackage extends ApplicationPackage {
  WebApplicationPackage(this.flutterProject) : super(id: flutterProject.manifest.appName);

  final FlutterProject flutterProject;

  @override
  String get name => flutterProject.manifest.appName;

  /// The location of the web source assets.
  Directory get webSourcePath => flutterProject.directory.childDirectory('web');
}

class WebDevice extends Device {
  WebDevice() : super(
      'web',
      category: Category.web,
      platformType: PlatformType.web,
      ephemeral: false,
  );

  @override
  bool get supportsHotReload => true;

  @override
  bool get supportsHotRestart => true;

  @override
  bool get supportsStartPaused => true;

  @override
  bool get supportsFlutterExit => true;

  @override
  bool get supportsScreenshot => false;

  @override
  void clearLogs() { }

  @override
  DeviceLogReader getLogReader({ApplicationPackage app}) {
    return NoOpDeviceLogReader(app.name);
  }

  @override
  Future<bool> installApp(ApplicationPackage app) async => true;

  @override
  Future<bool> isAppInstalled(ApplicationPackage app) async => true;

  @override
  Future<bool> isLatestBuildInstalled(ApplicationPackage app) async => true;

  @override
  Future<bool> get isLocalEmulator async => false;

  @override
  bool isSupported() => flutterWebEnabled && canFindChrome();

  @override
  String get name => 'web';

  @override
  DevicePortForwarder get portForwarder => const NoOpDevicePortForwarder();

  @override
  Future<String> get sdkNameAndVersion async {
    if (!isSupported()) {
      return 'unknown';
    }
    // See https://bugs.chromium.org/p/chromium/issues/detail?id=158372
    String version = 'unknown';
    if (platform.isWindows) {
      final ProcessResult result = await processManager.run(<String>[
        r'reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'
      ]);
      if (result.exitCode == 0) {
        final List<String> parts = result.stdout.split(RegExp(r'\s+'));
        if (parts.length > 2) {
          version = 'Google Chrome ' + parts[parts.length - 2];
        }
      }
    } else {
      final String chrome = findChromeExecutable();
      final ProcessResult result = await processManager.run(<String>[
        chrome,
        '--version',
      ]);
      if (result.exitCode == 0) {
        version = result.stdout;
      }
    }
    return version;
  }

  @override
  Future<LaunchResult> startApp(
    covariant WebApplicationPackage package, {
    String mainPath,
    String route,
    DebuggingOptions debuggingOptions,
    Map<String, Object> platformArgs,
    bool prebuiltApplication = false,
    bool usesTerminalUi = true,
    bool ipv6 = false,
  }) async {
    // See [ResidentWebRunner.run] in flutter_tools/lib/src/resident_web_runner.dart
    // for the web initialization and server logic.
    return LaunchResult.succeeded(observatoryUri: null);
  }

  @override
  Future<bool> stopApp(ApplicationPackage app) async {
    return true;
  }

  @override
  Future<TargetPlatform> get targetPlatform async => TargetPlatform.web_javascript;

  @override
  Future<bool> uninstallApp(ApplicationPackage app) async => true;

  @override
  bool isSupportedForProject(FlutterProject flutterProject) {
    return flutterProject.web.existsSync();
  }
}

class WebDevices extends PollingDeviceDiscovery {
  WebDevices() : super('web');

  final WebDevice _webDevice = WebDevice();

  @override
  bool get canListAnything => flutterWebEnabled;

  @override
  Future<List<Device>> pollingGetDevices() async {
    return <Device>[
      _webDevice,
    ];
  }

  @override
  bool get supportsPlatform => flutterWebEnabled;
}

@visibleForTesting
String parseVersionForWindows(String input) {
  return input.split(RegExp('\w')).last;
}
