from PySide6.QtWidgets import QWidget
from ui_VistaVisualizzaSpettacoloAmministratore import Ui_VistaVisualizzaSpettacoloAmministratore
from Gestione.GestoreSpettacoli import GestoreSpettacoli
from Gestione.GestoreBiglietti import GestoreBiglietti

class VistaVisualizzaSpettacoloAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaSpettacoliAmministratore, goVistaModificaSpettacoloAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaSpettacoloAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaSpettacoliAmministratore = goVistaVisualizzaSpettacoliAmministratore
        self.goVistaModificaSpettacoloAmministratore = goVistaModificaSpettacoloAmministratore

        self.ui.labelHomeButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaSpettacoliAmministratore)
        self.ui.pushButtonModifica.clicked.connect(self.modifica)
        self.ui.pushButtonModifica.setEnabled(False)
        self.ui.pushButtonElimina.clicked.connect(self.elimina)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.pushButtonModifica.setEnabled(False)

        spettacoloAmministratore = self.spettacoloAmministratore
        gestoreBiglietti = GestoreBiglietti()

        if spettacoloAmministratore.getStato():
            self.ui.pushButtonModifica.setEnabled(True)

        prezzo = gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloAmministratore)[0].getPrezzo()
        prezzoPunti = gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloAmministratore)[0].getPrezzoPunti()
        if gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloAmministratore) == []:
                prezzo = gestoreBiglietti = getListaBigliettiSpettacolo(spettacoloAmministratore)[0].getPrezzo()
                prezzoPunti = gestoreBiglietti = getListaBigliettiSpettacolo(spettacoloAmministratore).getPrezzoPunti()

        self.ui.labelTitoloSpettacolo.setText(spettacoloAmministratore.getTitolo())
        self.ui.labelGenereSpettacolo.setText(spettacoloAmministratore.getGenere())
        self.ui.labelSalaSpettacolo.setText(spettacoloAmministratore.getSala())
        self.ui.labelDataSpettacolo.setText(spettacoloAmministratore.getData().toString("dd/MM/yyyy"))
        self.ui.labelOrarioInizioSpettacolo.setText(spettacoloAmministratore.getOrarioInizio().toString("HH:mm:ss"))
        self.ui.labelOrarioFineSpettacolo.setText(spettacoloAmministratore.getOrarioFine().toString("HH:mm:ss"))
        self.ui.labelDurataSpettacolo.setText(f"{spettacoloAmministratore.getDurata()} minuti")
        self.ui.labelStatoSpettacolo.setText(spettacoloAmministratore.getTestoStato())
        self.ui.labelPrezzoSpettacolo.setText(f"{prezzo} €")
        self.ui.labelPrezzoPuntiSpettacolo.setText(f"{prezzoPunti} punti")

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
