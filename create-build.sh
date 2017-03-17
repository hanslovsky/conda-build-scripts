#!/bin/sh

BASE_DIR=$PWD
META=meta.yaml
TEMPLATE=${META}.template
BUILDSH=build.sh
TESTPY=run_test.py

PACKAGE=$1
shift

for REVISION in "$@"; do
    TARGET=$PACKAGE/build-${REVISION}
    if [ -e "$TARGET" ]; then
        echo File or directory $TARGET exists; skipping...
    else
        mkdir -p $TARGET
        sed "s/GIT_REVISION/\"${REVISION}\"/" $PACKAGE/$TEMPLATE > $TARGET/$META
        cp $PACKAGE/$BUILDSH $TARGET
        if [ -e "$PACKAGE/$TESTPY" ]; then
            cp $PACKAGE/$TESTPY $TARGET
        fi
    fi
done
