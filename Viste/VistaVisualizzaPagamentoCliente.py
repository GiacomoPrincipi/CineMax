import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaPagamentoCliente import Ui_VistaVisualizzaPagamentoCliente

class VistaVisualizzaPagamentoCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaPagamentoCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaPagamentoCliente()
    widget.show()
    sys.exit(app.exec())
