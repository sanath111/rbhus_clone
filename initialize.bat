@echo off
setlocal

REM Change to the D: drive and root directory
cd /d D:\ || exit /b

REM Clone the Git repository
git clone https://github.com/sanath111/rbhus_clone.git

REM Change to the cloned directory
cd rbhus_clone || exit /b

REM Checkout the specified version
git checkout v3.0

REM Change back to the previous directory
cd .. || exit /b

REM Create the rbhus_clone_root directory
mkdir "rbhus_clone_root"

REM Create a zip file of the contents of rbhus_clone_root
powershell -command "Compress-Archive -Path 'rbhus_clone_root\*' -DestinationPath 'rbhus_clone_root\backup.zip' -Force"

REM Copy the template and database directories to rbhus_clone_root
xcopy /E /I "rbhus_clone\template" "rbhus_clone_root\template" /Y
xcopy /E /I "rbhus_clone\database" "rbhus_clone_root\database" /Y

REM Change to the rbhus_clone directory again
cd "rbhus_clone" || exit /b

REM Execute the bootstrap.bat script
call "bootstrap.bat"

endlocal
