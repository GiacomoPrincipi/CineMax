from PySide6.QtWidgets import QWidget, QHeaderView
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

    def showEvent(self, event):
        super().showEvent(event)

        gestoreProdotti = GestoreProdotti()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Nome:", "Prezzo:"])

        for prodotto in gestoreProdotti.getListaProdottiDisponibili():
            self.modelloTabella.appendRow([QStandardItem(QStandardItem(prodotto.getNome())), QStandardItem(f"{prodotto.getPrezzo()} €")])

        self.ui.tableViewProdotti.setModel(self.modelloTabella)
        self.ui.tableViewProdotti.doubleClicked.connect(self.apriProdotto)

    def apriProdotto(self):

        gestoreProdotti = GestoreProdotti()

        riga = self.ui.tableViewProdotti.selectionModel().currentIndex().row()
        prodottoCliente = gestoreProdotti.getListaProdottiDisponibili()[riga]

        self.goVistaVisualizzaProdottoCliente(prodottoCliente)
