import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma

# Get the animCurve node for a specific attribute on the selected node
def get_anim_curve(obj, attr_name):
    plug = find_plug(obj, attr_name)

# Helper method that will get the MPlug for the attribute name (if one exists)
def find_plug(obj, attr_name):
    depend_fn = om.MFnDependencyNode(obj)
    try:
        plug = depend_fn.findPlug(attr_name, False)
    except:
        om.MGlobal.displayWarning("Attribute not found: {0}.{1}".format(depend_fn.name(), attr_name))
        return None
    return plug

if __name__ == "__main__":
    selection = om.MGlobal.getActiveSelectionList()
    if selection.length() > 0:
        obj = selection.getDependMode(0)
    else:
        om.MGlobal.displayError("An object is not selected!")

