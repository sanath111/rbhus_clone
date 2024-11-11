#!/usr/bin/env bash
rm -rf rbhus_clone-env
python3 -m venv rbhus_clone-env
source rbhus_clone-env/bin/activate
unset PYTHONPATH
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
echo "----- Created venv -------"
