// Copyright 2017 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'dart:async';
import 'dart:io';
import 'dart:math' as math;
import 'dart:typed_data';

import 'package:flutter/foundation.dart';
import 'package:flutter/painting.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/mockito.dart';

import '../rendering/rendering_tester.dart';
import 'image_data.dart';
import 'mocks_for_image_cache.dart';

void main() {
  group(ImageProvider, () {
    setUpAll(() {
      TestRenderingFlutterBinding(); // initializes the imageCache
    });

    group('Image cache', () {
      tearDown(() {
        imageCache.clear();
      });

      test('ImageProvider can evict images', () async {
        final Uint8List bytes = Uint8List.fromList(kTransparentImage);
        final MemoryImage imageProvider = MemoryImage(bytes);
        final ImageStream stream = imageProvider.resolve(ImageConfiguration.empty);
        final Completer<void> completer = Completer<void>();
        stream.addListener(ImageStreamListener((ImageInfo info, bool syncCall) => completer.complete()));
        await completer.future;

        expect(imageCache.currentSize, 1);
        expect(await MemoryImage(bytes).evict(), true);
        expect(imageCache.currentSize, 0);
      });

      test('ImageProvider.evict respects the provided ImageCache', () async {
        final ImageCache otherCache = ImageCache();
        final Uint8List bytes = Uint8List.fromList(kTransparentImage);
        final MemoryImage imageProvider = MemoryImage(bytes);
        otherCache.putIfAbsent(imageProvider, () => imageProvider.load(imageProvider));
        final ImageStream stream = imageProvider.resolve(ImageConfiguration.empty);
        final Completer<void> completer = Completer<void>();
        stream.addListener(ImageStreamListener((ImageInfo info, bool syncCall) => completer.complete()));
        await completer.future;

        expect(otherCache.currentSize, 1);
        expect(imageCache.currentSize, 1);
        expect(await imageProvider.evict(cache: otherCache), true);
        expect(otherCache.currentSize, 0);
        expect(imageCache.currentSize, 1);
      });

      test('ImageProvider errors can always be caught', () async {
        final ErrorImageProvider imageProvider = ErrorImageProvider();
        final Completer<bool> caughtError = Completer<bool>();
        FlutterError.onError = (FlutterErrorDetails details) {
          caughtError.complete(false);
        };
        final ImageStream stream = imageProvider.resolve(ImageConfiguration.empty);
        stream.addListener(ImageStreamListener((ImageInfo info, bool syncCall) {
          caughtError.complete(false);
        }, onError: (dynamic error, StackTrace stackTrace) {
          caughtError.complete(true);
        }));
        expect(await caughtError.future, true);
      });
    });

    test('obtainKey errors will be caught', () async {
      final ImageProvider imageProvider = ObtainKeyErrorImageProvider();
      final Completer<bool> caughtError = Completer<bool>();
      FlutterError.onError = (FlutterErrorDetails details) {
        caughtError.complete(false);
      };
      final ImageStream stream = imageProvider.resolve(ImageConfiguration.empty);
      stream.addListener(ImageStreamListener((ImageInfo info, bool syncCall) {
        caughtError.complete(false);
      }, onError: (dynamic error, StackTrace stackTrace) {
        caughtError.complete(true);
      }));
      expect(await caughtError.future, true);
    });

    test('resolve sync errors will be caught', () async {
      bool uncaught = false;
      final Zone testZone = Zone.current.fork(specification: ZoneSpecification(
        handleUncaughtError: (Zone zone, ZoneDelegate zoneDelegate, Zone parent, Object error, StackTrace stackTrace) {
          uncaught = true;
        },
      ));
      await testZone.run(() async {
        final ImageProvider imageProvider = LoadErrorImageProvider();
        final Completer<bool> caughtError = Completer<bool>();
        FlutterError.onError = (FlutterErrorDetails details) {
          throw Error();
        };
        final ImageStream result = imageProvider.resolve(ImageConfiguration.empty);
        result.addListener(ImageStreamListener((ImageInfo info, bool syncCall) {
        }, onError: (dynamic error, StackTrace stackTrace) {
          caughtError.complete(true);
        }));
        expect(await caughtError.future, true);
      });
      expect(uncaught, false);
    });

    test('resolve errors in the completer will be caught', () async {
      bool uncaught = false;
      final Zone testZone = Zone.current.fork(specification: ZoneSpecification(
        handleUncaughtError: (Zone zone, ZoneDelegate zoneDelegate, Zone parent, Object error, StackTrace stackTrace) {
          uncaught = true;
        },
      ));
      await testZone.run(() async {
        final ImageProvider imageProvider = LoadErrorCompleterImageProvider();
        final Completer<bool> caughtError = Completer<bool>();
        FlutterError.onError = (FlutterErrorDetails details) {
          throw Error();
        };
        final ImageStream result = imageProvider.resolve(ImageConfiguration.empty);
        result.addListener(ImageStreamListener((ImageInfo info, bool syncCall) {
        }, onError: (dynamic error, StackTrace stackTrace) {
          caughtError.complete(true);
        }));
        expect(await caughtError.future, true);
      });
      expect(uncaught, false);
    });

    group(NetworkImage, () {
      MockHttpClient httpClient;

      setUp(() {
        httpClient = MockHttpClient();
        debugNetworkImageHttpClientProvider = () => httpClient;
      });

      tearDown(() {
        debugNetworkImageHttpClientProvider = null;
      });

      test('Disallows null urls', () {
        expect(() {
          NetworkImage(nonconst(null));
        }, throwsAssertionError);
      });

      test('Uses the HttpClient provided by debugNetworkImageHttpClientProvider if set', () async {
        when(httpClient.getUrl(any)).thenThrow('client1');
        final List<dynamic> capturedErrors = <dynamic>[];

        Future<void> loadNetworkImage() async {
          final NetworkImage networkImage = NetworkImage(nonconst('foo'));
          final ImageStreamCompleter completer = networkImage.load(networkImage);
          completer.addListener(ImageStreamListener(
            (ImageInfo image, bool synchronousCall) { },
            onError: (dynamic error, StackTrace stackTrace) {
              capturedErrors.add(error);
            },
          ));
          await Future<void>.value();
        }

        await loadNetworkImage();
        expect(capturedErrors, <dynamic>['client1']);
        final MockHttpClient client2 = MockHttpClient();
        when(client2.getUrl(any)).thenThrow('client2');
        debugNetworkImageHttpClientProvider = () => client2;
        await loadNetworkImage();
        expect(capturedErrors, <dynamic>['client1', 'client2']);
      }, skip: isBrowser);

      test('Propagates http client errors during resolve()', () async {
        when(httpClient.getUrl(any)).thenThrow(Error());
        bool uncaught = false;

        await runZoned(() async {
          const ImageProvider imageProvider = NetworkImage('asdasdasdas');
          final Completer<bool> caughtError = Completer<bool>();
          FlutterError.onError = (FlutterErrorDetails details) {
            throw Error();
          };
          final ImageStream result = imageProvider.resolve(ImageConfiguration.empty);
          result.addListener(ImageStreamListener((ImageInfo info, bool syncCall) {
          }, onError: (dynamic error, StackTrace stackTrace) {
            caughtError.complete(true);
          }));
          expect(await caughtError.future, true);
        }, zoneSpecification: ZoneSpecification(
          handleUncaughtError: (Zone zone, ZoneDelegate zoneDelegate, Zone parent, Object error, StackTrace stackTrace) {
            uncaught = true;
          },
        ));
        expect(uncaught, false);
      });

      test('Notifies listeners of chunk events', () async {
        final List<List<int>> chunks = <List<int>>[];
        const int chunkSize = 8;
        for (int offset = 0; offset < kTransparentImage.length; offset += chunkSize) {
          chunks.add(kTransparentImage.skip(offset).take(chunkSize).toList());
        }
        final Completer<void> imageAvailable = Completer<void>();
        final MockHttpClientRequest request = MockHttpClientRequest();
        final MockHttpClientResponse response = MockHttpClientResponse();
        when(httpClient.getUrl(any)).thenAnswer((_) => Future<HttpClientRequest>.value(request));
        when(request.close()).thenAnswer((_) => Future<HttpClientResponse>.value(response));
        when(response.statusCode).thenReturn(HttpStatus.ok);
        when(response.contentLength).thenReturn(kTransparentImage.length);
        when(response.listen(
          any,
          onDone: anyNamed('onDone'),
          onError: anyNamed('onError'),
          cancelOnError: anyNamed('cancelOnError'),
        )).thenAnswer((Invocation invocation) {
          final void Function(List<int>) onData = invocation.positionalArguments[0];
          final void Function(Object) onError = invocation.namedArguments[#onError];
          final void Function() onDone = invocation.namedArguments[#onDone];
          final bool cancelOnError = invocation.namedArguments[#cancelOnError];

          return Stream<List<int>>.fromIterable(chunks).listen(
            onData,
            onDone: onDone,
            onError: onError,
            cancelOnError: cancelOnError,
          );
        });

        final ImageProvider imageProvider = NetworkImage(nonconst('foo'));
        final ImageStream result = imageProvider.resolve(ImageConfiguration.empty);
        final List<ImageChunkEvent> events = <ImageChunkEvent>[];
        result.addListener(ImageStreamListener(
          (ImageInfo image, bool synchronousCall) {
            imageAvailable.complete();
          },
          onChunk: (ImageChunkEvent event) {
            events.add(event);
          },
          onError: (dynamic error, StackTrace stackTrace) {
            imageAvailable.completeError(error, stackTrace);
          },
        ));
        await imageAvailable.future;
        expect(events.length, chunks.length);
        for (int i = 0; i < events.length; i++) {
          expect(events[i].cumulativeBytesLoaded, math.min((i + 1) * chunkSize, kTransparentImage.length));
          expect(events[i].expectedTotalBytes, kTransparentImage.length);
        }
      }, skip: isBrowser);
    });
  });
}

class MockHttpClient extends Mock implements HttpClient {}
class MockHttpClientRequest extends Mock implements HttpClientRequest {}
class MockHttpClientResponse extends Mock implements HttpClientResponse {}
