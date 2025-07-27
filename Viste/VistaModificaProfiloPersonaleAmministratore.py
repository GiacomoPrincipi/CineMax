from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate
from ui_VistaModificaProfiloPersonaleAmministratore import Ui_VistaModificaProfiloPersonaleAmministratore
from Gestione.GestoreAmministratori import GestoreAmministratori
from Gestione.GestoreAutenticazione import GestoreAutenticazione
from Sistema.Amministratore import Amministratore

class VistaModificaProfiloPersonaleAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaVisualizzaProfiloPersonaleAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaModificaProfiloPersonaleAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaProfiloPersonaleAmministratore = goVistaVisualizzaProfiloPersonaleAmministratore

        self.ui.pushButtonAnnulla.clicked.connect(goVistaVisualizzaProfiloPersonaleAmministratore)
        self.ui.pushButtonConferma.clicked.connect(self.conferma)

    def showEvent(self, event):
        super().showEvent(event)

        amministratore = self.statoLogin.amministratoreAutenticato

        self.ui.lineEditNome.setText(amministratore.nome)
        self.ui.lineEditCognome.setText(amministratore.cognome)
        self.ui.dateEditDataNascita.setDate(amministratore.dataNascita)
        self.ui.lineEditEmail.setText(amministratore.email)
        self.ui.lineEditTelefono.setText(str(amministratore.telefono))
        self.ui.labelMatricolaAmministratore.setText(amministratore.matricola)
        self.ui.lineEditPassword.setText(amministratore.password)

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
        self.ui.labelErroreConfermaPassword.setText("")

        nome = self.ui.lineEditNome.text()
        cognome = self.ui.lineEditCognome.text()
        dataNascita = self.ui.dateEditDataNascita.date()
        email = self.ui.lineEditEmail.text()
        telefono = self.ui.lineEditTelefono.text()
        password = self.ui.lineEditPassword.text()
        confermaPassword = self.ui.lineEditConfermaPassword.text()

        if nome == "" or cognome == "" or dataNascita == QDate(1950, 1, 1) or email == "" or telefono == "" or password == "" or not GestoreAutenticazione.controlloStrutturaPassword(password) or confermaPassword == "":
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
            if confermaPassword == "":
                self.ui.labelErroreConfermaPassword.setText("Reinserisci la password!")
            elif confermaPassword != password:
                self.ui.labelErroreConfermaPassword.setText("Le password non corrispondono!")
            else: self.ui.labelErroreConfermaPassword.setText("")
            return

        if confermaPassword != password:
            self.ui.labelErroreConfermaPassword.setText("Le password non corrispondono!")
            return

        amministratore = self.statoLogin.amministratoreAutenticato

        matricola = amministratore.getMatricola()

        gestoreAmministratori = GestoreAmministratori()

        for amministratoreNellaLista in gestoreAmministratori.listaAmministratori:
            if amministratoreNellaLista.getMatricola() == amministratore.getMatricola():
                amministratoreNellaLista.setInfoAmministratore(nome, cognome, dataNascita, email, telefono, password, matricola)
                self.statoLogin.loginAmministratore(amministratoreNellaLista)

        gestoreAmministratori.salvaDatiAmministratori()

        self.goVistaVisualizzaProfiloPersonaleAmministratore()
