@echo off
setlocal

:: Define variables
set "username=kiosk-user"
set "password=password"
set "repo_url=https://github.com/sanath111/rbhus_clone.git"
set "version_tag=v3.0"
set "bootstrap_script=bootstrap.bat"
set "root_dir=D:\"
set "clone_dir=rbhus_clone"
set "output_dir=rbhus_clone_root"
set "shortcut_name=rbhus_clone_launcher_win.lnk"
set "shortcut_target=D:\Repos\rbhus_clone\dist\rbhus_clone_launcher_win.exe"

:: Ensure script is run as administrator
whoami /groups | find "S-1-5-32-544" >nul || (
    echo This script must be run as an administrator.
    pause
    exit /b
)

:: Create a new user
echo Creating new user...
net user %username% %password% /add
if %errorlevel% neq 0 (
    echo Failed to create user. Exiting.
    exit /b
)

:: Create a temporary batch file for the new user
echo Preparing commands for the new user...
set "temp_batch=%temp%\run_commands_as_user.bat"
(
    echo cd /d %root_dir%
    echo git clone %repo_url%
    echo cd %clone_dir%
    echo git checkout %version_tag%
    echo cd ..
    echo mkdir %output_dir%
    echo powershell -Command "Compress-Archive -Path '%output_dir%\*' -DestinationPath '%output_dir%\backup.zip' -Force"
    echo xcopy /E /I "%clone_dir%\template" "%output_dir%\template" /Y
    echo xcopy /E /I "%clone_dir%\database" "%output_dir%\database" /Y
    echo cd %clone_dir%
    echo call %bootstrap_script%
) > "%temp_batch%"

:: Run the temporary batch file as the new user
echo Switching to user %username% to execute commands...
runas /user:%username% /noprofile "%temp_batch%"
if %errorlevel% neq 0 (
    echo Failed to execute commands as user %username%. Exiting.
    del "%temp_batch%"
    exit /b
)

:: Determine the Startup directory
set "startup_dir=C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
if not exist "%startup_dir%" (
    echo Failed to find Startup directory for user %username%. Exiting.
    exit /b
)

:: Create a shortcut in the Startup directory
echo Creating shortcut in Startup directory...
powershell -Command ^
    "$ws = New-Object -ComObject WScript.Shell; ^
    $shortcut = $ws.CreateShortcut('%startup_dir%\%shortcut_name%'); ^
    $shortcut.TargetPath = '%shortcut_target%'; ^
    $shortcut.Save()"

:: Cleanup
del "%temp_batch%"
echo All tasks completed successfully.
pause

endlocal
