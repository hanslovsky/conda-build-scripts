#!/bin/sh

PACKAGE=$1
shift
PYTHON=$1
shift



for REVISION in "$@"; do
    CMD="conda build $PACKAGE/build-$REVISION --python=$PYTHON"
    if [ -n "$OUTPUT" ]; then
        CMD="${CMD} --output"
    fi
    $CMD
done
