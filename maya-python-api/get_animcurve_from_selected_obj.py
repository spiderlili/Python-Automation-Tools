import traceback 
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma

def get_current_time():
    return oma.MAnimControl.currentTime()

def set_value(anim_curve_fn, index, value):
    anim_curve_fn.setValue(index, value)

# Cannot change the order of a key: it would need to be removed from the curve & added back at the new time!
def set_time(anim_curve_fn, index, time):
    anim_curve_fn.setInput(index, time)

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

def display_anim_curve_info(anim_curve_fn):
    print("Number of keys: {0}".format(anim_curve_fn.numKeys))
    print("Is Static: {0}".format(anim_curve_fn.isStatic)) # Return the same value regardless of the evaluation time
    print("Pre Infinity Type: {0}".format(anim_curve_fn.preInfinityType)) # Return the same value regardless of the evaluation time
    print("Post Infinity Type: {0}".format(anim_curve_fn.postInfinityType)) # Return the same value regardless of the evaluation time
    print("----KEYS----")

    for index in range(anim_curve_fn.numKeys):
        display_key_info(anim_curve_fn, index)

def display_key_info(anim_curve_fn, index):
    time_current_frame = anim_curve_fn.input(index).value
    value = anim_curve_fn.value(index)
    isBreakdown = anim_curve_fn.isBreakdown(index)
    tangents_locked = anim_curve_fn.tangentsLocked(index)
    in_tangent_type = anim_curve_fn.inTangentType(index)
    in_tangent_values = anim_curve_fn.getTangentXY(index, True)
    out_tangent_type = anim_curve_fn.outTangentType(index)
    out_tangent_values = anim_curve_fn.getTangentXY(index, False)

    output = "[{0}] Time: {1}\tValue: {2}\t".format(index, time_current_frame, value)
    output += "Breakdown: {0}\n\tTangents Locked: {1}\t".format(isBreakdown, tangents_locked)
    output += "In Tangent: {0} {1}\t".format(in_tangent_type, in_tangent_values)
    output += "Out Tangent: {0} {1}".format(out_tangent_type, out_tangent_values)
    print(output)

if __name__ == "__main__":
    selection = om.MGlobal.getActiveSelectionList()
    if selection.length() > 0:
        obj = selection.getDependNode(0)

        anim_curve_fn = get_anim_curve(obj, "translateY")
        if anim_curve_fn:
            set_value(anim_curve_fn, 1, 3)
            set_time(anim_curve_fn, 0, get_current_time())
            display_anim_curve_info(anim_curve_fn)

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

