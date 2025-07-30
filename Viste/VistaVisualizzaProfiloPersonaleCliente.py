from PySide6.QtWidgets import QWidget
from ui_VistaVisualizzaProfiloPersonaleCliente import Ui_VistaVisualizzaProfiloPersonaleCliente
from Gestione.GestoreClienti import GestoreClienti

class VistaVisualizzaProfiloPersonaleCliente(QWidget):
    def __init__(self, statoLogin, goVistaHome, goVistaHomeCliente, goVistaModificaProfiloPersonaleCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProfiloPersonaleCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaHome = goVistaHome

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeCliente)
        self.ui.pushButtonModifica.clicked.connect(goVistaModificaProfiloPersonaleCliente)
        self.ui.pushButtonElimina.clicked.connect(self.elimina)

    def showEvent(self, event):
        super().showEvent(event)

        cliente = self.statoLogin.clienteAutenticato

        self.ui.labelNomeCliente.setText(cliente.getNome())
        self.ui.labelCognomeCliente.setText(cliente.getCognome())
        self.ui.labelDataNascitaCliente.setText(cliente.getDataNascita().toString("dd/MM/yyyy"))
        self.ui.labelEmailCliente.setText(cliente.getEmail())
        self.ui.labelTelefonoCliente.setText(cliente.getTelefono())
        self.ui.labelPasswordCliente.setText(cliente.getPassword())
        self.ui.labelCodiceFiscaleCliente.setText(cliente.getCodiceFiscale())
        self.ui.labelPuntiCliente.setText(str(cliente.getPunti()))

    def elimina(self):

        cliente = self.statoLogin.clienteAutenticato
        gestoreClienti = GestoreClienti()

        gestoreClienti.rimuoviCliente(cliente)
        self.statoLogin.logoutCliente()

        self.goVistaHome()
