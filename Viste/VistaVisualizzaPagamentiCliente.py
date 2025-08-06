from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from Viste.ui_VistaVisualizzaPagamentiCliente import Ui_VistaVisualizzaPagamentiCliente
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
        self.ui.tableViewPagamenti.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.tableViewPagamenti.verticalScrollBar().setValue(self.ui.tableViewPagamenti.verticalScrollBar().minimum())

        gestorePagamenti = GestorePagamenti()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Identificativo:", "Data:", "Ora:", "Articolo:", "Importo:", "Importo Punti:"])

        for pagamento in sorted(gestorePagamenti.getListaPagamentiCliente(self.statoLogin.clienteAutenticato), key = lambda oggetto: (oggetto.getData(), oggetto.getOra()), reverse = True):
            if isinstance(pagamento.getArticolo(), Biglietto):
                testo = pagamento.getArticolo().getSpettacolo().getId()
            elif isinstance(pagamento.getArticolo(), Prodotto):
                testo = pagamento.getArticolo().getId()
            self.modelloTabella.appendRow([QStandardItem(pagamento.getId()), QStandardItem(pagamento.getData().toString("dd/MM/yyyy")), QStandardItem(pagamento.getOra().toString("HH:mm:ss")), QStandardItem(testo), QStandardItem(f"{pagamento.getImporto()} €"), QStandardItem(f"{pagamento.getImportoPunti()} punti")])

        self.ui.tableViewPagamenti.setModel(self.modelloTabella)
        self.ui.tableViewPagamenti.doubleClicked.connect(self.apriPagamento)

    def apriPagamento(self):

        gestorePagamenti = GestorePagamenti()

        riga = self.ui.tableViewPagamenti.selectionModel().currentIndex().row()
        pagamentoCliente = gestorePagamenti.getListaPagamentiCliente(self.statoLogin.clienteAutenticato)[riga]

        self.goVistaVisualizzaPagamentoCliente(pagamentoCliente)

