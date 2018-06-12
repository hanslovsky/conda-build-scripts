SET IMGLYB_SHARE=%PREFIX%\share\imglyb
mkdir %IMGLYB_SHARE%

call mvn clean package
@echo on
if errorlevel 1 exit 1
:: found this to get version from pom.xml:
:: https://stackoverflow.com/questions/38722361/how-to-get-maven-project-version-to-the-windows-command-line-or-batch-file 
:: mvn -q --non-recursive "-Dexec.executable=cmd" "-Dexec.args=/C echo ${project.version}" "org.codehaus.mojo:exec-maven-plugin:1.3.1:exec"
:: https://stackoverflow.com/questions/2323292/windows-batch-assign-output-of-a-program-to-a-variable
for /f %%i in ('mvn -q --non-recursive "-Dexec.executable=cmd" "-Dexec.args=/C echo ${project.version}" "org.codehaus.mojo:exec-maven-plugin:1.3.1:exec"') do SET JAR_VERSION=%%i
if errorlevel 1 exit 1
@echo on
SET JAR_NAME=imglib2-imglyb-%JAR_VERSION%.jar
SET JAR_PATH=target\%JAR_NAME%
copy %JAR_PATH% %IMGLYB_SHARE%
if errorlevel 1 exit 1

pip install --no-deps .
if errorlevel 1 exit 1

echo %JAVA_HOME%
call mvn -version
if errorlevel 1 exit 1
@echo on

:: ensure that IMGLYB_JAR is set correctly
mkdir %PREFIX%\etc\conda\activate.d
:: ignore errorlevel for mkdir commands
:: if errorlevel 1 exit 1
echo SET "IMGLYB_JAR_BACKUP=%IMGLYB_JAR%" > "%PREFIX%\etc\conda\activate.d\imglyb.bat"
echo SET "IMGLYB_JAR=%%CONDA_PREFIX%%\share\imglyb\%JAR_NAME%" >> "%PREFIX%\etc\conda\activate.d\imglyb.bat"
mkdir %PREFIX%\etc\conda\deactivate.d
:: if errorlevel 1 exit 1
echo SET "IMGLYB_JAR=%IMGLYB_JAR_BACKUP%" > "%PREFIX%\etc\conda\deactivate.d\imglyb.bat"
echo SET "IMGLYB_JAR_BACKUP=''" >> "%PREFIX%\etc\conda\deactivate.d\imglyb.bat"
