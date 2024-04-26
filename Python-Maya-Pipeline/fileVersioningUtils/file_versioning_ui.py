# Qt5(<= Maya 2025), Qt6 (> Maya 2025)
try:
    from PySide2 import QtCore
    from PySide2 import QtWidgets 
    from shiboken2 import wrapInstance
except:
    from PySide6 import QtCore
    from PySide6 import QtWidgets 
    from shiboken6 import wrapInstance

import maya.cmds as cmds
import maya.OpenMayaUI as omui

# file_utils.py need to be in a directory that’s on Maya’s Python path (.e.g. Maya scripts directory) so it’s recognised as a module & can be imported by the UI script!
import file_utils

class FileVersioningUi(QtWidgets.QDialog):

    WINDOW_TITLE = "File Versioning"
    @classmethod
    def maya_main_window(cls):
        main_window_ptr = omui.MQtUtil.mainWindow()
        if sys.version_info.major >= 3:
            return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
        else:
            return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

    def __init__(self):
        super(FileVersioningUi, self).__init__(self.maya_main_window())

        self.setWindowTitle(self.WINDOW_TITLE)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.maya_ascii_rb = QtWidgets.QRadioButton("mayaAscii")
        self.maya_ascii_rb.setChecked(True)

        self.maya_binary_rb = QtWidgets.QRadioButton("mayaBinary")

        self.save_btn =  QtWidgets.QPushButton("Versioned Save")

    def create_layout(self):
        type_layout = QtWidgets.QHBoxLayout()
        type_layout.addWidget(self.maya_ascii_rb)
        type_layout.addWidget(self.maya_binary_rb)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(type_layout)
        main_layout.addStretch()
        main_layout.addWidget(self.save_btn)

    def create_connections(self):
        self.save_btn.clicked.connect(self.do_save)

    def do_save(self):
        if self.maya_binary_rb.isChecked():
            file_type = "mayaBinary"
        else:
            file_type = "mayaAscii"

        file_utils.versioned_saved(file_type)


if __name__ == "__main__":

    try:
        versioning_ui.close() # pylint: disable=E0601
        versioning_ui.deleteLater()
    except:
        pass

    versioning_ui = FileVersioningUi()
    versioning_ui.show()
