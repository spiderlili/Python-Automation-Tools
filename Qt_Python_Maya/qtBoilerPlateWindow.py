try:
    # Qt5(<= Maya 2025)
    from PySide2 import QtCore
    from PySide2 import QtGui
    from PySide2 import QtWidgets 
    from shiboken2 import wrapInstance
except:
    # Qt6 (> Maya 2025)
    from PySide6 import QtCore
    from PySide6 import QtGui
    from PySide6 import QtWidgets # Qt6 (> Maya 2025)
    from shiboken6 import wrapInstance

import sys
import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class OpenImportDialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(OpenImportDialog, self).__init__(parent)
        self.setWindowTitle("Window Title")
        self.setMinimumSize(400, 100)

        # On MacOS make the window a tool to keep it on top of Maya
        if sys.platform == "darwin":
            self.setWindowFlag(QtCore.Qt.Tool, True)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        pass

    def create_layout(self):
        pass

    def create_connections(self):
        pass

if __name__ == "__main__":
    try:
        open_import_dialog.close()
        open_import_dialog.deleteLate()
    except:
        pass

    open_import_dialog = OpenImportDialog()
    open_import_dialog.show()