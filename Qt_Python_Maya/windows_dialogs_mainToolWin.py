# > Maya 2025: use PySide6
import maya.cmds as cmds

try:
    # Qt5(<= Maya 2025)
    from PySide2 import QtCore
    from PySide2 import QtWidgets 
except:
    # Qt6 (> Maya 2025)
    from PySide6 import QtCore
    from PySide6 import QtWidgets 

class MainToolWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)