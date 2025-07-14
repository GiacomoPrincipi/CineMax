import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaHomeCliente import Ui_VistaHomeCliente

class VistaHomeCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaHomeCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaHomeCliente()
    widget.show()
    sys.exit(app.exec())
