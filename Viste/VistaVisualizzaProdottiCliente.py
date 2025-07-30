from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from ui_VistaVisualizzaProdottiCliente import Ui_VistaVisualizzaProdottiCliente
from Gestione.GestoreProdotti import GestoreProdotti

class VistaVisualizzaProdottiCliente(QWidget):
    def __init__(self, statoLogin, goVistaHomeCliente, goVistaVisualizzaProdottoCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProdottiCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaProdottoCliente = goVistaVisualizzaProdottoCliente

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeCliente)

        self.ui.tableViewProdotti.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewProdotti.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewProdotti.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.ui.tableViewProdotti.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.tableViewProdotti.verticalScrollBar().setValue(self.ui.tableViewProdotti.verticalScrollBar().minimum())

        gestoreProdotti = GestoreProdotti()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Nome:", "Ingredienti:", "allergeni:", "Prezzo:", "Prezzoin Punti:"])

        for prodotto in gestoreProdotti.getListaProdottiDisponibili():
            self.modelloTabella.appendRow([QStandardItem(prodotto.getNome()), QStandardItem(", ".join(prodotto.getIngredienti())), QStandardItem(", ".join(prodotto.getAllergeni())), QStandardItem(f"{prodotto.getPrezzo()} €"), QStandardItem(f"{prodotto.getPrezzoPunti()} punti")])

        self.ui.tableViewProdotti.setModel(self.modelloTabella)
        self.ui.tableViewProdotti.doubleClicked.connect(self.apriProdotto)

    def apriProdotto(self):

        gestoreProdotti = GestoreProdotti()

        riga = self.ui.tableViewProdotti.selectionModel().currentIndex().row()
        prodottoCliente = gestoreProdotti.getListaProdottiDisponibili()[riga]

        self.goVistaVisualizzaProdottoCliente(prodottoCliente)
