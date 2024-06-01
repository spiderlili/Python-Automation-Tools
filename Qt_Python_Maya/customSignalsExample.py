import maya.cmds as cmds
import maya.OpenMayaUI as omui
import sys

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

        # Make the dialog a tool window for MacOS to prevent it from falling behind Maya main window
        if sys.platform == "darwin":
            self.setWindowFlag(QtCore.Qt.Tool, True) 

        self.create_widgets()
        self.create_layout()
        self.create_connections()
        
    def create_widgets(self):
        self.name_le = QtWidgets.QLineEdit()
        self.ok_btn = QtWidgets.QPushButton("OK")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")

    def create_layout(self):
        form_layout = QtWidgets.QFormLayout()
        form_layout.setSpacing(6)
        form_layout.addRow("Name: ", self.wdg_a)

        # Button layout parented to a window instead of a form
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.addStretch()
        btn_layout.addWidget(self.ok_btn)
        btn_layout.addWidget(self.cancel_btn)

        # Arrange widgets vertically in a main top level layout, use it to contain a child form layout at the top & a button layout at the bottom
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(btn_layout)

    def create_connections(self):
        pass

    def on_enter_pressed(self, texet):
        print(f"Enter key pressed: {text}")

    def on_return_pressed(self, text):
        print(f"Return key pressed: {text}")

if __name__ == "__main__":
    # Delete existing window instance before a new one is shown
    try:
        win.close()
        win.deleteLater()
    except:
        pass

    # Show window
    win = MainToolWindow()
    win.show()