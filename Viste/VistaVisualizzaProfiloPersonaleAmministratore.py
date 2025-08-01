from PySide6.QtWidgets import QWidget
from Viste.ui_VistaVisualizzaProfiloPersonaleAmministratore import Ui_VistaVisualizzaProfiloPersonaleAmministratore
from Gestione.GestoreAmministratori import GestoreAmministratori

class VistaVisualizzaProfiloPersonaleAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHome, goVistaHomeAmministratore, goVistaModificaProfiloPersonaleAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProfiloPersonaleAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaHome = goVistaHome

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.pushButtonModifica.clicked.connect(goVistaModificaProfiloPersonaleAmministratore)
        self.ui.pushButtonElimina.clicked.connect(self.elimina)

    def showEvent(self, event):
        super().showEvent(event)

        amministratore = self.statoLogin.amministratoreAutenticato

        self.ui.labelNomeAmministratore.setText(amministratore.getNome())
        self.ui.labelCognomeAmministratore.setText(amministratore.getCognome())
        self.ui.labelDataNascitaAmministratore.setText(amministratore.getDataNascita().toString("dd/MM/yyyy"))
        self.ui.labelEmailAmministratore.setText(amministratore.getEmail())
        self.ui.labelTelefonoAmministratore.setText(amministratore.getTelefono())
        self.ui.labelPasswordAmministratore.setText(amministratore.getPassword())
        self.ui.labelMatricolaAmministratore.setText(amministratore.getMatricola())

    def elimina(self):

        amministratore = self.statoLogin.amministratoreAutenticato
        gestoreAmministratori = GestoreAmministratori()

        gestoreAmministratori.rimuoviAmministratore(amministratore)
        self.statoLogin.logoutAmministratore()

        self.goVistaHome()
