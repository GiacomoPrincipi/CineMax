from PySide6.QtWidgets import QWidget
from ui_VistaVisualizzaProfiloPersonaleCliente import Ui_VistaVisualizzaProfiloPersonaleCliente

class VistaVisualizzaProfiloPersonaleCliente(QWidget):
    def __init__(self, statoLogin, goVistaHomeCliente, goVistaModificaProfiloPersonaleCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProfiloPersonaleCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeCliente)
        self.ui.pushButtonModifica.clicked.connect(goVistaModificaProfiloPersonaleCliente)

    def showEvent(self, event):
        super().showEvent(event)

        cliente = self.statoLogin.clienteAutenticato

        self.ui.labelNomeCliente.setText(cliente.nome)
        self.ui.labelCognomeCliente.setText(cliente.cognome)
        self.ui.labelDataNascitaCliente.setText(cliente.dataNascita.toString("dd/MM/yyyy"))
        self.ui.labelEmailCliente.setText(cliente.email)
        self.ui.labelTelefonoCliente.setText(str(cliente.telefono))
        self.ui.labelPasswordCliente.setText(cliente.password)
        self.ui.labelCodiceFiscaleCliente.setText(cliente.codiceFiscale)
        self.ui.labelPuntiCliente.setText(str(cliente.punti))
