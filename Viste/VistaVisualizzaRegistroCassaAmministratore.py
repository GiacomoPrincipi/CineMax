from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from Viste.ui_VistaVisualizzaRegistroCassaAmministratore import Ui_VistaVisualizzaRegistroCassaAmministratore
from Gestione.GestorePagamenti import GestorePagamenti
from Sistema.Biglietto import Biglietto
from Sistema.Prodotto import Prodotto

class VistaVisualizzaRegistroCassaAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaPagamentoAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaRegistroCassaAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaPagamentoAmministratore = goVistaVisualizzaPagamentoAmministratore

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeAmministratore)

        self.ui.tableViewPagamenti.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewPagamenti.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewPagamenti.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.ui.tableViewPagamenti.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.tableViewPagamenti.verticalScrollBar().setValue(self.ui.tableViewPagamenti.verticalScrollBar().minimum())

        gestorePagamenti = GestorePagamenti()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Identificativo:", "Cliente:", "Data:", "Ora:", "Articolo:", "Importo:", "Importo in Punti:"])

        for pagamento in gestorePagamenti.getListaPagamenti():
            if isinstance(pagamento.getArticolo(), Biglietto):
                testo = pagamento.getArticolo().getSpettacolo().getTitolo()
            elif isinstance(pagamento.getArticolo(), Prodotto):
                testo = pagamento.getArticolo().getNome()
            self.modelloTabella.appendRow([QStandardItem(pagamento.getId()), QStandardItem(pagamento.getCliente().getCodiceFiscale()), QStandardItem(pagamento.getData().toString("dd/MM/yyyy")), QStandardItem(pagamento.getOra().toString("HH:mm:ss")), QStandardItem(testo), QStandardItem(f"{pagamento.getImporto()} €"), QStandardItem(f"{pagamento.getImportoPunti()} punti")])

        self.ui.tableViewPagamenti.setModel(self.modelloTabella)
        self.ui.tableViewPagamenti.doubleClicked.connect(self.apriPagamento)

    def apriPagamento(self):

        gestorePagamenti = GestorePagamenti()

        riga = self.ui.tableViewPagamenti.selectionModel().currentIndex().row()
        pagamentoAmministratore = gestorePagamenti.getListaPagamenti()[riga]

        self.goVistaVisualizzaPagamentoAmministratore(pagamentoAmministratore)
