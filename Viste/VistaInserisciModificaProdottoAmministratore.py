import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaInserisciModificaProdottoAmministratore import Ui_VistaInserisciModificaProdottoAmministratore

class VistaInserisciModificaProdottoAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaInserisciModificaProdottoAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaInserisciModificaProdottoAmministratore()
    widget.show()
    sys.exit(app.exec())
