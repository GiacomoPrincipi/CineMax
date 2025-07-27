from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from ui_VistaVisualizzaRecensioniCliente import Ui_VistaVisualizzaRecensioniCliente
from Gestione.GestoreRecensioni import GestoreRecensioni

class VistaVisualizzaRecensioniCliente(QWidget):
    def __init__(self, statoLogin, goVistaHomeCliente, goVistaVisualizzaRecensioneCliente, goVistaInserisciRecensioneCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaRecensioniCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaRecensioneCliente = goVistaVisualizzaRecensioneCliente

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeCliente)
        self.ui.pushButtonInserisci.clicked.connect(goVistaInserisciRecensioneCliente)

        self.ui.tableViewRecensioni.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewRecensioni.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewRecensioni.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

    def showEvent(self, event):
        super().showEvent(event)

        gestoreRecensioni = GestoreRecensioni()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Data:", "Ora:", "Stelle:"])

        for recensione in gestoreRecensioni.getListaRecensioniCliente(self.statoLogin.clienteAutenticato):
            self.modelloTabella.appendRow([QStandardItem(QStandardItem(recensione.getData().toString("dd/MM/yyyy"))), QStandardItem(recensione.getOra().toString("HH:mm:ss")), QStandardItem(str(recensione.getStelle()))])

        self.ui.tableViewRecensioni.setModel(self.modelloTabella)
        self.ui.tableViewRecensioni.doubleClicked.connect(self.apriRecensione)

    def apriRecensione(self):

        gestoreRecensioni = GestoreRecensioni()

        riga = self.ui.tableViewRecensioni.selectionModel().currentIndex().row()
        recensioneCliente = gestoreRecensioni.getListaRecensioniCliente(self.statoLogin.clienteAutenticato)[riga]

        self.goVistaVisualizzaRecensioneCliente(recensioneCliente)


