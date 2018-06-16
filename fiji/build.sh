OS_STRING="$(uname -s)"

case "${OS_STRING}" in
    Linux*) IMAGEJ=ImageJ-linux64;;
    Darwin*) IMAGEJ=ImageJ-macosx;;
    *) IMAGEJ=;;
esac

if [ -e "${IMAGEJ}" ]; then
    "Failed to build: do not understand operating system: ${OS_STRING}"
    exit 1
fi

for CHANGE in "activate" "deactivate"
do
    TARGET_DIR="${CHANGE}.d"
    FILENAME="${CHANGE}.sh"
    mkdir -p "${PREFIX}/etc/conda/${TARGET_DIR}"
    cp "${RECIPE_DIR}/${FILENAME}" "${PREFIX}/etc/conda/${TARGET_DIR}/${PKG_NAME}_${FILENAME}"
done

mkdir -p "${PREFIX}/share"
mv "Fiji.app" "${PREFIX}/share/Fiji.app"

mkdir -p "${PREFIX}/bin"
ln -s "${PREFIX}/share/Fiji.app/${IMAGEJ}" "${PREFIX}/bin/${IMAGEJ}"
ln -s "${PREFIX}/bin/${IMAGEJ}" "${PREFIX}/bin/imagej"
ln -s "${PREFIX}/bin/${IMAGEJ}" "${PREFIX}/bin/fiji"





