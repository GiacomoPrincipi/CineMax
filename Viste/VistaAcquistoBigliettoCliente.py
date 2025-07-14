import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaAcquistoBigliettoCliente import Ui_VistaAcquistoBigliettoCliente

class VistaAcquistoBigliettoCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaAcquistoBigliettoCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaAcquistoBigliettoCliente()
    widget.show()
    sys.exit(app.exec())
