from PySide6.QtWidgets import QWidget
from ui_VistaHomeAmministratore import Ui_VistaHomeAmministratore

class VistaHomeAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHome, goVistaVisualizzaProfiloPersonaleAmministratore, goVistaVisualizzaSpettacoliAmministratore, goVistaVisualizzaProdottiAmministratore, goVistaVisualizzaRegistroCassaAmministratore, goVistaVisualizzaRecensioniAmministratore, goVistaVisualizzaAmministratoriAmministratore, goVistaVisualizzaClientiAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaHomeAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaHome = goVistaHome

        self.ui.labelLogoutButton.clicked.connect(self.logout)
        self.ui.labelProfiloButton.clicked.connect(goVistaVisualizzaProfiloPersonaleAmministratore)
        self.ui.pushButtonSpettacoli.clicked.connect(goVistaVisualizzaSpettacoliAmministratore)
        self.ui.pushButtonProdotti.clicked.connect(goVistaVisualizzaProdottiAmministratore)
        self.ui.pushButtonRegistroCassa.clicked.connect(goVistaVisualizzaRegistroCassaAmministratore)
        self.ui.pushButtonRecensioni.clicked.connect(goVistaVisualizzaRecensioniAmministratore)
        self.ui.pushButtonClienti.clicked.connect(goVistaVisualizzaClientiAmministratore)
        self.ui.pushButtonAmministratori.clicked.connect(goVistaVisualizzaAmministratoriAmministratore)
        #self.ui.labelBackupButton.clicked.connect(self.EffettuaBackup)

    def showEvent(self, event):
        super().showEvent(event)

        amministratore = self.statoLogin.amministratoreAutenticato

    def logout(self):
        self.statoLogin.logoutAmministratore()
        self.goVistaHome()

