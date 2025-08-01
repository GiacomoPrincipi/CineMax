from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate
from Viste.ui_VistaInserisciAmministratoreAmministratore import Ui_VistaInserisciAmministratoreAmministratore
from Gestione.GestoreAmministratori import GestoreAmministratori
from Gestione.GestoreAutenticazione import GestoreAutenticazione
from Sistema.Amministratore import Amministratore

class VistaInserisciAmministratoreAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaVisualizzaAmministratoriAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaInserisciAmministratoreAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaAmministratoriAmministratore = goVistaVisualizzaAmministratoriAmministratore

        self.ui.pushButtonAnnulla.clicked.connect(goVistaVisualizzaAmministratoriAmministratore)
        self.ui.pushButtonConferma.clicked.connect(self.conferma)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.lineEditNome.setText("")
        self.ui.lineEditCognome.setText("")
        self.ui.dateEditDataNascita.setDate(QDate(1950, 1, 1))
        self.ui.lineEditEmail.setText("")
        self.ui.lineEditTelefono.setText("")
        self.ui.lineEditPassword.setText("")
        self.ui.lineEditConfermaPassword.setText("")

        self.ui.labelErroreNome.setText("")
        self.ui.labelErroreCognome.setText("")
        self.ui.labelErroreDataNascita.setText("")
        self.ui.labelErroreEmail.setText("")
        self.ui.labelErroreTelefono.setText("")
        self.ui.labelErrorePassword.setText("")
        self.ui.labelErrorePassword2.setText("")
        self.ui.labelErroreConfermaPassword.setText("")

    def conferma(self):
        self.ui.labelErroreNome.setText("")
        self.ui.labelErroreCognome.setText("")
        self.ui.labelErroreDataNascita.setText("")
        self.ui.labelErroreEmail.setText("")
        self.ui.labelErroreTelefono.setText("")
        self.ui.labelErrorePassword.setText("")
        self.ui.labelErrorePassword2.setText("")

        nome = self.ui.lineEditNome.text().title()
        cognome = self.ui.lineEditCognome.text().title()
        dataNascita = self.ui.dateEditDataNascita.date()
        email = self.ui.lineEditEmail.text().lower()
        telefono = self.ui.lineEditTelefono.text().replace(" ", "")
        password = self.ui.lineEditPassword.text()
        confermaPassword = self.ui.lineEditConfermaPassword.text()

        gestoreAmministratori = GestoreAmministratori()

        matricola = gestoreAmministratori.generaMatricolaAmministratore()

        esito = False

        if nome == "":
            self.ui.labelErroreNome.setText("Inserisci il nome!")
            esito = True
        elif not nome.isalpha():
            self.ui.labelErroreNome.setText("Nome non valido!")
            esito = True
        if cognome == "":
            self.ui.labelErroreCognome.setText("Inserisci il cognome!")
            esito = True
        elif not cognome.isalpha():
            self.ui.labelErroreCognome.setText("Cognome non valido!")
            esito = True
        if dataNascita == QDate(1950, 1, 1):
            self.ui.labelErroreDataNascita.setText("Inserisci la data!")
            esito = True
        elif dataNascita >= QDate.currentDate():
            self.ui.labelErroreDataNascita.setText("Data non valida!")
            esito = True
        if email == "":
            self.ui.labelErroreEmail.setText("Inserisci l'email!")
            esito = True
        elif not GestoreAutenticazione.controlloStrutturaEmail(email):
            self.ui.labelErroreEmail.setText("Email non valida!")
            esito = True
        if telefono == "":
            self.ui.labelErroreTelefono.setText("Inserisci il numero di telefono!")
            esito = True
        elif not telefono.isdigit():
            self.ui.labelErroreTelefono.setText("Telefono non valido!")
            esito = True
        if password == "":
            self.ui.labelErrorePassword.setText("Inserisci la password!")
            esito = True
        elif not GestoreAutenticazione.controlloStrutturaPassword(password):
            self.ui.labelErrorePassword.setText("Password non valida!")
            self.ui.labelErrorePassword2.setText("La password deve essere lunga almeno 8 caratteri e devi usare almeno un numero, una lettera maiuscola e uno dei simboli consentiti !?@#. Altri simboli non sono ammessi.")
            esito = True
        if confermaPassword == "":
            self.ui.labelErroreConfermaPassword.setText("Reinserisci la password!")
            esito = True
        elif confermaPassword != password:
            self.ui.labelErroreConfermaPassword.setText("Le password non corrispondono!")
            esito = True

        if esito: return

        amministratore = Amministratore(nome, cognome, dataNascita, email, telefono, password, matricola)
        gestoreAmministratori.inserisciAmministratore(amministratore)

        self.goVistaVisualizzaAmministratoriAmministratore()

