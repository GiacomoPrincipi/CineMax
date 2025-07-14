import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaRecensioneCliente import Ui_VistaVisualizzaRecensioneCliente

class VistaVisualizzaRecensioneCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaRecensioneCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaRecensioneCliente()
    widget.show()
    sys.exit(app.exec())
