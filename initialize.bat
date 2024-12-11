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
set "shortcut_target="D:\Repos\rbhus_clone\dist\rbhus_clone_launcher_win.exe""

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

:: Switch to the new user and execute commands
echo Switching to user %username%...
runas /user:%username% cmd /c ^
    ^"cd /d %root_dir% && ^
    git clone %repo_url% && ^
    cd %clone_dir% && ^
    git checkout %version_tag% && ^
    cd .. && ^
    mkdir %output_dir% && ^
    powershell -command "Compress-Archive -Path '%output_dir%\*' -DestinationPath '%output_dir%\backup.zip' -Force" && ^
    xcopy /E /I "%clone_dir%\template" "%output_dir%\template" /Y && ^
    xcopy /E /I "%clone_dir%\database" "%output_dir%\database" /Y && ^
    cd %clone_dir% && ^
    call %bootstrap_script%^"

:: Determine the Startup directory for the new user
for /f "tokens=3 delims= " %%A in ('reg query "HKU\.DEFAULT\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /v Startup') do (
    set "startup_dir=%%A"
)

if not defined startup_dir (
    echo Failed to determine the Startup directory. Exiting.
    exit /b
)

:: Create a shortcut in the Startup folder
echo Creating shortcut in Startup directory...
powershell -Command ^
    "$ws = New-Object -ComObject WScript.Shell; ^
    $shortcut = $ws.CreateShortcut('%startup_dir%\%shortcut_name%'); ^
    $shortcut.TargetPath = '%shortcut_target%'; ^
    $shortcut.Save()"

:: Completion message
echo All tasks completed successfully.
pause

:: End the local environment
endlocal
