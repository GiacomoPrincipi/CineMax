import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaLoginCliente import Ui_VistaLoginCliente

class VistaLoginCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaLoginCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaLoginCliente()
    widget.show()
    sys.exit(app.exec())
