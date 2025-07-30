from PySide6.QtWidgets import QWidget
from ui_VistaVisualizzaRecensioneCliente import Ui_VistaVisualizzaRecensioneCliente
from Gestione.GestoreRecensioni import GestoreRecensioni

class VistaVisualizzaRecensioneCliente(QWidget):
    def __init__(self, statoLogin, goVistaHomeCliente, goVistaVisualizzaRecensioniCliente, goVistaModificaRecensioneCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaRecensioneCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaRecensioniCliente = goVistaVisualizzaRecensioniCliente
        self.goVistaModificaRecensioneCliente = goVistaModificaRecensioneCliente

        self.ui.labelHomeButton.clicked.connect(goVistaHomeCliente)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaRecensioniCliente)
        self.ui.pushButtonModifica.clicked.connect(self.modifica)
        self.ui.pushButtonElimina.clicked.connect(self.elimina)

    def showEvent(self, event):
        super().showEvent(event)

        recensioneCliente = self.recensioneCliente

        self.ui.labelDataRecensione.setText(recensioneCliente.getData().toString("dd/MM/yyyy"))
        self.ui.labelOraRecensione.setText(recensioneCliente.getOra().toString("HH:mm:ss"))
        self.ui.labelStelleRecensione.setText(f"{recensioneCliente.getStelle()}/5")
        self.ui.textBrowserTesto.setText(recensioneCliente.getTesto())


    def modifica(self):
        recensioneCliente = self.recensioneCliente

        self.goVistaModificaRecensioneCliente(recensioneCliente)

    def elimina(self):

        recensioneCliente = self.recensioneCliente
        gestoreRecensioni = GestoreRecensioni()

        gestoreRecensioni.rimuoviRecensione(recensioneCliente)

        self.goVistaVisualizzaRecensioniCliente()
