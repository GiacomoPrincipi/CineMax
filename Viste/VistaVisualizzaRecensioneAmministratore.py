from PySide6.QtWidgets import QWidget
from Viste.ui_VistaVisualizzaRecensioneAmministratore import Ui_VistaVisualizzaRecensioneAmministratore

class VistaVisualizzaRecensioneAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaRecensioniAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaRecensioneAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.ui.labelHomeButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaRecensioniAmministratore)

    def showEvent(self, event):
        super().showEvent(event)

        recensioneAmministratore = self.recensioneAmministratore

        self.ui.labelIdRecensione.setText(recensioneAmministratore.getId())
        self.ui.labelCodiceFiscaleRecensione.setText(recensioneAmministratore.getCliente().getCodiceFiscale())
        self.ui.labelDataRecensione.setText(recensioneAmministratore.getData().toString("dd/MM/yyyy"))
        self.ui.labelOraRecensione.setText(recensioneAmministratore.getOra().toString("HH:mm:ss"))
        self.ui.labelStelleRecensione.setText(f"{recensioneAmministratore.getStelle()}/5")
        self.ui.textBrowserTesto.setText(recensioneAmministratore.getTesto())
