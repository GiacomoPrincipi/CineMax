from PySide6.QtWidgets import QWidget
from Viste.ui_VistaVisualizzaBigliettoAmministratore import Ui_VistaVisualizzaBigliettoAmministratore
from Gestione.GestorePagamenti import GestorePagamenti


class VistaVisualizzaBigliettoAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaSpettacoloAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaBigliettoAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaSpettacoloAmministratore = goVistaVisualizzaSpettacoloAmministratore

        self.ui.labelHomeButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.labelIndietroButton.clicked.connect(self.indietro)

    def showEvent(self, event):
        super().showEvent(event)

        bigliettoAmministratore = self.bigliettoAmministratore

        gestorePagamenti = GestorePagamenti()

        self.ui.labelPostoBiglietto.setText(str(bigliettoAmministratore.getPosto()))
        self.ui.labelIdBiglietto.setText(bigliettoAmministratore.getId())
        self.ui.labelTipoBiglietto.setText(bigliettoAmministratore.getTipo())
        if bigliettoAmministratore.getTipo() == None:
            if not bigliettoAmministratore.getSpettacolo().getStato():
                self.ui.labelTipoBiglietto.setText("Non Definito")
            else: self.ui.labelTipoBiglietto.setText("Da Definire")
        self.ui.labelDisponibileBiglietto.setText(bigliettoAmministratore.getTestoDisponibile())
        if bigliettoAmministratore.getSpettacolo().getStato():
            self.ui.labelClienteBiglietto.setText("Da Associare")
        else: self.ui.labelClienteBiglietto.setText("Non Associato")
        for pagamento in gestorePagamenti.getListaPagamenti():
            if pagamento.getArticolo().getId() == bigliettoAmministratore.getId():
                self.ui.labelClienteBiglietto.setText(pagamento.getCliente().getCodiceFiscale())

    def indietro(self):

        bigliettoAmministratore = self.bigliettoAmministratore
        spettacoloAmministratore = bigliettoAmministratore.getSpettacolo()

        self.goVistaVisualizzaSpettacoloAmministratore(spettacoloAmministratore)

