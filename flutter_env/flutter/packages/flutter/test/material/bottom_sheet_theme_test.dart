// Copyright 2019 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('BottomSheetThemeData copyWith, ==, hashCode basics', () {
    expect(const BottomSheetThemeData(), const BottomSheetThemeData().copyWith());
    expect(const BottomSheetThemeData().hashCode, const BottomSheetThemeData().copyWith().hashCode);
  });

  test('BottomSheetThemeData null fields by default', () {
    const BottomSheetThemeData bottomSheetTheme = BottomSheetThemeData();
    expect(bottomSheetTheme.backgroundColor, null);
    expect(bottomSheetTheme.elevation, null);
    expect(bottomSheetTheme.shape, null);
  });

  testWidgets('Default BottomSheetThemeData debugFillProperties', (WidgetTester tester) async {
    final DiagnosticPropertiesBuilder builder = DiagnosticPropertiesBuilder();
    const BottomSheetThemeData().debugFillProperties(builder);

    final List<String> description = builder.properties
        .where((DiagnosticsNode node) => !node.isFiltered(DiagnosticLevel.info))
        .map((DiagnosticsNode node) => node.toString())
        .toList();

    expect(description, <String>[]);
  });

  testWidgets('BottomSheetThemeData implements debugFillProperties', (WidgetTester tester) async {
    final DiagnosticPropertiesBuilder builder = DiagnosticPropertiesBuilder();
    BottomSheetThemeData(
      backgroundColor: const Color(0xFFFFFFFF),
      elevation: 2.0,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(2.0)),
    ).debugFillProperties(builder);

    final List<String> description = builder.properties
        .where((DiagnosticsNode node) => !node.isFiltered(DiagnosticLevel.info))
        .map((DiagnosticsNode node) => node.toString())
        .toList();

    expect(description, <String>[
      'backgroundColor: Color(0xffffffff)',
      'elevation: 2.0',
      'shape: RoundedRectangleBorder(BorderSide(Color(0xff000000), 0.0, BorderStyle.none), BorderRadius.circular(2.0))',
    ]);
  });

  testWidgets('Passing no BottomSheetThemeData returns defaults', (WidgetTester tester) async {
    await tester.pumpWidget(MaterialApp(
      home: Scaffold(
        body: BottomSheet(
          onClosing: () {},
          builder: (BuildContext context) {
            return Container();
          },
        ),
      ),
    ));

    final Material material = tester.widget<Material>(
      find.descendant(
        of: find.byType(BottomSheet),
        matching: find.byType(Material),
      ).first,
    );
    expect(material.color, null);
    expect(material.elevation, 0.0);
    expect(material.shape, null);
  });

  testWidgets('BottomSheet uses values from BottomSheetThemeData', (WidgetTester tester) async {
    final BottomSheetThemeData bottomSheetTheme = _bottomSheetTheme();

    await tester.pumpWidget(MaterialApp(
      theme: ThemeData(bottomSheetTheme: bottomSheetTheme),
      home: Scaffold(
        body: BottomSheet(
          onClosing: () {},
          builder: (BuildContext context) {
            return Container();
          },
        ),
      ),
    ));

    final Material material = tester.widget<Material>(
      find.descendant(
        of: find.byType(BottomSheet),
        matching: find.byType(Material),
      ).first,
    );
    expect(material.color, bottomSheetTheme.backgroundColor);
    expect(material.elevation, bottomSheetTheme.elevation);
    expect(material.shape, bottomSheetTheme.shape);
  });

  testWidgets('BottomSheet widget properties take priority over theme', (WidgetTester tester) async {
    const Color backgroundColor = Colors.purple;
    const double elevation = 7.0;
    const ShapeBorder shape = RoundedRectangleBorder(
      borderRadius: BorderRadius.all(Radius.circular(9.0)),
    );

    await tester.pumpWidget(MaterialApp(
      theme: ThemeData(bottomSheetTheme: _bottomSheetTheme()),
      home: Scaffold(
        body: BottomSheet(
          backgroundColor: backgroundColor,
          elevation: elevation,
          shape: shape,
          onClosing: () {},
          builder: (BuildContext context) {
            return Container();
          },
        ),
      ),
    ));

    final Material material = tester.widget<Material>(
      find.descendant(
        of: find.byType(BottomSheet),
        matching: find.byType(Material),
      ).first,
    );
    expect(material.color, backgroundColor);
    expect(material.elevation, elevation);
    expect(material.shape, shape);
  });
}

BottomSheetThemeData _bottomSheetTheme() {
  return BottomSheetThemeData(
    backgroundColor: Colors.orange,
    elevation: 12.0,
    shape: BeveledRectangleBorder(borderRadius: BorderRadius.circular(12)),
  );
}
