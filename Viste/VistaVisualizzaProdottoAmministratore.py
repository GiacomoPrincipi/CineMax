from PySide6.QtWidgets import QWidget
from Viste.ui_VistaVisualizzaProdottoAmministratore import Ui_VistaVisualizzaProdottoAmministratore
from Gestione.GestoreProdotti import GestoreProdotti

class VistaVisualizzaProdottoAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaProdottiAmministratore, goVistaModificaProdottoAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProdottoAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaProdottiAmministratore = goVistaVisualizzaProdottiAmministratore
        self.goVistaModificaProdottoAmministratore = goVistaModificaProdottoAmministratore

        self.ui.labelHomeButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaProdottiAmministratore)
        self.ui.pushButtonModifica.clicked.connect(self.modifica)
        self.ui.pushButtonElimina.clicked.connect(self.elimina)

    def showEvent(self, event):
        super().showEvent(event)

        prodottoAmministratore = self.prodottoAmministratore

        ingredienti = ", ".join(prodottoAmministratore.getIngredienti())

        allergeni = ", ".join(prodottoAmministratore.getAllergeni())

        self.ui.labelNomeProdotto.setText(prodottoAmministratore.getNome())
        self.ui.labelIdProdotto.setText(prodottoAmministratore.getId())
        self.ui.labelIngredientiProdotto.setText(ingredienti)
        self.ui.labelAllergeniProdotto.setText(allergeni)
        self.ui.labelPrezzoProdotto.setText(f"{prodottoAmministratore.getPrezzo()} €")
        self.ui.labelPrezzoPuntiProdotto.setText(f"{prodottoAmministratore.getPrezzoPunti()} punti")
        self.ui.labelDisponibileProdotto.setText(prodottoAmministratore.getTestoDisponibile())

    def modifica(self):
        prodottoAmministratore = self.prodottoAmministratore

        self.goVistaModificaProdottoAmministratore(prodottoAmministratore)

    def elimina(self):
        prodottoAmministratore = self.prodottoAmministratore
        gestoreProdotti = GestoreProdotti()

        gestoreProdotti.rimuoviProdotto(prodottoAmministratore)

        self.goVistaVisualizzaProdottiAmministratore()
