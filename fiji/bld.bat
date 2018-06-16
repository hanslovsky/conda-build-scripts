setlocal EnableDelayedExpansion

FOR %%F IN (activate deactivate) DO (
    IF NOT EXIST %PREFIX%\etc\conda\%%F.d MKDIR %PREFIX%\etc\conda\%%F.d
    COPY %RECIPE_DIR%\%%F.bat %PREFIX%\etc\conda\%%F.d\%PKG_NAME%_%%F.bat
)

IF NOT EXIST %PREFIX%\share MKDIR %PREFIX%\share
MOVE Fiji.app %PREFIX%\share\Fiji.app

IF NOT EXIST %PREFIX%\bin MKDIR %PREFIX%\bin
MKLINK "%PREFIX%\bin\ImageJ-win64.exe" "%PREFIX%\share\Fiji.app\ImageJ-win64.exe"
MKLINK "%PREFIX%\bin\imagej" "ImageJ-win64.exe"
MKLINK "%PREFIX%\bin\fiji" "ImageJ-win64.exe"





