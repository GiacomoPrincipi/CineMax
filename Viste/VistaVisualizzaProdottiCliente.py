import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaProdottiCliente import Ui_VistaVisualizzaProdottiCliente

class VistaVisualizzaProdottiCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProdottiCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaProdottiCliente()
    widget.show()
    sys.exit(app.exec())
