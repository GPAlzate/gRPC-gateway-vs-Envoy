#!/bin/bash

set -e

GIT_REVISION=$(git rev-parse HEAD)

pushd dev/integration_tests/release_smoke_test

../../../bin/flutter build appbundle --target-platform android-arm,android-arm64

echo $GCLOUD_FIREBASE_TESTLAB_KEY > ${HOME}/gcloud-service-key.json
gcloud auth activate-service-account --key-file=${HOME}/gcloud-service-key.json
gcloud --quiet config set project flutter-infra

# Run the test.
gcloud firebase test android run --type robo \
  --app build/app/outputs/bundle/release/app.aab \
  --timeout 2m \
  --results-bucket=gs://flutter_firebase_testlab \
  --results-dir=release_smoke_test/$GIT_REVISION/$CIRRUS_BUILD_ID

# Check logcat for "E/flutter" - if it's there, something's wrong.
gsutil cp gs://flutter_firebase_testlab/release_smoke_test/$GIT_REVISION/$CIRRUS_BUILD_ID/walleye-26-en-portrait/logcat /tmp/logcat
! grep "E/flutter" /tmp/logcat || false
grep "I/flutter" /tmp/logcat

popd
