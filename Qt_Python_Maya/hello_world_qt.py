# > Maya 2025: use PySide6
import maya.cmds as cmds

try:
    from PySide2 import QtWidgets # Qt5(<= Maya 2025)
except:
    from PySide6 import QtWidgets # Qt6 (> Maya 2025)

class HelloQtWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hello Qt")


if __name__ == "__main__":
    window = HelloQtWindow()
    window.show()