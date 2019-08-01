// Copyright 2017 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'package:flutter_tools/src/doctor.dart';
import 'package:flutter_tools/src/macos/cocoapods.dart';
import 'package:flutter_tools/src/macos/cocoapods_validator.dart';
import 'package:mockito/mockito.dart';

import '../src/common.dart';
import '../src/context.dart';

void main() {
  group('CocoaPods validation', () {
    MockCocoaPods cocoaPods;

    setUp(() {
      cocoaPods = MockCocoaPods();
      when(cocoaPods.evaluateCocoaPodsInstallation)
          .thenAnswer((_) async => CocoaPodsStatus.recommended);
      when(cocoaPods.isCocoaPodsInitialized).thenAnswer((_) async => true);
      when(cocoaPods.cocoaPodsVersionText).thenAnswer((_) async => '1.8.0');
    });

    testUsingContext('Emits installed status when CocoaPods is installed', () async {
      final CocoaPodsTestTarget workflow = CocoaPodsTestTarget();
      final ValidationResult result = await workflow.validate();
      expect(result.type, ValidationType.installed);
    }, overrides: <Type, Generator>{
      CocoaPods: () => cocoaPods,
    });

    testUsingContext('Emits missing status when CocoaPods is not installed', () async {
      when(cocoaPods.evaluateCocoaPodsInstallation)
          .thenAnswer((_) async => CocoaPodsStatus.notInstalled);
      final CocoaPodsTestTarget workflow = CocoaPodsTestTarget();
      final ValidationResult result = await workflow.validate();
      expect(result.type, ValidationType.missing);
    }, overrides: <Type, Generator>{
      CocoaPods: () => cocoaPods,
    });

    testUsingContext('Emits partial status when CocoaPods is installed with unknown version', () async {
      when(cocoaPods.evaluateCocoaPodsInstallation)
          .thenAnswer((_) async => CocoaPodsStatus.unknownVersion);
      final CocoaPodsTestTarget workflow = CocoaPodsTestTarget();
      final ValidationResult result = await workflow.validate();
      expect(result.type, ValidationType.partial);
    }, overrides: <Type, Generator>{
      CocoaPods: () => cocoaPods,
    });

    testUsingContext('Emits partial status when CocoaPods is not initialized', () async {
      when(cocoaPods.isCocoaPodsInitialized).thenAnswer((_) async => false);
      final CocoaPodsTestTarget workflow = CocoaPodsTestTarget();
      final ValidationResult result = await workflow.validate();
      expect(result.type, ValidationType.partial);
    }, overrides: <Type, Generator>{
      CocoaPods: () => cocoaPods,
    });

    testUsingContext('Emits partial status when CocoaPods version is too low', () async {
      when(cocoaPods.evaluateCocoaPodsInstallation)
          .thenAnswer((_) async => CocoaPodsStatus.belowRecommendedVersion);
      final CocoaPodsTestTarget workflow = CocoaPodsTestTarget();
      final ValidationResult result = await workflow.validate();
      expect(result.type, ValidationType.partial);
    }, overrides: <Type, Generator>{
      CocoaPods: () => cocoaPods,
    });

    testUsingContext('Emits installed status when homebrew not installed, but not needed', () async {
      final CocoaPodsTestTarget workflow = CocoaPodsTestTarget(hasHomebrew: false);
      final ValidationResult result = await workflow.validate();
      expect(result.type, ValidationType.installed);
    }, overrides: <Type, Generator>{
      CocoaPods: () => cocoaPods,
    });
  });
}

class MockCocoaPods extends Mock implements CocoaPods {}

class CocoaPodsTestTarget extends CocoaPodsValidator {
  CocoaPodsTestTarget({
    this.hasHomebrew = true,
  });

  @override
  final bool hasHomebrew;
}
