from PySide6.QtWidgets import QWidget
from ui_VistaVisualizzaSpettacoloAmministratore import Ui_VistaVisualizzaSpettacoloAmministratore

class VistaVisualizzaSpettacoloAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaSpettacoliAmministratore, goVistaModificaSpettacoloAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaSpettacoloAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaModificaSpettacoloAmministratore = goVistaModificaSpettacoloAmministratore

        self.ui.labelHomeButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaSpettacoliAmministratore)
        self.ui.pushButtonModifica.clicked.connect(self.modifica)

    def showEvent(self, event):
        super().showEvent(event)

        spettacoloAmministratore = self.spettacoloAmministratore

        self.ui.labelTitoloSpettacolo.setText(spettacoloAmministratore.getTitolo())
        self.ui.labelGenereSpettacolo.setText(spettacoloAmministratore.getGenere())
        self.ui.labelSalaSpettacolo.setText(spettacoloAmministratore.getSala())
        self.ui.labelDataSpettacolo.setText(spettacoloAmministratore.getData().toString("dd/MM/yyyy"))
        self.ui.labelOrarioInizioSpettacolo.setText(spettacoloAmministratore.getOrarioInizio().toString("HH:mm:ss"))
        self.ui.labelOrarioFineSpettacolo.setText(spettacoloAmministratore.getOrarioFine().toString("HH:mm:ss"))
        self.ui.labelDurataSpettacolo.setText(f"{spettacoloAmministratore.getDurata()} minuti")
        self.ui.labelStatoSpettacolo.setText(spettacoloAmministratore.getTestoStato())
        #self.ui.labelPrezzoSpettacolo.setText(str(bigliettoAmministratore.getPrezzo()))
        #self.ui.labelPrezzoPuntiSpettacolo.setText(str(bigliettoAmministratore.getPrezzoPunti()))

    def modifica(self):
        spettacoloAmministratore = self.spettacoloAmministratore

        self.goVistaModificaSpettacoloAmministratore(spettacoloAmministratore)
