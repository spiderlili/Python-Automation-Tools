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
        self.setWindowTitle("Open/Import/Reference")
        self.setMinimumSize(400, 100)

        # On MacOS make the window a tool to keep it on top of Maya
        if sys.platform == "darwin":
            self.setWindowFlag(QtCore.Qt.Tool, True)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.filepath_le = QtWidgets.QLineEdit()

        # Temporarily hardcode a file path into the line edit to speed up development: can just click the Apply button during testing to verify whether or not the code changes are working
        testSceneTemp = "/Users/jing.tan/Documents/maya/projects/maya-2017-rigging-introduction/project_files/Maya_Files/Intro_To_Rigging_Maya_2017/scenes/m01-01_begin.ma"
        self.filepath_le.setText(testSceneTemp)

        self.select_file_path_btn = QtWidgets.QPushButton()
        # Show a Maya-provided folder icon that's commonly used for file open operations using Qt resource 
        self.select_file_path_btn.setIcon(QtGui.QIcon(":fileOpen.png"))

        self.open_rb = QtWidgets.QRadioButton("Open")
        self.open_rb.setChecked(True)

        self.import_rb = QtWidgets.QRadioButton("Import")
        self.reference_rb = QtWidgets.QRadioButton("Reference")        
        self.force_cb = QtWidgets.QCheckBox("Force")
        self.apply_btn = QtWidgets.QPushButton("Apply")
        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        file_path_layout = QtWidgets.QHBoxLayout()
        file_path_layout.addWidget(self.filepath_le)
        file_path_layout.addWidget(self.select_file_path_btn)

        radio_btn_layout = QtWidgets.QHBoxLayout()
        radio_btn_layout.addWidget(self.open_rb)
        radio_btn_layout.addWidget(self.import_rb)
        radio_btn_layout.addWidget(self.reference_rb)

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("File Path: ", file_path_layout)
        form_layout.addRow("", radio_btn_layout)
        form_layout.addRow("", self.force_cb)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.apply_btn)
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.select_file_path_btn.clicked.connect(self.show_file_select_dialog)
        self.open_rb.toggled.connect(self.set_force_cb_visible)
        self.apply_btn.clicked.connect(self.load_file)
        self.close_btn.clicked.connect(self.close)

    def show_file_select_dialog(self):
        print("TODO: show_file_select_dialog")
    
    def set_force_cb_visible(self, checked):
        self.force_cb.setVisible(checked) # If the radio button calling this is checked: the force checkbox will be visible

    def load_file(self):
        print("TODO: load_file on Apply button click")

if __name__ == "__main__":
    try:
        open_import_dialog.close()
        open_import_dialog.deleteLate()
    except:
        pass

    open_import_dialog = OpenImportDialog()
    open_import_dialog.show()