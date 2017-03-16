#!/bin/sh

PYTHON=${PYTHON:-3.6}

for REVISION in "$@"; do
    conda build build-$REVISION --python=$PYTHON
done
