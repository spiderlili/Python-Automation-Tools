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
        
        # Adding widgets example
        #QtWidgets.QPushButton("hello", self)
        self.button_a = QtWidgets.QPushButton("Button A") # Parent button to window for it to 
        self.button_b = QtWidgets.QPushButton("Button B") 
        self.button_c = QtWidgets.QPushButton("Button C") 
        self.button_d = QtWidgets.QPushButton("Button D") 
        self.button_1 = QtWidgets.QPushButton("Button 1") 
        self.button_2 = QtWidgets.QPushButton("Button 2") 
        self.button_3 = QtWidgets.QPushButton("Button 3") 
        self.button_4 = QtWidgets.QPushButton("Button 4") 
        self.wdg_a = QtWidgets.QLineEdit()
        self.wdg_b = QtWidgets.QLineEdit()
        self.wdg_c = QtWidgets.QCheckBox("Enabled")
        self.name_le = QtWidgets.QLineEdit()
        self.address_le = QtWidgets.QLineEdit()
        self.rb1 = QtWidgets.QRadioButton("RB 1")
        self.rb1.setChecked(True)
        self.rb2 = QtWidgets.QRadioButton("RB 2")
        self.rb3 = QtWidgets.QRadioButton("RB 3")
        self.cb1 = QtWidgets.QCheckBox("Option 1")
        self.cb2 = QtWidgets.QCheckBox("Option 2")
        self.cb3 = QtWidgets.QCheckBox("Option 3")
        self.cb4 = QtWidgets.QCheckBox("Option 4")

        # self.button_b.move(0, 30)

        '''
        # Create layouts
        main_layout = QtWidgets.QVBoxLayout() 
        # main_layout = QtWidgets.QHBoxLayout() 
        self.setLayout(main_layout) # Set windows as parent of layout
        main_layout.setSpacing(2) # fix the default spacing between widgets
        main_layout.setContentsMargins(2, 10, 2, 10)
        main_layout.addWidget(self.button_a)
        main_layout.addWidget(self.button_b)
        main_layout.addWidget(self.button_c)
        main_layout.addWidget(self.button_d)
        main_layout.addStretch() # Push the buttons to the top of the UI
        
        # Grid layout
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setContentsMargins(2, 10, 2, 10)
        self.setLayout(grid_layout)
        grid_layout.addWidget(self.button_1, 0, 0)
        grid_layout.addWidget(self.button_2, 0, 1)
        grid_layout.addWidget(self.button_3, 1, 0)
        grid_layout.addWidget(self.button_4, 1, 1)
        '''
        # Radio buttons layout
        rb_layout = QtWidgets.QHBoxLayout()
        rb_layout.setContentsMargins(0, 0, 0, 0) # Starting point
        rb_layout.addWidget(self.rb1)
        rb_layout.addWidget(self.rb2)
        rb_layout.addWidget(self.rb3)

        # Form layout
        form_layout = QtWidgets.QFormLayout()
        self.setLayout(form_layout)
        form_layout.addRow("Name: ", self.wdg_a)
        form_layout.addRow("Address: ", self.wdg_b)
        form_layout.addRow("", self.wdg_c)
        form_layout.addRow("", rb_layout)

if __name__ == "__main__":
    win = MainToolWindow()
    win.show()