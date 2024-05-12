import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma

# Get the animCurve node for a specific attribute on the selected node
def get_anim_curve(obj, attr_name):
    plug = find_plug(obj, attr_name)
    if not plug:
        return None
    
    source_plug = plug.source() # if an AnimCurve node is connected: its output attribute will be the source plug
    anim_curve_fn = oma.MFnAnimCurve()

    if anim_curve_fn.hasObj(source_plug.node()):
        anim_curve_fn,setObject(source_plug.node())
        return anim_curve_fn
    
    return None

# Helper method that will get the MPlug for the attribute name (if one exists)
def find_plug(obj, attr_name):
    depend_fn = om.MFnDependencyNode(obj) # Dependency Node function set
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
        anim_curve_fn = get_anim_curve(obj, "translateX")
        if anim_curve_fn:
            print("Anim Curve Function Name:" + anim_curve_fn.name())
    else:
        om.MGlobal.displayError("An object is not selected!")

