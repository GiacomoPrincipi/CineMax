from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from ui_VistaVisualizzaProdottiAmministratore import Ui_VistaVisualizzaProdottiAmministratore
from Gestione.GestoreProdotti import GestoreProdotti

class VistaVisualizzaProdottiAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaProdottoAmministratore, goVistaInserisciProdottoAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProdottiAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaProdottoAmministratore = goVistaVisualizzaProdottoAmministratore

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.pushButtonInserisci.clicked.connect(goVistaInserisciProdottoAmministratore)

        self.ui.tableViewProdotti.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewProdotti.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewProdotti.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.ui.tableViewProdotti.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.tableViewProdotti.verticalScrollBar().setValue(self.ui.tableViewProdotti.verticalScrollBar().minimum())

        gestoreProdotti = GestoreProdotti()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Identificativo:", "Nome:", "Ingredienti:", "Allergeni:", "Prezzo:", "Prezzo in Punti:", "Disponibilità:"])

        for prodotto in gestoreProdotti.getListaProdotti():
            self.modelloTabella.appendRow([QStandardItem(prodotto.getId()), QStandardItem(prodotto.getNome()), QStandardItem(", ".join(prodotto.getIngredienti())), QStandardItem(", ".join(prodotto.getAllergeni())), QStandardItem(f"{prodotto.getPrezzo()} €"), QStandardItem(f"{prodotto.getPrezzoPunti()} punti"), QStandardItem(prodotto.getTestoDisponibile())])

        self.ui.tableViewProdotti.setModel(self.modelloTabella)
        self.ui.tableViewProdotti.doubleClicked.connect(self.apriProdotto)

    def apriProdotto(self):

        gestoreProdotti = GestoreProdotti()

        riga = self.ui.tableViewProdotti.selectionModel().currentIndex().row()
        prodottoAmministratore = gestoreProdotti.getListaProdotti()[riga]

        self.goVistaVisualizzaProdottoAmministratore(prodottoAmministratore)
