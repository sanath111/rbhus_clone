@echo off
setlocal enabledelayedexpansion

rem Kill start menu and taskbar
rem taskkill /F /IM explorer.exe
rem taskkill /F /IM msedge.exe

rem Resolve the full path to the script
set "SOURCE=%~f0"
:loop
for %%I in ("%SOURCE%") do (
    if /i "%%~I" neq "%%~fI" (
        rem SOURCE is a symlink, resolve the target
        set "SOURCE=%%~fI"
        goto loop
    )
)

rem Get the directory of the script
for %%I in ("%SOURCE%") do set "DIR=%%~dpI"
set "DIR=%DIR:~0,-1%"

rem Activate the virtual environment
call "%DIR%\rbhus_clone-env\Scripts\activate.bat"

rem Change to the script directory
pushd "%DIR%"
python "%DIR%\login_prompt.py" %*
popd

endlocal
