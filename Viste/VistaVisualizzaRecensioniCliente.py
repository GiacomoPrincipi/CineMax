from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from Viste.ui_VistaVisualizzaRecensioniCliente import Ui_VistaVisualizzaRecensioniCliente
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
        self.ui.tableViewRecensioni.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.tableViewRecensioni.verticalScrollBar().setValue(self.ui.tableViewRecensioni.verticalScrollBar().minimum())

        gestoreRecensioni = GestoreRecensioni()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Data:", "Ora:", "Stelle:", "Testo:"])

        for recensione in sorted(gestoreRecensioni.getListaRecensioniCliente(self.statoLogin.clienteAutenticato), key = lambda oggetto: (oggetto.getData(), oggetto.getOra()), reverse = True):
            self.modelloTabella.appendRow([QStandardItem(recensione.getData().toString("dd/MM/yyyy")), QStandardItem(recensione.getOra().toString("HH:mm:ss")), QStandardItem(f"{recensione.getStelle()}/5"), QStandardItem(recensione.getTesto())])

        self.ui.tableViewRecensioni.setModel(self.modelloTabella)
        self.ui.tableViewRecensioni.doubleClicked.connect(self.apriRecensione)

    def apriRecensione(self):

        gestoreRecensioni = GestoreRecensioni()

        riga = self.ui.tableViewRecensioni.selectionModel().currentIndex().row()
        recensioneCliente = gestoreRecensioni.getListaRecensioniCliente(self.statoLogin.clienteAutenticato)[riga]

        self.goVistaVisualizzaRecensioneCliente(recensioneCliente)


