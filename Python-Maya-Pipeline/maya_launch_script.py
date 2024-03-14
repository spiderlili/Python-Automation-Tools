import os
import subprocess

MAYA_PATH = "/Applications/Autodesk/maya2024/Maya.app" # Mac

# Launch Maya from the default environment
# May need to give executable permission for this script to run
maya_args = [MAYA_PATH]
# subprocess.call is blocking - it waits for the process to exist (in this case Maya), before continuing to run the script.
# subprocess.call(maya_args) 
# subprocess.Popen is non-blocking - needs to be run through terminal, otherwise it ends immediately after launching Maya which also ends the Maya process
subprocess.Popen(maya_args)