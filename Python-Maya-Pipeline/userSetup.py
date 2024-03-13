import inspect
import os
import sys
import maya.cmds as cmds

user_setup_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print("Reading userSetup.py from {0}".format(user_setup_path)) # Check output window

# Add new paths at the start of the Maya plugin path & script path environment variables, verify via plug-in manager (must be a valid path with >= 1 plugin)
new_plugin_path = "D:/TestPlugins"
new_script_path = "D:/TestScripts"
os.environ["MAYA_PLUG_IN_PATH"] = new_plugin_path + os.pathsep + os.environ["MAYA_PLUG_IN_PATH"] 
os.environ["MAYA_SCRIPT_PATH"] = new_script_path + os.pathsep + os.environ["MAYA_SCRIPT_PATH"] 

# problem with the scripts directory: 
# currently any Python modules added to this directory will not be recognised, because this directory has not been added to the Python path. 
# not possible to edit the Python path environment variable in the userSetup file - add a new path to sys.path instead
sys.path.insert(0, new_script_path)

# Open a command port for both MEL & Python commands to allow external applications to communicate with Maya
# Verify using commandPort -q -listPorts
cmds.commandPort(name=":20240", sourceType="mel")
cmds.commandPort(name=":20241", sourceType="python")