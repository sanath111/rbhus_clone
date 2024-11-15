import subprocess
import sys
import os

script_path = sys.argv[0]

script_dir = os.path.dirname(os.path.abspath(script_path))

parent_dir = os.path.dirname(script_dir)

bash_file = os.path.join(parent_dir, 'rbhus_clone')

if not os.path.isfile(bash_file):
    print(f"Error: The specified BASH file does not exist: {bash_file}")
    sys.exit(1)

subprocess.run([bash_file], shell=True)
