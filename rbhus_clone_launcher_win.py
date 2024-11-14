import subprocess
import sys
import os

# Get the path to the Python script or executable (sys.argv[0])
script_path = sys.argv[0]

# Get the directory containing the script or executable
script_dir = os.path.dirname(os.path.abspath(script_path))

# Move one directory up to get the path before 'dist'
parent_dir = os.path.dirname(script_dir)

# Path to the BAT file (assuming it's in the root project directory)
bat_file = os.path.join(parent_dir, 'rbhus_clone.bat')

# Ensure the BAT file exists before running it
if not os.path.isfile(bat_file):
    print(f"Error: The specified BAT file does not exist: {bat_file}")
    sys.exit(1)

# Run the BAT file using subprocess
subprocess.run([bat_file], shell=True)
