@echo off
rmdir /s /q rbhus_clone-env
python -m venv rbhus_clone-env
call rbhus_clone-env\Scripts\activate.bat
set PYTHONPATH=
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo "----- Created venv -------"
