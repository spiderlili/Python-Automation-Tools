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

        self.ok_btn = QtWidgets.QPushButton("OK")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
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

    def create_layout(self):
        # Radio buttons layout
        rb_layout = QtWidgets.QHBoxLayout()
        rb_layout.setContentsMargins(0, 0, 0, 0) # Starting point
        rb_layout.addWidget(self.rb1)
        rb_layout.addWidget(self.rb2)
        rb_layout.addWidget(self.rb3)

        # Grid layout of 4 checkboxes
        cb_layout = QtWidgets.QGridLayout()
        cb_layout.setContentsMargins(0, 0, 0, 0)
        cb_layout.addWidget(self.cb1, 0, 0)
        cb_layout.addWidget(self.cb2, 0, 1)
        cb_layout.addWidget(self.cb3, 1, 0)
        cb_layout.addWidget(self.cb3, 1, 1)

        # Form layout
        form_layout = QtWidgets.QFormLayout()
        form_layout.setSpacing(6)
        form_layout.addRow("Name: ", self.wdg_a)
        form_layout.addRow("Address: ", self.wdg_b)
        form_layout.addRow("", rb_layout)
        form_layout.addRow("", cb_layout)

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
        self.cancel_btn.clicked.connect(self.close) 
        self.name_le.editingFinished.connect(self.print_name) 
        # self.name_le.textChanged.connect(self.print_name) # Print each character input
        self.cb1.toggled.connect(self.print_checkbox)
        self.cb2.toggled.connect(self.print_checkbox)
        self.cb3.toggled.connect(self.print_checkbox)
        self.cb4.toggled.connect(self.print_checkbox)

    def print_name(self):
        name = self.name_le.text()
        print(name)

    # Use the sender method to determine which checkbox called this method
    def print_checkbox(self, checked):
        cb = self.sender()
        if cb == self.cb1:
            cb_name = "Option 1"
        elif cb == self.cb2:
            cb_name = "Option 2"
        elif cb == self.cb3:
            cb_name = "Option 3"
        elif cb == self.cb4:
            cb_name = "Option 4"
        else:
            return
        
        if checked:
            print(f"{cb_name} is checked")
        else:
            print(f"{cb_name} is not checked")


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