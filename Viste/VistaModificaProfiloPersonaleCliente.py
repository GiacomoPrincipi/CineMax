import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaModificaProfiloPersonaleCliente import Ui_VistaModificaProfiloPersonaleCliente

class VistaModificaProfiloPersonaleCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaModificaProfiloPersonaleCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaModificaProfiloPersonaleCliente()
    widget.show()
    sys.exit(app.exec())
