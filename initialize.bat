@echo off
setlocal

set "username=kiosk-user"
set "repo_url=https://github.com/sanath111/rbhus_clone.git"
set "version_tag=v3.0"
set "bootstrap_script=bootstrap.bat"
set "root_dir=D:\"
set "clone_dir=rbhus_clone"
set "output_dir=rbhus_clone_root"
set "shortcut_name=rbhus_clone_launcher_win.lnk"
set "shortcut_target=D:\rbhus_clone\dist\rbhus_clone_launcher_win.exe"
set "startup_dir=C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

echo Initializing...
cd /d %root_dir%
git clone %repo_url%
cd %clone_dir%
git checkout %version_tag%
cd ..
mkdir %output_dir%
powershell -Command "Compress-Archive -Path '%output_dir%\*' -DestinationPath '%output_dir%\backup.zip' -Force"
xcopy /E /I "%clone_dir%\template" "%output_dir%\template" /Y
xcopy /E /I "%clone_dir%\database" "%output_dir%\database" /Y
cd %clone_dir%
call %bootstrap_script%

echo Creating shortcut in Startup directory...
powershell -Command ^
    "$ws = New-Object -ComObject WScript.Shell; ^
    $shortcut = $ws.CreateShortcut('%startup_dir%\%shortcut_name%'); ^
    $shortcut.TargetPath = '%shortcut_target%'; ^
    $shortcut.Save()"

endlocal
