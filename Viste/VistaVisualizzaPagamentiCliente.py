import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaPagamentiCliente import Ui_VistaVisualizzaPagamentiCliente

class VistaVisualizzaPagamentiCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaPagamentiCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaPagamentiCliente()
    widget.show()
    sys.exit(app.exec())
