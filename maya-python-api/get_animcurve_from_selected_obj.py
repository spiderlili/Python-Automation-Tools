import traceback 
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma

def get_current_time():
    return oma.MAnimControl.currentTime()

def add_key(obj, attr_name):
    current_time = get_current_time()
    anim_curve_fn = get_anim_curve(obj, attr_name)
    if not anim_curve_fn:
        anim_curve_fn = create_anim_curve(obj, attr_name)
        if not anim_curve_fn:
            return None
    # Verify that a key doesn’t already exist at the current time 
    index = anim_curve_fn.find(current_time)
    if index is None:
        return anim_curve_fn.insertKey(current_time)
    return None

def remove_key(obj, attr_name):
    anim_curve_fn = get_anim_curve(obj, attr_name)
    if not anim_curve_fn:
        return
    # Verify that a key already exists at the current time 
    index = anim_curve_fn.find(get_current_time())
    if not index is None:
        anim_curve_fn.remove(index)

# Helper method that creates an AnimCurve node & connect it to the selected object (if one does not exist)
def create_anim_curve(obj, attr_name):
    plug = find_plug(obj, attr_name)
    if not plug or plug.isConnected:
        return None
    
    anim_curve_fn = oma.MFnAnimCurve()
    try:
        anim_curve_fn.create(plug, oma.MFnAnimCurve.kAnimCurveUnknown)
    except:
        traceback.print_exc() # Print out the error message that raised the exception
        return None
    return anim_curve_fn

# Get the animCurve node for a specific attribute on the selected node
def get_anim_curve(obj, attr_name):
    plug = find_plug(obj, attr_name)
    if not plug:
        return None
    
    source_plug = plug.source() # if an AnimCurve node is connected: its output attribute will be the source plug
    anim_curve_fn = oma.MFnAnimCurve()

    if anim_curve_fn.hasObj(source_plug.node()):
        anim_curve_fn.setObject(source_plug.node())
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
        obj = selection.getDependNode(0)

        if add_key(obj, "translateX") is None:
            remove_key(obj, "translateX")

        """
        # Add anim curve if none exists
        anim_curve_fn = get_anim_curve(obj, "translateX")
        
        if not anim_curve_fn:
            anim_curve_fn = create_anim_curve(obj, "translateX")
        
        if anim_curve_fn:
            print("Anim Curve Function Name:" + anim_curve_fn.name())
        else:
            print("An AnimCurve node is not connected!")
        """
    else:
        om.MGlobal.displayError("An object is not selected!")

