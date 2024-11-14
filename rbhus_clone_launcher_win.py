import subprocess
import sys
import os

script_path = sys.argv[0]

script_dir = os.path.dirname(os.path.abspath(script_path))

parent_dir = os.path.dirname(script_dir)

bat_file = os.path.join(parent_dir, 'rbhus_clone.bat')

if not os.path.isfile(bat_file):
    print(f"Error: The specified BAT file does not exist: {bat_file}")
    sys.exit(1)

subprocess.run([bat_file], shell=True)
