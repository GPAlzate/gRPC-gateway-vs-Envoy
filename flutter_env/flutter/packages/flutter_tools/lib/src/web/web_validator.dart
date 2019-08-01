// Copyright 2019 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import '../base/platform.dart';
import '../doctor.dart';
import 'chrome.dart';
import 'workflow.dart';

/// A validator that checks whether chrome is installed and can run.
class WebValidator extends DoctorValidator {
  const WebValidator() : super('Chrome - develop for the web');

  @override
  Future<ValidationResult> validate() async {
    final String chrome = findChromeExecutable();
    final bool canRunChrome = canFindChrome();
    final List<ValidationMessage> messages = <ValidationMessage>[];
    if (platform.environment.containsKey(kChromeEnvironment)) {
      if (!canRunChrome) {
        messages.add(ValidationMessage.hint('$chrome is not executable.'));
      } else {
        messages.add(ValidationMessage('$kChromeEnvironment = $chrome'));
      }
    } else {
      if (!canRunChrome) {
        messages.add(ValidationMessage.hint('$kChromeEnvironment not set'));
      } else {
        messages.add(ValidationMessage('Chrome at $chrome'));
      }
    }
    if (!canRunChrome) {
      return ValidationResult(
        ValidationType.missing,
        messages,
        statusInfo: 'Cannot find chrome executable at $chrome',
      );
    }
    return ValidationResult(
      ValidationType.installed,
      messages,
    );
  }
}
