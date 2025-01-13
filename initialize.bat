@echo off
setlocal

set "script_name=%~f0"
set "username=kiosk-user"
set "repo_url=https://github.com/sanath111/rbhus_clone.git"
set "version_tag=v3.0"
set "bootstrap_script=bootstrap.bat"
set "root_dir=D:\"
set "clone_dir=rbhus_clone"
set "output_dir=rbhus_clone_root"
set "vbs_target=wscript.exe \"%root_dir%rbhus_clone\rbhus_clone.vbs\""

:: set "shortcut_name=rbhus_clone_launcher_win.lnk"
:: set "shortcut_target=D:\rbhus_clone\dist\rbhus_clone_launcher_win.exe"
:: set "startup_dir=C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

echo Initializing...

python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed.
    echo Press Enter to open the Microsoft Store to install Python.
    pause
    python
    echo After installing Python, Press enter to rerun this script.
    pause
    timeout /t 5 >nul
    start "" "%script_name%"
    exit /b
)

:: If Python is installed, proceed with the script
echo Python is installed. Proceeding with the script...

cd /d %root_dir%
git clone %repo_url%
cd %clone_dir%
git checkout %version_tag%
git pull
cd ..
mkdir %output_dir%
powershell -Command "Compress-Archive -Path '%output_dir%\*' -DestinationPath '%output_dir%\backup.zip' -Force"
xcopy /E /I "%clone_dir%\template" "%output_dir%\template" /Y
xcopy /E /I "%clone_dir%\database" "%output_dir%\database" /Y
cd %clone_dir%
call %bootstrap_script%

echo Creating Registry entry...
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "%vbs_target%" /f
pause
exit /b

endlocal
