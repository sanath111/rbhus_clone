@echo off
setlocal

cd "D:\" || exit /b
git clone https://github.com/sanath111/rbhus_clone.git
cd rbhus_clone || exit /b
git checkout v3.0
cd .. || exit /b
mkdir "D:\rbhus_clone_root"
powershell -command "Compress-Archive -Path 'D:\rbhus_clone_root\*' -DestinationPath 'D:\rbhus_clone_root\backup.zip' -Force"
xcopy /E /I "D:\rbhus_clone\template" "D:\rbhus_clone_root\template"
xcopy /E /I "D:\rbhus_clone\database" "D:\rbhus_clone_root\database"

endlocal
