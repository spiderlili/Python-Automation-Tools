import os
import subprocess
import sys

# PySide6 with Qt6 supports version of python >=3.7 and <3.12
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets


class ApplicationButtonWdg(QtWidgets.QWidget):

    BUTTON_SIZE = QtCore.QSize(48, 48)

    clicked = QtCore.Signal(str)

    def __init__(self, name, application_path, parent=None):
        super(ApplicationButtonWdg, self).__init__(parent)

        self.application_path = application_path

        self.button = self.create_button()

        self.label = QtWidgets.QLabel("<b>{0}</b>".format(name))

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setAlignment(QtCore.Qt.AlignCenter)
        button_layout.addWidget(self.button)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.label)
        main_layout.addStretch()

    def create_button(self):
        button = QtWidgets.QToolButton()
        button.setFixedSize(ApplicationButtonWdg.BUTTON_SIZE)

        file_info = QtCore.QFileInfo(self.application_path)

        file_icon_provider = QtWidgets.QFileIconProvider()
        icon = file_icon_provider.icon(file_info)

        icon = self.get_scaled_icon(icon)
        button.setIcon(icon)
        button.setIconSize(ApplicationButtonWdg.BUTTON_SIZE)

        button.clicked.connect(self.on_click)

        return button

    def get_scaled_icon(self, icon):
        pixmap = icon.pixmap(ApplicationButtonWdg.BUTTON_SIZE)
        return QtGui.QIcon(pixmap)

    def on_click(self):
        self.clicked.emit(self.application_path)


class MayaLauncher(QtWidgets.QWidget):

    # TODO: Add switch situations for Windows, Mac OS / Linux
    MAYA_2022_PATH = "C:/Program Files/Autodesk/Maya2022/bin/maya.exe"
    MAYA_2023_PATH = "C:/Program Files/Autodesk/Maya2023/bin/maya.exe"

    EMPTY_SCENE = "<Empty Scene>"

    def __init__(self):
        super(MayaLauncher, self).__init__(parent=None)

        self.setWindowTitle("Maya Launcher")
        self.setMinimumWidth(360)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.env_select_cmb = QtWidgets.QComboBox()
        self.env_select_cmb.addItems(["Stable", "Dev"])

        self.maya_2022_btn = ApplicationButtonWdg("Maya 2022", MayaLauncher.MAYA_2022_PATH)
        self.maya_2023_btn = ApplicationButtonWdg("Maya 2023", MayaLauncher.MAYA_2023_PATH)

        self.scene_select_cmb = QtWidgets.QComboBox()
        self.scene_select_cmb.addItems([MayaLauncher.EMPTY_SCENE, "E:/maya_project/shapes.ma"])
        
    def create_layout(self):
        env_select_layout = QtWidgets.QHBoxLayout()
        env_select_layout.addStretch()
        env_select_layout.addWidget(QtWidgets.QLabel("Environment:"))
        env_select_layout.addWidget(self.env_select_cmb)

        maya_btn_layout = QtWidgets.QHBoxLayout()
        maya_btn_layout.addWidget(self.maya_2022_btn)
        maya_btn_layout.addWidget(self.maya_2023_btn)
        maya_btn_layout.addStretch()

        scene_select_layout = QtWidgets.QVBoxLayout()
        scene_select_layout.addWidget(QtWidgets.QLabel("Scene Selection:"))
        scene_select_layout.addWidget(self.scene_select_cmb)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(env_select_layout)
        main_layout.addLayout(maya_btn_layout)
        main_layout.addLayout(scene_select_layout)
        main_layout.addStretch()

    def create_connections(self):
        self.maya_2022_btn.clicked.connect(self.open_application)
        self.maya_2023_btn.clicked.connect(self.open_application)

    # Application path is stored in the button instance & passed as part of a signal slot connection
    def open_application(self, application_path):
        print("Opening Application: {0}".format(application_path))

        selected_env_path = "" # Base on the user's environment selection (stable / development)
        maya_args = []

        selected_env = self.env_select_cmb.currentText()
        if selected_env == "Stable":
            selected_env_path = "D:/PythonStable"
        elif selected_env == "Dev":
            selected_env_path = "D:/PythonDev"

        # Load selected scene when Maya loads: either the empty scene or file path
        scene_path = self.scene_select_cmb.currentText()
        if scene_path != MayaLauncher.EMPTY_SCENE:
            maya_args = ["-file", scene_path]

        self.open_application_python(application_path, selected_env_path, maya_args)
        # self.open_application_qt(application_path, selected_env_path, maya_args)

    def open_application_python(self, application_path, selected_env_path, maya_args):
        maya_env = os.environ.copy()
        maya_env["PYTHONPATH"] = selected_env_path

        # When using Popen & passing in the args for the application: the executable path needs to be the 1st arg in that list
        maya_args.insert(0, application_path)
        subprocess.Popen(maya_args, env=maya_env)

    # Qt-based alternative to the subprocess module - leverage the Qt process class. 
    # advantages in Qt applications through the use of signals & slots despite similarity in setup & functionality to subprocess
    def open_application_qt(self, application_path, selected_env_path, maya_args):
        process_environment = QtCore.QProcessEnvironment.systemEnvironment()
        process_environment.insert("PYTHONPATH", selected_env_path)
        process = QtCore.QProcess(self)
        # Provide the environment, application path, Maya-specific args
        process.setProcessEnvironment(process_environment)
        process.setProgram(application_path)
        process.setArguments(maya_args)
        process.startDetached() # Make sure the process does not block script execution

if __name__ == "__main__":
    # Create the main Qt application
    app = QtWidgets.QApplication(sys.argv)

    window = MayaLauncher()
    window.show()

    # Enter Qt main loop (start event handling)
    app.exec_()

