import maya.cmds as cmds

cube_obj = "D:/MayaScenes/cube.ma"
cylinder_obj = "D:/MayaScenes/cylinder.ma"
sphere_obj = "D:/MayaScenes/sphere.ma"

# Reference a file (no namespace)
cmds.file(cube_obj, reference=True)

# Reference a file (with a namespace)
cmds.file(cylinder_obj, reference=True, namespace="cylinder")


# Deferred loading
ref_file_path = cmds.file(sphere_obj, reference=True, namespace="sphere", deferReference=True)

# Toggle the loading and unloading of a reference
ref_node = cmds.file(ref_file_path, q=True, referenceNode=True)
is_unloaded = cmds.file(q=True, referenceNode=ref_node, deferReference=True)
if is_unloaded:
    cmds.file(loadReference=ref_node)
else:
    cmds.file(unloadReference=ref_node)
