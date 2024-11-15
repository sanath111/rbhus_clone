#!/usr/bin/env bash
rm -rfv rbhus_clone-env dist build
echo "----- Removed old environment  -------"
python3 -m venv rbhus_clone-env
source rbhus_clone-env/bin/activate
unset PYTHONPATH
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
echo "----- Created python environment -------"
pyinstaller --onefile rbhus_clone_launcher_lin.py
echo "----- Created launcher -------"
deactivate
echo "----- Deactivated environment  -------"
