import os

import maya.cmds as cmds
import maya.api.OpenMaya as om # for handling errors & displaying them to Maya's main UI

def version_saved(file_type = "mayaAscii"):
    scene_path = cmds.file(q=True, sceneName=True)
    if not scene_path:
        om.MGlobal.displayError("Unsaved File!")
        return
    
    if file_type == "mayaAscii":
        extension = "ma"
    elif file_type == "mayaBinary":
        extension = "mb"
    else:
        om.MGlobal.displayError("Unsupport file type")
        return

# When finished: will return the file path for the next version to be saved with the updated version number (scene.0001.ma)
def next_version_path(scene_path, extension):
    dir_path = os.path.dirname(scene_path)
    file_name = os.path.basename(scene_path)
    # The base file cannot contain any dots in the name as dot is used as a separator!
    base_file_name = file_name.split(".")[0]
    current_versions = get_current_versions(dir_path, base_file_name)
    
    if current_versions:
        next_version = current_versions[-1] + 1 # Get the last version in the list (as they're sorted in ascending order) + 1
    else:
        next_version = 1

    next_version_str = "{0}".format(next_version).zfill(4)
    return "{0}/{1}.{2}.{3}".format(dir_path, base_file_name, next_version_str, extension)

# Get a list of all the current versions that already exist for the given scene name
def get_current_versions(dir_path, base_file_name):
    current_versions = []
    file_names = os.listdir(dir_path)
    for file_name in file_names:
        # Verify that the base file name matches the file name it’s being compared to
        if file_name.startswith("{0}".format(base_file_name)):
            split_file_name = file_name.split(".")
            if len(split_file_name) == 3:
                version_num_str = split_file_name[1]
                try:
                    version_num_int = int(version_num_str)
                except:
                    continue
                current_versions.append(version_num_int)
    current_versions.sort()
    return current_versions

if __name__ == "__main__":
    file_path = "/Users/jing.tan/Documents/GitHub/Python-Automation-Tools/Python-Maya-Pipeline/MayaTestScenes/test_scene_vc.ma"
    next_ver_path = next_version_path(file_path, "ma")
    print(next_ver_path)