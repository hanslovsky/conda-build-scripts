#!/bin/sh

BASE_DIR=$PWD
META=meta.yaml
TEMPLATE=${META}.template
BUILDSH=build.sh


for REVISION in "$@"; do
    TARGET=build-${REVISION}
    if [ -e "$TARGET" ]; then
        echo File or directory $TARGET exists; skipping...
    else
        mkdir -p $TARGET
        sed "s/GIT_REVISION/\"${REVISION}\"/" $TEMPLATE > $TARGET/$META
        cp $BUILDSH $TARGET
    fi
    
done
