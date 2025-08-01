from PySide6.QtWidgets import QWidget
from Viste.ui_VistaVisualizzaProdottoCliente import Ui_VistaVisualizzaProdottoCliente

class VistaVisualizzaProdottoCliente(QWidget):
    def __init__(self, statoLogin, goVistaHomeCliente, goVistaVisualizzaProdottiCliente, goVistaAcquistoProdottoCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProdottoCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaAcquistoProdottoCliente = goVistaAcquistoProdottoCliente

        self.ui.labelHomeButton.clicked.connect(goVistaHomeCliente)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaProdottiCliente)
        self.ui.pushButtonAcquista.clicked.connect(self.acquisto)

    def showEvent(self, event):
        super().showEvent(event)

        prodottoCliente = self.prodottoCliente

        self.ui.labelNomeProdotto.setText(prodottoCliente.getNome())
        self.ui.labelIngredientiProdotto.setText(", ".join(prodottoCliente.getIngredienti()))
        self.ui.labelAllergeniProdotto.setText(", ".join(prodottoCliente.getAllergeni()))
        self.ui.labelPrezzoProdotto.setText(f"{prodottoCliente.getPrezzo()} €")
        self.ui.labelPrezzoPuntiProdotto.setText(f"{prodottoCliente.getPrezzoPunti()} punti")

    def acquisto(self):
            self.goVistaAcquistoProdottoCliente(self.prodottoCliente)

