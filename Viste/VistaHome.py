import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaHome import Ui_VistaHome

class VistaHome(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaHome()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaHome()
    widget.show()
    sys.exit(app.exec())
