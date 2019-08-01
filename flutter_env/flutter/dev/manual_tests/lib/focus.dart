// Copyright 2019 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter/widgets.dart';

void main() {
  runApp(const MaterialApp(
    title: 'Focus Demo',
    home: FocusDemo(),
  ));
}

class DemoButton extends StatelessWidget {
  const DemoButton({this.name});

  final String name;

  void _handleOnPressed() {
    print('Button $name pressed.');
  }

  @override
  Widget build(BuildContext context) {
    return FlatButton(
      focusColor: Colors.red,
      hoverColor: Colors.blue,
      onPressed: () => _handleOnPressed(),
      child: Text(name),
    );
  }
}

class FocusDemo extends StatefulWidget {
  const FocusDemo({Key key}) : super(key: key);

  @override
  _FocusDemoState createState() => _FocusDemoState();
}

class _FocusDemoState extends State<FocusDemo> {
  FocusNode outlineFocus;

  @override
  void initState() {
    super.initState();
    outlineFocus = FocusNode(debugLabel: 'Demo Focus Node');
  }

  @override
  void dispose() {
    outlineFocus.dispose();
    super.dispose();
  }

  bool _handleKeyPress(FocusNode node, RawKeyEvent event) {
    if (event is RawKeyDownEvent) {
      print('Scope got key event: ${event.logicalKey}, $node');
      print('Keys down: ${RawKeyboard.instance.keysPressed}');
      if (event.logicalKey == LogicalKeyboardKey.tab) {
        debugDumpFocusTree();
        if (event.isShiftPressed) {
          print('Moving to previous.');
          node.previousFocus();
          return true;
        } else {
          print('Moving to next.');
          node.nextFocus();
          return true;
        }
      }
      if (event.logicalKey == LogicalKeyboardKey.arrowLeft) {
        node.focusInDirection(TraversalDirection.left);
        return true;
      }
      if (event.logicalKey == LogicalKeyboardKey.arrowRight) {
        node.focusInDirection(TraversalDirection.right);
        return true;
      }
      if (event.logicalKey == LogicalKeyboardKey.arrowUp) {
        node.focusInDirection(TraversalDirection.up);
        return true;
      }
      if (event.logicalKey == LogicalKeyboardKey.arrowDown) {
        node.focusInDirection(TraversalDirection.down);
        return true;
      }
    }
    return false;
  }

  @override
  Widget build(BuildContext context) {
    final TextTheme textTheme = Theme.of(context).textTheme;

    return DefaultFocusTraversal(
      policy: ReadingOrderTraversalPolicy(),
      child: FocusScope(
        debugLabel: 'Scope',
        onKey: _handleKeyPress,
        autofocus: true,
        child: DefaultTextStyle(
          style: textTheme.display1,
          child: Scaffold(
            appBar: AppBar(
              title: const Text('Focus Demo'),
            ),
            floatingActionButton: FloatingActionButton(
              child: const Text('+'),
              onPressed: () {},
            ),
            body: Center(
              child: Builder(builder: (BuildContext context) {
                return Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: const <Widget>[
                        DemoButton(name: 'One'),
                      ],
                    ),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: const <Widget>[
                        DemoButton(name: 'Two'),
                        DemoButton(name: 'Three'),
                      ],
                    ),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: const <Widget>[
                        DemoButton(name: 'Four'),
                        DemoButton(name: 'Five'),
                        DemoButton(name: 'Six'),
                      ],
                    ),
                    OutlineButton(onPressed: () => print('pressed'), child: const Text('PRESS ME')),
                    const Padding(
                      padding: EdgeInsets.all(8.0),
                      child: TextField(
                        decoration: InputDecoration(labelText: 'Enter Text', filled: true),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: TextField(
                        decoration: InputDecoration(
                          border: OutlineInputBorder(),
                          labelText: 'Enter Text',
                          filled: false,
                        ),
                      ),
                    ),
                  ],
                );
              }),
            ),
          ),
        ),
      ),
    );
  }
}
