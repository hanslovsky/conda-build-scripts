#!/bin/sh

PYTHON=${PYTHON:-3.6}

for REVISION in "$@"; do
    CMD="conda build build-$REVISION --python=$PYTHON"
    if [ -n "$OUTPUT" ]; then
        CMD="${CMD} --output"
    fi
    $CMD
done
