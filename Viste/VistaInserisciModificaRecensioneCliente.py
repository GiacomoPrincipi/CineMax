import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaInserisciModificaRecensioneCliente import Ui_VistaInserisciModificaRecensioneCliente

class VistaInserisciModificaRecensioneCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaInserisciModificaRecensioneCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaInserisciModificaRecensioneCliente()
    widget.show()
    sys.exit(app.exec())
