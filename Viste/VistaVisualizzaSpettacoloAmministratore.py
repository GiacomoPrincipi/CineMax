from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from Viste.ui_VistaVisualizzaSpettacoloAmministratore import Ui_VistaVisualizzaSpettacoloAmministratore
from Gestione.GestoreSpettacoli import GestoreSpettacoli
from Gestione.GestoreBiglietti import GestoreBiglietti

class VistaVisualizzaSpettacoloAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaSpettacoliAmministratore, goVistaModificaSpettacoloAmministratore, goVistaVisualizzaBigliettoAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaSpettacoloAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaSpettacoliAmministratore = goVistaVisualizzaSpettacoliAmministratore
        self.goVistaModificaSpettacoloAmministratore = goVistaModificaSpettacoloAmministratore
        self.goVistaVisualizzaBigliettoAmministratore = goVistaVisualizzaBigliettoAmministratore

        self.ui.labelHomeButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaSpettacoliAmministratore)
        self.ui.pushButtonModifica.clicked.connect(self.modifica)
        self.ui.pushButtonModifica.setEnabled(False)
        self.ui.pushButtonElimina.clicked.connect(self.elimina)
        self.ui.pushButtonApri.clicked.connect(self.apriBiglietto)
        self.ui.pushButtonApri.setEnabled(False)

        self.ui.tableViewBiglietti.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewBiglietti.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewBiglietti.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.ui.tableViewBiglietti.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.pushButtonModifica.setEnabled(False)

        spettacoloAmministratore = self.spettacoloAmministratore
        gestoreBiglietti = GestoreBiglietti()

        if spettacoloAmministratore.getStato():
            self.ui.pushButtonModifica.setEnabled(True)

        prezzo = gestoreBiglietti.getListaBigliettiSpettacolo(spettacoloAmministratore)[0].getPrezzo()
        prezzoPunti = gestoreBiglietti.getListaBigliettiSpettacolo(spettacoloAmministratore)[0].getPrezzoPunti()
        if gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloAmministratore) != []:
            prezzo = gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloAmministratore)[0].getPrezzo()
            prezzoPunti = gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloAmministratore)[0].getPrezzoPunti()

        genere = ", ".join(spettacoloAmministratore.getGenere())

        self.ui.labelTitoloSpettacolo.setText(spettacoloAmministratore.getTitolo())
        self.ui.labelIdSpettacolo.setText(spettacoloAmministratore.getId())
        self.ui.labelGenereSpettacolo.setText(genere)
        self.ui.labelSalaSpettacolo.setText(spettacoloAmministratore.getSala())
        self.ui.labelDataSpettacolo.setText(spettacoloAmministratore.getData().toString("dd/MM/yyyy"))
        self.ui.labelOrarioInizioSpettacolo.setText(spettacoloAmministratore.getOrarioInizio().toString("HH:mm:ss"))
        self.ui.labelOrarioFineSpettacolo.setText(spettacoloAmministratore.getOrarioFine().toString("HH:mm:ss"))
        self.ui.labelDurataSpettacolo.setText(f"{spettacoloAmministratore.getDurata()} minuti")
        self.ui.labelStatoSpettacolo.setText(spettacoloAmministratore.getTestoStato())
        self.ui.labelPrezzoSpettacolo.setText(f"{prezzo} €")
        self.ui.labelPrezzoPuntiSpettacolo.setText(f"{prezzoPunti} punti")
        
        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Identificativo:", "Posto:", "Disponibilità:"])

        for biglietto in sorted(gestoreBiglietti.getListaBigliettiSpettacolo(spettacoloAmministratore), key = lambda oggetto: oggetto.getPosto(), reverse = False):
            self.modelloTabella.appendRow([QStandardItem(biglietto.getId()), QStandardItem(str(biglietto.getPosto())), QStandardItem(biglietto.getTestoDisponibile())])

        self.ui.tableViewBiglietti.setModel(self.modelloTabella)

        self.ui.tableViewBiglietti.clicked.connect(self.abilitaBottone)

    def modifica(self):
        spettacoloAmministratore = self.spettacoloAmministratore

        self.goVistaModificaSpettacoloAmministratore(spettacoloAmministratore)

    def elimina(self):
        spettacoloAmministratore = self.spettacoloAmministratore
        gestoreSpettacoli = GestoreSpettacoli()

        gestoreSpettacoli.rimuoviSpettacolo(spettacoloAmministratore)

        gestoreBiglietti = GestoreBiglietti()
        for biglietto in gestoreBiglietti.getListaBigliettiSpettacolo(spettacoloAmministratore):
            gestoreBiglietti.rimuoviBiglietto(biglietto)

        self.goVistaVisualizzaSpettacoliAmministratore()


    def apriBiglietto(self):

        spettacoloAmministratore = self.spettacoloAmministratore
        gestoreBiglietti = GestoreBiglietti()

        riga = self.ui.tableViewBiglietti.selectionModel().currentIndex().row()
        bigliettoAmministratore = sorted(gestoreBiglietti.getListaBigliettiSpettacolo(spettacoloAmministratore), key = lambda oggetto: oggetto.getPosto(), reverse = False)[riga]

        self.goVistaVisualizzaBigliettoAmministratore(bigliettoAmministratore)

    def abilitaBottone(self):
        self.ui.pushButtonApri.setEnabled(True)
