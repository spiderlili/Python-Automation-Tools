import os

import maya.cmds as cmds
import maya.api.OpenMaya as om # for handling errors & displaying them to Maya's main UI

# When finished: will return the file path for the next version to be saved with the updated version number (scene.0001.ma)
def next_version_path(scene_path, extension):
    dir_path = os.path.dirname(scene_path)
    file_name = os.path.basename(scene_path)
    # The base file cannot contain any dots in the name as dot is used as a separator!
    base_file_name = file.name.split(".")[0]
    current_versions = get_current_versions(dir_path, base_file_name)
    print(current_versions)

# Get a list of all the current versions that already exist for the given scene name
def get_current_versions(dir_path, base_file_name):
    current_versions = []
    file_names = os.listdir(dir_path)
    for file_name in file_names:
        split_file_name = file_name.split(".")
        if len(split_file_name) == 3:
            version_num_str = split_file_name[1]
            try:
                version_num_int = int(version_num_str)
            except:
                continue
            current_versions.append(version_num_int)
    return current_versions