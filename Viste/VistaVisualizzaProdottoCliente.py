import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaProdottoCliente import Ui_VistaVisualizzaProdottoCliente

class VistaVisualizzaProdottoCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProdottoCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaProdottoCliente()
    widget.show()
    sys.exit(app.exec())
