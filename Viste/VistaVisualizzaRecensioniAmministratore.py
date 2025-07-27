from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from ui_VistaVisualizzaRecensioniAmministratore import Ui_VistaVisualizzaRecensioniAmministratore
from Gestione.GestoreRecensioni import GestoreRecensioni

class VistaVisualizzaRecensioniAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaRecensioneAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaRecensioniAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaRecensioneAmministratore = goVistaVisualizzaRecensioneAmministratore

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeAmministratore)

        self.ui.tableViewRecensioni.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewRecensioni.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewRecensioni.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

    def showEvent(self, event):
        super().showEvent(event)

        gestoreRecensioni = GestoreRecensioni()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Cliente:", "Data:", "Ora:", "Stelle:"])

        for recensione in gestoreRecensioni.getListaRecensioni():
            self.modelloTabella.appendRow([QStandardItem(recensione.getCliente().getCodiceFiscale()), QStandardItem(recensione.getData().toString("dd/MM/yyyy")), QStandardItem(recensione.getOra().toString("HH:mm:ss")), QStandardItem(str(recensione.getStelle()))])

        self.ui.tableViewRecensioni.setModel(self.modelloTabella)
        self.ui.tableViewRecensioni.doubleClicked.connect(self.apriRecensione)

    def apriRecensione(self):

        gestoreRecensioni = GestoreRecensioni()

        riga = self.ui.tableViewRecensioni.selectionModel().currentIndex().row()
        recensioneAmministratore = gestoreRecensioni.getListaRecensioni()[riga]

        self.goVistaVisualizzaRecensioneAmministratore(recensioneAmministratore)
