import maya.cmds as cmds
import maya.OpenMayaUI as omui

try:
    # Qt5(<= Maya 2025)
    from PySide2 import QtCore
    from PySide2 import QtWidgets 
    from shiboken2 import wrapInstance
except:
    # Qt6 (> Maya 2025)
    from PySide6 import QtCore
    from PySide6 import QtWidgets 
    from shiboken6 import wrapInstance

# convert the C++ pointer so that it’s a valid python object
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class MainToolWindow(QtWidgets.QDialog):
    # Reparent to Maya's main window to always display on top even when not on focus
    def __init__(self, parent=maya_main_window()): 
        super().__init__(parent)
        self.setWindowTitle("Windows Dialogs")
        self.setMinimumSize(400, 300)

if __name__ == "__main__":
    win = MainToolWindow()
    win.show()