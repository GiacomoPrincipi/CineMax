import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaAcquistoProdottoCliente import Ui_VistaAcquistoProdottoCliente

class VistaAcquistoProdottoCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaAcquistoProdottoCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaAcquistoProdottoCliente()
    widget.show()
    sys.exit(app.exec())
