from PySide6.QtWidgets import QWidget
from Viste.ui_VistaLoginCliente import Ui_VistaLoginCliente
from Gestione.GestoreClienti import GestoreClienti
from Gestione.GestoreAutenticazione import GestoreAutenticazione

class VistaLoginCliente(QWidget):
    def __init__(self, statoLogin, goVistaHome, goVistaRegistrazioneCliente, goVistaHomeCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaLoginCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaHomeCliente = goVistaHomeCliente

        self.ui.labelIndietroButton.clicked.connect(goVistaHome)
        self.ui.pushButtonRegistrati.clicked.connect(goVistaRegistrazioneCliente)
        self.ui.pushButtonAccedi.clicked.connect(self.accedi)
        self.ui.pushButtonRecuperoPassword.clicked.connect(self.recuperoCredenziali)

        self.contatore = 0

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.lineEditEmail.setText("")
        self.ui.lineEditPassword.setText("")

        self.ui.labelErroreEmail.setText("")
        self.ui.labelErrorePassword.setText("")
        self.ui.labelRecuperoPassword.setText("")

    def accedi(self):
        self.ui.labelErroreEmail.setText("")
        self.ui.labelErrorePassword.setText("")

        email = self.ui.lineEditEmail.text().lower()
        password = self.ui.lineEditPassword.text()

        esito = False

        if email == "":
            self.ui.labelErroreEmail.setText("Inserisci l'email!")
            esito = True
        elif not GestoreAutenticazione.controlloStrutturaEmail(email):
            self.ui.labelErroreEmail.setText("Email non Valida!")
            esito = True
        if password == "":
            self.ui.labelErrorePassword.setText("Inserisci la password!")
            esito = True

        if esito: return

        gestoreClienti = GestoreClienti()

        esito = GestoreAutenticazione.controlloEmail(gestoreClienti.getListaClienti(), email)
        if esito:
            cliente = gestoreClienti.getCliente(email)
            self.statoLogin.loginCliente(cliente)
            esito = GestoreAutenticazione.controlloPassword(cliente, password)
            if esito:
                self.goVistaHomeCliente()
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

        email = self.ui.lineEditEmail.text().lower()

        esito = False

        if email == "":
            self.ui.labelErroreEmail.setText("Inserisci l'email!")
            esito = True
        elif not GestoreAutenticazione.controlloStrutturaEmail(email):
            self.ui.labelErroreEmail.setText("Email non Valida!")
            esito = True

        if esito: return

        gestoreClienti = GestoreClienti()

        esito = GestoreAutenticazione.controlloEmail(gestoreClienti.getListaClienti(), email)
        if esito:
            cliente = gestoreClienti.getCliente(email)
            GestoreAutenticazione.invioEmailRecuperoPassword(cliente)
            gestoreClienti.salvaDatiClienti()
            self.ui.labelRecuperoPassword.setText("Ti abbiamo spedito una mail!")
        else: self.ui.labelErroreEmail.setText("L'email non è stata trovata!")

