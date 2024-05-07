import os
import maya.cmds as cmds

env_var_name = "REPO_PATH"
root_path = os.environ[env_var_name]

# for each file node in the scene: get its file path, compare the root path with the repo path, update the file node path if required (if that file path is part of the repo)
file_nodes = cmds.ls(type="file")
for file_node in file_nodes:
    attr = "{0}.fileTextureName".format(file_node)
    file_path = cmds.getAttr(attr)
    print("Original File Path: {0}".format(file_path))

    # Make sure it only contains forward slashes when updating the path: on Windows the file paths may be using backslahes as separators but backslahes are not supported on MacOS / Linux
    file_path = file_path.replace("\\", "/") 
    if file_path.startswith(root_path):
        file_path = file_path.replace(root_path, "${0}".format(env_var_name), 1) # only replace it once at the start of the path
        print("Updated File Path: {0}".format(file_path))

        cmds.setAttr(attr, file_path, type="string")