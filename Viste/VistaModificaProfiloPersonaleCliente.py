from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate
from ui_VistaModificaProfiloPersonaleCliente import Ui_VistaModificaProfiloPersonaleCliente
from Gestione.GestoreClienti import GestoreClienti
from Gestione.GestoreAutenticazione import GestoreAutenticazione
from Sistema.Cliente import Cliente

class VistaModificaProfiloPersonaleCliente(QWidget):
    def __init__(self, statoLogin, goVistaVisualizzaProfiloPersonaleCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaModificaProfiloPersonaleCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaProfiloPersonaleCliente = goVistaVisualizzaProfiloPersonaleCliente

        self.ui.pushButtonAnnulla.clicked.connect(goVistaVisualizzaProfiloPersonaleCliente)
        self.ui.pushButtonConferma.clicked.connect(self.conferma)

    def showEvent(self, event):
        super().showEvent(event)

        cliente = self.statoLogin.clienteAutenticato

        self.ui.lineEditNome.setText(cliente.nome)
        self.ui.lineEditCognome.setText(cliente.cognome)
        self.ui.dateEditDataNascita.setDate(cliente.dataNascita)
        self.ui.lineEditEmail.setText(cliente.email)
        self.ui.lineEditTelefono.setText(str(cliente.telefono))
        self.ui.labelCodiceFiscaleCliente.setText(cliente.codiceFiscale)
        self.ui.lineEditPassword.setText(cliente.password)

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

        cliente = self.statoLogin.clienteAutenticato

        codiceFiscale = cliente.getCodiceFiscale()
        punti = cliente.getPunti()

        gestoreClienti = GestoreClienti()

        for clienteNellaLista in gestoreClienti.listaClienti:
            if clienteNellaLista.getCodiceFiscale() == cliente.getCodiceFiscale():
                clienteNellaLista.setInfoCliente(nome, cognome, dataNascita, email, telefono, password, codiceFiscale, punti)
                self.statoLogin.loginCliente(clienteNellaLista)

        gestoreClienti.salvaDatiClienti()

        self.goVistaVisualizzaProfiloPersonaleCliente()
