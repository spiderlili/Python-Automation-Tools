import os
import subprocess

MAYA_PATH = "/Applications/Autodesk/maya2024/Maya.app" # Mac
NEW_MAYA_APP_DIR_PATH = "/Users/jing.tan/Documents/maya_dev"
NEW_PYTHON_PATH = "/Users/jing.tan/Documents/maya_dev/python"

# Launch Maya from the default environment
# May need to give executable permission for this script to run
maya_args = [MAYA_PATH]
# subprocess.call is blocking - it waits for the process to exist (in this case Maya), before continuing to run the script.
# subprocess.call(maya_args) 
# subprocess.Popen is non-blocking - needs to be run through terminal, otherwise it ends immediately after launching Maya which also ends the Maya process
subprocess.Popen(maya_args)

# Modify the environment variables
env = os.environ.copy() # Get a dictionary copy of all environment variables to not modify the originals
env["MAYA_APP_DIR"] = NEW_MAYA_APP_DIR_PATH

# Not appending to the existing PYTHONPATH: clean PYTHONPATH with only 1 directory
# Any PYTHONPATHs required by Maya will be added automatically by Maya during initialisation
env["PYTHONPATH"] = NEW_PYTHON_PATH
subprocess.Popen(maya_args, env=env)
