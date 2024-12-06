@echo off
setlocal

cd D:
mkdir "rbhus_clone"
cd "rbhus_clone"
git clone https://github.com/sanath111/rbhus_clone.git
git checkout v3.0
cd D:
mkdir "rbhus_clone_root"
powershell -command "Compress-Archive -Path 'rbhus_clone_root\*' -DestinationPath 'rbhus_clone_root\backup.zip' -Force"
xcopy /E /I "rbhus_clone\template" "rbhus_clone_root\template"
xcopy /E /I "rbhus_clone\database" "rbhus_clone_root\database"
cd "rbhus_clone"
call "bootstrap.bat"

endlocal
