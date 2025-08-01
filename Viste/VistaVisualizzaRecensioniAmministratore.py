from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from Viste.ui_VistaVisualizzaRecensioniAmministratore import Ui_VistaVisualizzaRecensioniAmministratore
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
        self.ui.tableViewRecensioni.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.tableViewRecensioni.verticalScrollBar().setValue(self.ui.tableViewRecensioni.verticalScrollBar().minimum())

        gestoreRecensioni = GestoreRecensioni()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Identificativo:", "Cliente:", "Data:", "Ora:", "Stelle:", "Testo:"])

        for recensione in gestoreRecensioni.getListaRecensioni():
            self.modelloTabella.appendRow([QStandardItem(recensione.getId()), QStandardItem(recensione.getCliente().getCodiceFiscale()), QStandardItem(recensione.getData().toString("dd/MM/yyyy")), QStandardItem(recensione.getOra().toString("HH:mm:ss")), QStandardItem(f"{recensione.getStelle()}/5"), QStandardItem(recensione.getTesto())])

        self.ui.tableViewRecensioni.setModel(self.modelloTabella)
        self.ui.tableViewRecensioni.doubleClicked.connect(self.apriRecensione)

    def apriRecensione(self):

        gestoreRecensioni = GestoreRecensioni()

        riga = self.ui.tableViewRecensioni.selectionModel().currentIndex().row()
        recensioneAmministratore = gestoreRecensioni.getListaRecensioni()[riga]

        self.goVistaVisualizzaRecensioneAmministratore(recensioneAmministratore)
