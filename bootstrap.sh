#!/usr/bin/env bash
rm -rfv .venv dist build
echo "----- Removed old environment  -------"
python3 -m venv .venv --system-site-packages
echo "----- Created python environment -------"
source .venv/bin/activate
echo "----- Activated python environment  -------"
unset PYTHONPATH
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
echo "----- Installed dependencies -------"
pyinstaller --onefile rbhus_clone_launcher_lin.py
echo "----- Created launcher -------"
deactivate
echo "----- Deactivated environment  -------"
