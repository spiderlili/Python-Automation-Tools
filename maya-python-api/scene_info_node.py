import getpass

from PySide2 import QtCore
from PySide2 import QtGui

import maya.api.OpenMaya as om
import maya.api.OpenMayaRender as omr  # pylint: disable=E0001,E0611
import maya.api.OpenMayaUI as omui

import maya.cmds as cmds


def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass


class SceneInfoNode(omui.MPxLocatorNode):

    TYPE_NAME = "SceneInfoNode"
    TYPE_ID = om.MTypeId(0x0007F7F9)
    DRAW_CLASSIFICATION = "drawdb/geometry/sceneinfo"
    DRAW_REGISTRANT_ID = "SceneInfoNode"


    def __init__(self):
        super(SceneInfoNode, self).__init__()

    @classmethod
    def creator(cls):
        return SceneInfoNode()

    @classmethod
    def initialize(cls):
        pass


class SceneInfoDrawOverride(omr.MPxDrawOverride):

    NAME = "SceneInfoDrawOverride"


    def __init__(self, obj):
        super(SceneInfoDrawOverride, self).__init__(obj, None)

    def prepareForDraw(self, obj_path, camera_path, frame_context, old_data):
        self.scene_name = cmds.file(q=True, sn=True, shn=True)
        if not self.scene_name:
            self.scene_name = "Untitled"

        self.user_name = getpass.getuser()
        self.current_frame = int(cmds.currentTime(q=True))

    def supportedDrawAPIs(self):
        return (omr.MRenderer.kAllDevices)

    def hasUIDrawables(self):
        return True

    def addUIDrawables(self, obj_path, draw_manager, frame_context, data):
        draw_manager.beginDrawable()

        draw_manager.text2d(om.MPoint(80, 100), "Scene Name: {0}".format(self.scene_name))
        draw_manager.text2d(om.MPoint(80, 80), "User Name: {0}".format(self.user_name))
        draw_manager.text2d(om.MPoint(80, 60), "Frame: {0}".format(self.current_frame))

        draw_manager.endDrawable()

    @classmethod
    def creator(cls, obj):
        return SceneInfoDrawOverride(obj)


def initializePlugin(plugin):

    vendor = "Chris Zurbrigg"
    version = "1.0.0"
    api_version = "Any"

    plugin_fn = om.MFnPlugin(plugin, vendor, version, api_version)

    try:
        plugin_fn.registerNode(SceneInfoNode.TYPE_NAME,              # name of the node
                               SceneInfoNode.TYPE_ID,                # unique id that identifies node
                               SceneInfoNode.creator,                # function/method that returns new instance of class
                               SceneInfoNode.initialize,             # function/method that will initialize all attributes of node
                               om.MPxNode.kLocatorNode,              # type of node to be registered
                               SceneInfoNode.DRAW_CLASSIFICATION)    # draw-specific classification string (VP2.0)
    except:
        om.MGlobal.displayError("Failed to register node: {0}".format(SceneInfoNode.TYPE_NAME))

    try:
        omr.MDrawRegistry.registerDrawOverrideCreator(SceneInfoNode.DRAW_CLASSIFICATION,     # draw-specific classification
                                                      SceneInfoNode.DRAW_REGISTRANT_ID,      # unique name to identify registration
                                                      SceneInfoDrawOverride.creator)         # function/method that returns new instance of class
    except:
        om.MGlobal.displayError("Failed to register draw override: {0}".format(SceneInfoDrawOverride.NAME))


def uninitializePlugin(plugin):

    plugin_fn = om.MFnPlugin(plugin)
    try:
        omr.MDrawRegistry.deregisterDrawOverrideCreator(SceneInfoNode.DRAW_CLASSIFICATION, SceneInfoNode.DRAW_REGISTRANT_ID)
    except:
        om.MGlobal.displayError("Failed to deregister draw override: {0}".format(SceneInfoDrawOverride.NAME))

    try:
        plugin_fn.deregisterNode(SceneInfoNode.TYPE_ID)
    except:
        om.MGlobal.displayError("Failed to unregister node: {0}".format(SceneInfoNode.TYPE_NAME))


if __name__ == "__main__":

    cmds.file(new=True, force=True)

    plugin_name = "scene_info_node.py"

    cmds.evalDeferred('if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(plugin_name))
    cmds.evalDeferred('if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(plugin_name))

    cmds.evalDeferred('cmds.createNode("SceneInfoNode")')

