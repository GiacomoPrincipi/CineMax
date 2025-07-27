from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate
from ui_VistaInserisciAmministratoreAmministratore import Ui_VistaInserisciAmministratoreAmministratore
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
        self.ui.lineEditMatricola.setText("")
        self.ui.lineEditConfermaPassword.setText("")

        self.ui.labelErroreNome.setText("")
        self.ui.labelErroreCognome.setText("")
        self.ui.labelErroreDataNascita.setText("")
        self.ui.labelErroreEmail.setText("")
        self.ui.labelErroreTelefono.setText("")
        self.ui.labelErrorePassword.setText("")
        self.ui.labelErrorePassword2.setText("")
        self.ui.labelErroreMatricola.setText("")
        self.ui.labelErroreConfermaPassword.setText("")

    def conferma(self):
        self.ui.labelErroreNome.setText("")
        self.ui.labelErroreCognome.setText("")
        self.ui.labelErroreDataNascita.setText("")
        self.ui.labelErroreEmail.setText("")
        self.ui.labelErroreTelefono.setText("")
        self.ui.labelErrorePassword.setText("")
        self.ui.labelErrorePassword2.setText("")
        self.ui.labelErroreMatricola.setText("")

        nome = self.ui.lineEditNome.text()
        cognome = self.ui.lineEditCognome.text()
        dataNascita = self.ui.dateEditDataNascita.date()
        email = self.ui.lineEditEmail.text()
        telefono = self.ui.lineEditTelefono.text()
        password = self.ui.lineEditPassword.text()
        matricola = self.ui.lineEditMatricola.text()
        confermaPassword = self.ui.lineEditConfermaPassword.text()

        gestoreAmministratori = GestoreAmministratori()

        if nome == "" or cognome == "" or dataNascita == QDate(1950, 1, 1) or email == "" or telefono == "" or password == "" or not GestoreAutenticazione.controlloStrutturaPassword(password) or matricola == "" or confermaPassword == "":
            if nome == "":
                self.ui.labelErroreNome.setText("Inserisci il nome!")
            elif not nome.isalpha():
                self.ui.labelErroreNome.setText("Nome non valido!")
            if cognome == "":
                self.ui.labelErroreCognome.setText("Inserisci il cognome!")
            elif not cognome.isalpha():
                self.ui.labelErroreCognome.setText("Cognome non valido!")
            if dataNascita == QDate(1950, 1, 1):
                self.ui.labelErroreDataNascita.setText("Inserisci la data!")
            elif dataNascita >= QDate.currentDate():
                self.ui.labelErroreDataNascita.setText("Data non valida!")
            if email == "":
                self.ui.labelErroreEmail.setText("Inserisci l'email!")
            elif "@" not in email:
                self.ui.labelErroreEmail.setText("Email non valida!")
            if telefono == "":
                self.ui.labelErroreTelefono.setText("Inserisci il numero di telefono!")
            elif not telefono.isdigit():
                self.ui.labelErroreTelefono.setText("Telefono non valido!")
            if password == "":
                self.ui.labelErrorePassword.setText("Inserisci la password!")
            elif not GestoreAutenticazione.controlloStrutturaPassword(password):
                self.ui.labelErrorePassword.setText("Password non valida!")
                self.ui.labelErrorePassword2.setText("La password deve essere lunga almeno 8 caratteri e devi usare almeno un numero, una lettera maiuscola e uno dei simboli !?@#")
            if matricola == "":
                self.ui.labelErroreMatricola.setText("Inserisci la matricola!")
            elif len(matricola) != 5 or not matricola.isalnum():
                self.ui.labelErroreMatricola.setText("Matricola non valida!")
            elif not gestoreAmministratori.controlloMatricola(matricola):
                self.ui.labelErroreMatricola.setText("Matricola già utilizzata!")
            if confermaPassword == "":
                self.ui.labelErroreConfermaPassword.setText("Reinserisci la password!")
            elif confermaPassword != password:
                self.ui.labelErroreConfermaPassword.setText("Le password non corrispondono!")
            else: self.ui.labelErroreConfermaPassword.setText("")
            return

        if confermaPassword != password:
            self.ui.labelErroreConfermaPassword.setText("Le password non corrispondono!")
            return

        amministratore = Amministratore(nome, cognome, dataNascita, email, telefono, password, matricola)
        gestoreAmministratori.inserisciAmministratore(amministratore)

        self.goVistaVisualizzaAmministratoriAmministratore()

