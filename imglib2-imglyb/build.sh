IMGLYB_SHARE=$PREFIX/share/imglyb
mkdir -p $IMGLYB_SHARE


mvn clean package
JAR_VERSION=$(mvn org.apache.maven.plugins:maven-help-plugin:2.1.1:evaluate -Dexpression=project.version | grep -v 'INFO')
JAR_NAME=imglib2-imglyb-${JAR_VERSION}.jar
JAR_PATH=target/${JAR_NAME}
cp ${JAR_PATH} ${IMGLYB_SHARE}

python setup.py install --prefix=$PREFIX


echo $JAVA_HOME
mvn -version

# ensure that IMGLYB_JAR is set correctly
mkdir -p $PREFIX/etc/conda/activate.d
echo 'export IMGLYB_JAR_BACKUP=$IMGLYB_JAR' > "$PREFIX/etc/conda/activate.d/imglyb.sh"
echo 'export IMGLYB_JAR=$CONDA_PREFIX/share/imglyb'"/${JAR_NAME}" >> "$PREFIX/etc/conda/activate.d/imglyb.sh"
mkdir -p $PREFIX/etc/conda/deactivate.d
echo 'export IMGLYB_JAR=$IMGLYB_JAR_BACKUP' > "$PREFIX/etc/conda/deactivate.d/imglyb.sh"
echo 'unset IMGLYB_JAR_BACKUP' >> "$PREFIX/etc/conda/deactivate.d/imglyb.sh"
