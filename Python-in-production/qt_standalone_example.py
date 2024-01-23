# Boilerplate setup
import sys
from PySide6 import QtWidgets

# Window
class StandaloneWindow(QtWidgets.QWidget):
    def __init__(self):
        super(StandaloneWindow, self).__init__(parent=None)
        self.setWindowTitle("Standalone App")
        self.setMinimumSize(400, 300)
        self.close_btn = QtWidgets.QPushButton("Close", self)
        self.close_btn.clicked.connect(self.close)

# Main Qt Application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = StandaloneWindow()
    window.show()

    # Enter Qt's main loop: nothing will happen until event handling is kicked off in Qt to handle all events that happen 
    app.exec_() 