from PySide6.QtWidgets import QWidget
from ui_VistaLoginAmministratore import Ui_VistaLoginAmministratore
from Gestione.GestoreAmministratori import GestoreAmministratori
from Gestione.GestoreAutenticazione import GestoreAutenticazione

class VistaLoginAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHome, goVistaHomeAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaLoginAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaHomeAmministratore = goVistaHomeAmministratore

        self.ui.labelIndietroButton.clicked.connect(goVistaHome)
        self.ui.pushButtonAccedi.clicked.connect(self.accedi)
        self.ui.pushButtonRecuperoPassword.clicked.connect(self.recuperoCredenziali)

        self.contatore = 0

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.lineEditEmail.setText("")
        self.ui.lineEditPassword.setText("")

        self.ui.labelErroreEmail.setText("")
        self.ui.labelErrorePassword.setText("")

    def accedi(self):
        self.ui.labelErroreEmail.setText("")
        self.ui.labelErrorePassword.setText("")

        email = self.ui.lineEditEmail.text()
        password = self.ui.lineEditPassword.text()

        if email == "" or password == "":
            if email == "":
                self.ui.labelErroreEmail.setText("Inserisci l'email!")
            elif "@" not in email:
                self.ui.labelErroreEmail.setText("Email non Valida!")
            if password == "":
                self.ui.labelErrorePassword.setText("Inserisci la password!")
            return

        if "@" not in email:
            self.ui.labelErroreEmail.setText("Email non Valida!")
            return

        gestoreAmministratori = GestoreAmministratori()

        esito = GestoreAutenticazione.controlloEmail(gestoreAmministratori.listaAmministratori, email)
        if esito:
            amministratore = gestoreAmministratori.getAmministratore(email)
            self.statoLogin.loginAmministratore(amministratore)
            esito = GestoreAutenticazione.controlloPassword(amministratore, password)
            if esito:
                self.goVistaHomeAmministratore()
            else:
                self.ui.labelErrorePassword.setText("La password non è corretta!")
                self.contatore += 1

                if self.contatore == 5:
                    self.recuperoCredenziali()
                    self.contatore = 0
        else:
            self.ui.labelErroreEmail.setText("L'email non è stata trovata!")
            self.contatore = 0

    def recuperoCredenziali(self):
        self.ui.labelErroreEmail.setText("")
        self.ui.labelErrorePassword.setText("")
        self.ui.labelRecuperoPassword.setText("")

        email = self.ui.lineEditEmail.text()

        if email == "":
            self.ui.labelErroreEmail.setText("Inserisci l'email!")
            return
        elif "@" not in email:
            self.ui.labelErroreEmail.setText("Email non Valida!")
            return

        gestoreAmministratori = GestoreAmministratori()

        esito = GestoreAutenticazione.controlloEmail(gestoreAmministratori.listaAmministratori, email)
        if esito:
            amministratore = gestoreAmministratori.getAmministratore(email)
            GestoreAutenticazione.invioEmailRecuperoPassword(amministratore)
            gestoreAmministratori.salvaDatiAmministratori()
            self.ui.labelRecuperoPassword.setText("Ti abbiamo spedito una mail!")
        else: self.ui.labelErroreEmail.setText("L'email non è stata trovata!")
