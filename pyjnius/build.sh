PYJNIUS_SHARE=$PREFIX/share/pyjnius
mkdir -p $PYJNIUS_SHARE

make
make tests
python setup.py install


cp build/pyjnius.jar $PYJNIUS_SHARE
echo $PYJNIUS_SHARE
