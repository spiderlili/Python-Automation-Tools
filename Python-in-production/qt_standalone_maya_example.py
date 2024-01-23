# Boilerplate setup
from PySide6 import QtWidgets
from shiboken2 import wrapInstance

def maya_main_window():
    """
    Return the Maya main window widget as a Python object: gets the main Maya window, parent the standalone window to Maya 
    """
    main_window_ptr = omui.MQTUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

# Window
class StandaloneWindow(QtWidgets.QWidget):
    wnd_instance = None

    def __init__(self):
        super(StandaloneWindow, self).__init__(parent=None)
        self.setWindowTitle("Standalone App")
        self.setMinimumSize(400, 300)
        self.close_btn = QtWidgets.QPushButton("Close", self)
        self.close_btn.clicked.connect(self.close)

    # Toggles the window visibility: allows the script to be run from a shelf button in production
    @classmethod 
    def display(cls):
        if not cls.wnd_instance:
            cls.wnd_instance = StandaloneWindow()

        if cls.wnd_instance.isHidden():
            cls.wnd_instance.show()
        else:
            cls.wnd_instance.raise_()
            cls.wnd_instance.activateWindow()

# Main Qt Application: delete the dialogue each time the code is executed. 
# Python environment is persistent between Maya sessions: PySide2 dialogues need to be explicitly deleted to pick up code changes
if __name__ == "__main__":
    try:
        test_dialog.close()
        test_dialog.deleteLater()

    except:
        pass

    test_dialog = StandaloneWindow()
    test_dialog.show()

    app = QtWidgets.QApplication(sys.argv)
    window = StandaloneWindow()
    window.show()

    # Enter Qt's main loop: nothing will happen until event handling is kicked off in Qt to handle all events that happen 
    app.exec_() 