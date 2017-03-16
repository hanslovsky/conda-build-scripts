IMGLYB_SHARE=$PREFIX/share/imglyb
mkdir -p $IMGLYB_SHARE
cp pyjnius-bdv.py $IMGLYB_SHARE
cp butterfly.jpg $IMGLYB_SHARE

LOCAL_REPO=$PREFIX/.m2
mkdir -p $LOCAL_REPO
mvn clean package

JAR_NAME=$(basename `ls target/imglib2-*with-dependencies*jar`)
cp target/$JAR_NAME $IMGLYB_SHARE




# ensure that IMGLYB_JAR is set correctly
mkdir -p $PREFIX/etc/conda/activate.d
echo 'export IMGLYB_JAR_BACKUP=$IMGLYB_JAR' > "$PREFIX/etc/conda/activate.d/imglyb_jar.sh"
echo 'export IMGLYB_JAR=$CONDA_PREFIX/share/imglyb'"/${JAR_NAME}" >> "$PREFIX/etc/conda/activate.d/imglyb_jar.sh"
mkdir -p $PREFIX/etc/conda/deactivate.d
echo 'export IMGLYB_JAR=$IMGLYB_JAR_BACKUP' > "$PREFIX/etc/conda/deactivate.d/imglyb_jar.sh"
