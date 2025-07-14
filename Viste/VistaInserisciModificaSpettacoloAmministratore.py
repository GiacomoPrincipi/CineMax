import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaInserisciModificaSpettacoloAmministratore import Ui_VistaInserisciModificaSpettacoloAmministratore

class VistaInserisciModificaSpettacoloAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaInserisciModificaSpettacoloAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaInserisciModificaSpettacoloAmministratore()
    widget.show()
    sys.exit(app.exec())
