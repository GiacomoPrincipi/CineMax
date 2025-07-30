from PySide6.QtWidgets import QWidget
from ui_VistaHomeCliente import Ui_VistaHomeCliente

class VistaHomeCliente(QWidget):
    def __init__(self, statoLogin, goVistaHome, goVistaVisualizzaProfiloPersonaleCliente, goVistaVisualizzaSpettacoliCliente, goVistaVisualizzaProdottiCliente, goVistaVisualizzaPagamentiCliente, goVistaVisualizzaRecensioniCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaHomeCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaHome = goVistaHome

        self.ui.labelLogoutButton.clicked.connect(self.logout)
        self.ui.labelProfiloButton.clicked.connect(goVistaVisualizzaProfiloPersonaleCliente)
        self.ui.pushButtonSpettacoli.clicked.connect(goVistaVisualizzaSpettacoliCliente)
        self.ui.pushButtonProdotti.clicked.connect(goVistaVisualizzaProdottiCliente)
        self.ui.pushButtonPagamenti.clicked.connect(goVistaVisualizzaPagamentiCliente)
        self.ui.pushButtonRecensioni.clicked.connect(goVistaVisualizzaRecensioniCliente)

    def showEvent(self, event):
        super().showEvent(event)

    def logout(self):
        self.statoLogin.logoutCliente()

        self.goVistaHome()
