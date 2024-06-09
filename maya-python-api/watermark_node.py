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


class WatermarkNode(omui.MPxLocatorNode):

    TYPE_NAME = "watermarknode"
    TYPE_ID = om.MTypeId(0x0007F7FA)
    DRAW_CLASSIFICATION = "drawdb/geometry/watermark"
    DRAW_REGISTRANT_ID = "WatermarkNode"


    def __init__(self):
        super(WatermarkNode, self).__init__()

    @classmethod
    def creator(cls):
        return WatermarkNode()

    @classmethod
    def initialize(cls):
        pass


class WatermarkDrawOverride(omr.MPxDrawOverride):

    NAME = "WatermarkDrawOverride"


    def __init__(self, obj):
        super(WatermarkDrawOverride, self).__init__(obj, None)

        self.image_path = "C:/Users/czurbrigg/Documents/maya/projects/default/sourceimages/watermark.png"
        self.texture = None

        self.update_texture_by_path()

    def __del__(self):
        self.release_texture()

    def release_texture(self):
        if self.texture:
            texture_manager = omr.MRenderer.getTextureManager()
            texture_manager.releaseTexture(self.texture)
            self.texture = None

    def update_texture_by_path(self):
        if self.image_path:
            texture_manager = omr.MRenderer.getTextureManager()
            self.texture = texture_manager.acquireTexture(self.image_path)
            if not self.texture:
                om.MGlobal.displayError("Unsupported image file: {0}".format(self.image_path))
                return
        else:
            self.texture = None

    def prepareForDraw(self, obj_path, camera_path, frame_context, old_data):
        self.vp_width = frame_context.getViewportDimensions()[2]

        if self.texture:
            texture_desc = self.texture.textureDescription()
            self.half_width = 0.5 * texture_desc.fWidth
            self.half_height = 0.5 * texture_desc.fHeight

    def supportedDrawAPIs(self):
        return (omr.MRenderer.kAllDevices)

    def hasUIDrawables(self):
        return True

    def addUIDrawables(self, obj_path, draw_manager, frame_context, data):
        draw_manager.beginDrawable()

        if self.texture:
            draw_manager.setTexture(self.texture)
            draw_manager.setTextureSampler(omr.MSamplerState.kMinMagMipLinear, omr.MSamplerState.kTexClamp)
            draw_manager.setTextureMask(omr.MBlendState.kRGBAChannels)
            draw_manager.setColor(om.MColor((1.0, 1.0, 1.0, 1.0)))

            rect_center = om.MPoint(self.vp_width - (50 + self.half_width), 50 + self.half_height)
            draw_manager.rect2d(rect_center, om.MVector(0.0, 1.0, 0.0), self.half_width, self.half_height, True)

        draw_manager.endDrawable()

    @classmethod
    def creator(cls, obj):
        return WatermarkDrawOverride(obj)


def initializePlugin(plugin):

    vendor = "Chris Zurbrigg"
    version = "1.0.0"
    api_version = "Any"

    plugin_fn = om.MFnPlugin(plugin, vendor, version, api_version)

    try:
        plugin_fn.registerNode(WatermarkNode.TYPE_NAME,              # name of the node
                               WatermarkNode.TYPE_ID,                # unique id that identifies node
                               WatermarkNode.creator,                # function/method that returns new instance of class
                               WatermarkNode.initialize,             # function/method that will initialize all attributes of node
                               om.MPxNode.kLocatorNode,              # type of node to be registered
                               WatermarkNode.DRAW_CLASSIFICATION)    # draw-specific classification string (VP2.0)
    except:
        om.MGlobal.displayError("Failed to register node: {0}".format(WatermarkNode.TYPE_NAME))

    try:
        omr.MDrawRegistry.registerDrawOverrideCreator(WatermarkNode.DRAW_CLASSIFICATION,     # draw-specific classification
                                                      WatermarkNode.DRAW_REGISTRANT_ID,      # unique name to identify registration
                                                      WatermarkDrawOverride.creator)         # function/method that returns new instance of class
    except:
        om.MGlobal.displayError("Failed to register draw override: {0}".format(WatermarkDrawOverride.NAME))


def uninitializePlugin(plugin):

    plugin_fn = om.MFnPlugin(plugin)
    try:
        omr.MDrawRegistry.deregisterDrawOverrideCreator(WatermarkNode.DRAW_CLASSIFICATION, WatermarkNode.DRAW_REGISTRANT_ID)
    except:
        om.MGlobal.displayError("Failed to deregister draw override: {0}".format(WatermarkDrawOverride.NAME))

    try:
        plugin_fn.deregisterNode(WatermarkNode.TYPE_ID)
    except:
        om.MGlobal.displayError("Failed to unregister node: {0}".format(WatermarkNode.TYPE_NAME))


if __name__ == "__main__":

    cmds.file(new=True, force=True)

    plugin_name = "watermark_node.py"

    cmds.evalDeferred('if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(plugin_name))
    cmds.evalDeferred('if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(plugin_name))

    cmds.evalDeferred('cmds.createNode("watermarknode")')




