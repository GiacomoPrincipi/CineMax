from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from ui_VistaVisualizzaSpettacoliAmministratore import Ui_VistaVisualizzaSpettacoliAmministratore
from Gestione.GestoreSpettacoli import GestoreSpettacoli

class VistaVisualizzaSpettacoliAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaSpettacoloAmministratore, goVistaInserisciSpettacoloAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaSpettacoliAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaSpettacoloAmministratore = goVistaVisualizzaSpettacoloAmministratore

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.pushButtonInserisci.clicked.connect(goVistaInserisciSpettacoloAmministratore)

        self.ui.tableViewSpettacoli.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewSpettacoli.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewSpettacoli.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

    def showEvent(self, event):
        super().showEvent(event)

        gestoreSpettacoli = GestoreSpettacoli()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Titolo:", "Genere:", "Sala:", "Data:", "Orario Inizio:", "Orario Fine:"])

        gestoreSpettacoli.aggiornaStatoSpettacoli()

        for spettacolo in gestoreSpettacoli.getListaSpettacoli():
            self.modelloTabella.appendRow([QStandardItem(spettacolo.getTitolo()), QStandardItem(spettacolo.getGenere()), QStandardItem(spettacolo.getSala()), QStandardItem(spettacolo.getData().toString("dd/MM/yyyy")), QStandardItem(spettacolo.getOrarioInizio().toString("HH:mm:ss")), QStandardItem(spettacolo.getOrarioFine().toString("HH:mm:ss"))])

        self.ui.tableViewSpettacoli.setModel(self.modelloTabella)
        self.ui.tableViewSpettacoli.doubleClicked.connect(self.apriSpettacolo)

    def apriSpettacolo(self):

        gestoreSpettacoli = GestoreSpettacoli()

        riga = self.ui.tableViewSpettacoli.selectionModel().currentIndex().row()
        spettacoloAmministratore = gestoreSpettacoli.getListaSpettacoli()[riga]

        self.goVistaVisualizzaSpettacoloAmministratore(spettacoloAmministratore)
