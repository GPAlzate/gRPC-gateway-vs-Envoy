// Copyright 2019 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'package:flutter_tools/src/base/common.dart';
import 'package:flutter_tools/src/base/file_system.dart';
import 'package:flutter_tools/src/base/platform.dart';
import 'package:flutter_tools/src/build_info.dart';
import 'package:flutter_tools/src/cache.dart';
import 'package:flutter_tools/src/device.dart';
import 'package:flutter_tools/src/project.dart';
import 'package:flutter_tools/src/resident_runner.dart';
import 'package:flutter_tools/src/resident_web_runner.dart';
import 'package:flutter_tools/src/version.dart';
import 'package:flutter_tools/src/web/compile.dart';
import 'package:mockito/mockito.dart';

import '../src/common.dart';
import '../src/testbed.dart';

void main() {
  MockWebCompilationProxy mockWebCompilationProxy;
  Testbed testbed;
  MockPlatform mockPlatform;

  setUpAll(() {
    Cache.disableLocking();
  });

  setUp(() {
    mockWebCompilationProxy = MockWebCompilationProxy();
    testbed = Testbed(setup: () {
      fs.file('pubspec.yaml')
        ..createSync()
        ..writeAsStringSync('name: foo\n');
      fs.file('.packages').createSync();
      fs.file(fs.path.join('web', 'index.html')).createSync(recursive: true);
      fs.file(fs.path.join('lib', 'main.dart')).createSync(recursive: true);
      when(mockWebCompilationProxy.initialize(
        projectDirectory: anyNamed('projectDirectory'),
        release: anyNamed('release')
      )).thenAnswer((Invocation invocation) {
        final String path = fs.path.join('.dart_tool', 'build', 'flutter_web', 'foo', 'lib', 'main_web_entrypoint.dart.js');
        fs.file(path).createSync(recursive: true);
        fs.file('$path.map').createSync();
        return Future<bool>.value(true);
      });
    }, overrides: <Type, Generator>{
      WebCompilationProxy: () => mockWebCompilationProxy,
      Platform: () => mockPlatform,
      FlutterVersion: () => MockFlutterVersion(),
    });
  });

  test('Refuses to build for web when missing index.html', () => testbed.run(() async {
    fs.file(fs.path.join('web', 'index.html')).deleteSync();

    expect(buildWeb(
      FlutterProject.current(),
      fs.path.join('lib', 'main.dart'),
      BuildInfo.debug,
    ), throwsA(isInstanceOf<ToolExit>()));
  }));

  test('Refuses to build using runner when missing index.html', () => testbed.run(() async {
    fs.file(fs.path.join('web', 'index.html')).deleteSync();

    final ResidentWebRunner runner = ResidentWebRunner(
      <FlutterDevice>[],
      flutterProject: FlutterProject.current(),
      ipv6: false,
      debuggingOptions: DebuggingOptions.enabled(BuildInfo.debug),
    );
    expect(await runner.run(), 1);
  }));

  test('Can build for web', () => testbed.run(() async {

    await buildWeb(
      FlutterProject.current(),
      fs.path.join('lib', 'main.dart'),
      BuildInfo.debug,
    );
  }));
}

class MockWebCompilationProxy extends Mock implements WebCompilationProxy {}
class MockPlatform extends Mock implements Platform {
  @override
  Map<String, String> environment = <String, String>{
    'FLUTTER_ROOT': '/',
  };
}
class MockFlutterVersion extends Mock implements FlutterVersion {
  @override
  bool get isMaster => true;
}
