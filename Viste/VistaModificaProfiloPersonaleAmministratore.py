import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaModificaProfiloPersonaleAmministratore import Ui_VistaModificaProfiloPersonaleAmministratore

class VistaModificaProfiloPersonaleAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaModificaProfiloPersonaleAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaModificaProfiloPersonaleAmministratore()
    widget.show()
    sys.exit(app.exec())
