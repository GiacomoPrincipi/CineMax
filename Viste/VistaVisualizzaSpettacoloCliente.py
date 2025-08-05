from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from Viste.ui_VistaVisualizzaSpettacoloCliente import Ui_VistaVisualizzaSpettacoloCliente
from Gestione.GestoreBiglietti import GestoreBiglietti

class VistaVisualizzaSpettacoloCliente(QWidget):
    def __init__(self, statoLogin, goVistaHomeCliente, goVistaVisualizzaSpettacoliCliente, goVistaAcquistoBigliettoCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaSpettacoloCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaAcquistoBigliettoCliente = goVistaAcquistoBigliettoCliente

        self.ui.labelHomeButton.clicked.connect(goVistaHomeCliente)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaSpettacoliCliente)
        self.ui.pushButtonApri.clicked.connect(self.apriBiglietto)
        self.ui.pushButtonApri.setEnabled(False)

        self.ui.tableViewBiglietti.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewBiglietti.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewBiglietti.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.ui.tableViewBiglietti.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.tableViewBiglietti.verticalScrollBar().setValue(self.ui.tableViewBiglietti.verticalScrollBar().minimum())

        self.ui.pushButtonApri.setEnabled(False)

        spettacoloCliente = self.spettacoloCliente
        gestoreBiglietti = GestoreBiglietti()

        self.ui.labelTitoloSpettacolo.setText(spettacoloCliente.getTitolo())
        self.ui.labelGenereSpettacolo.setText(spettacoloCliente.getGenere())
        self.ui.labelSalaSpettacolo.setText(spettacoloCliente.getSala())
        self.ui.labelDataSpettacolo.setText(spettacoloCliente.getData().toString("dd/MM/yyyy"))
        self.ui.labelOrarioInizioSpettacolo.setText(spettacoloCliente.getOrarioInizio().toString("HH:mm:ss"))
        self.ui.labelOrarioFineSpettacolo.setText(spettacoloCliente.getOrarioFine().toString("HH:mm:ss"))
        self.ui.labelDurataSpettacolo.setText(f"{spettacoloCliente.getDurata()} minuti")

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Posto:", "Prezzo Adulto:", "Prezzo in Punti:"])

        for biglietto in gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloCliente):
            self.modelloTabella.appendRow([QStandardItem(str(biglietto.getPosto())), QStandardItem(f"{biglietto.getPrezzo()} €"), QStandardItem(f"{biglietto.getPrezzoPunti()} punti")])

        self.ui.tableViewBiglietti.setModel(self.modelloTabella)

        self.ui.tableViewBiglietti.clicked.connect(self.abilitaBottone)

    def apriBiglietto(self):

        spettacoloCliente = self.spettacoloCliente
        gestoreBiglietti = GestoreBiglietti()

        riga = self.ui.tableViewBiglietti.selectionModel().currentIndex().row()
        bigliettoCliente = gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloCliente)[riga]

        self.goVistaAcquistoBigliettoCliente(bigliettoCliente)

    def abilitaBottone(self):
        self.ui.pushButtonApri.setEnabled(True)
