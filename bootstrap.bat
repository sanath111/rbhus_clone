@echo off
rmdir /s /q rbhus_clone-env
rmdir /s /q dist
rmdir /s /q build
echo "----- Removed old environment  -------"
python -m venv rbhus_clone-env
call rbhus_clone-env\Scripts\activate.bat
set PYTHONPATH=
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo "----- Created python environment -------"
pyinstaller --onefile rbhus_clone_launcher_win.py
echo "----- Created launcher -------"
deactivate
echo "----- Deactivated environment -------"
