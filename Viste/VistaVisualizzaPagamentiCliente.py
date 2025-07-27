from PySide6.QtWidgets import QWidget, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from ui_VistaVisualizzaPagamentiCliente import Ui_VistaVisualizzaPagamentiCliente
from Gestione.GestorePagamenti import GestorePagamenti
from Sistema.Biglietto import Biglietto
from Sistema.Prodotto import Prodotto

class VistaVisualizzaPagamentiCliente(QWidget):
    def __init__(self, statoLogin, goVistaHomeCliente, goVistaVisualizzaPagamentoCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaPagamentiCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaPagamentoCliente = goVistaVisualizzaPagamentoCliente

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeCliente)

        self.ui.tableViewPagamenti.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewPagamenti.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewPagamenti.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

    def showEvent(self, event):
        super().showEvent(event)

        gestorePagamenti = GestorePagamenti()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Data:", "Ora:", "Articolo:"])

        for pagamento in gestorePagamenti.getListaPagamentiCliente(self.statoLogin.clienteAutenticato):
            if isinstance(pagamento.getArticolo(), Biglietto):
                testo = pagamento.getArticolo().getSpettacolo().getTitolo()
            elif isinstance(pagamento.getArticolo(), Prodotto):
                testo = pagamento.getArticolo().getNome()
            self.modelloTabella.appendRow([QStandardItem(QStandardItem(pagamento.getData().toString("dd/MM/yyyy"))), QStandardItem(pagamento.getOra().toString("HH:mm:ss")), QStandardItem(testo)])

        self.ui.tableViewPagamenti.setModel(self.modelloTabella)
        self.ui.tableViewPagamenti.doubleClicked.connect(self.apriPagamento)

    def apriPagamento(self):

        gestorePagamenti = GestorePagamenti()

        riga = self.ui.tableViewPagamenti.selectionModel().currentIndex().row()
        pagamentoCliente = gestorePagamenti.getListaPagamentiCliente(self.statoLogin.clienteAutenticato)[riga]

        self.goVistaVisualizzaPagamentoCliente(pagamentoCliente)

