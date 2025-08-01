from PySide6.QtWidgets import QWidget
from Viste.ui_VistaHome import Ui_VistaHome

class VistaHome(QWidget):
    def __init__(self, statoLogin, goVistaLoginAmministratore, goVistaLoginCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaHome()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.ui.pushButtonAmministratore.clicked.connect(goVistaLoginAmministratore)
        self.ui.pushButtonCliente.clicked.connect(goVistaLoginCliente)
