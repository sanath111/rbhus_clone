@echo off
setlocal

cd D:
git clone https://github.com/sanath111/rbhus_clone.git
cd rbhus_clone || exit /b
git checkout v3.0
cd .. || exit /b
mkdir "rbhus_clone_root"
powershell -command "Compress-Archive -Path 'rbhus_clone_root\*' -DestinationPath 'rbhus_clone_root\backup.zip' -Force"
xcopy /E /I "rbhus_clone\template" "rbhus_clone_root\template"
xcopy /E /I "rbhus_clone\database" "rbhus_clone_root\database"
cd "rbhus_clone" || exit /b
call "bootstrap.bat"

endlocal
