import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaRecensioniCliente import Ui_VistaVisualizzaRecensioniCliente

class VistaVisualizzaRecensioniCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaRecensioniCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaRecensioniCliente()
    widget.show()
    sys.exit(app.exec())
