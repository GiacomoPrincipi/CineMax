from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from ui_VistaVisualizzaClienteAmministratore import Ui_VistaVisualizzaClienteAmministratore
from Gestione.GestorePagamenti import GestorePagamenti
from Gestione.GestoreRecensioni import GestoreRecensioni
from Sistema.Biglietto import Biglietto
from Sistema.Prodotto import Prodotto

class VistaVisualizzaClienteAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaClientiAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaClienteAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.ui.labelHomeButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaClientiAmministratore)

        self.ui.tableViewPagamentiCliente.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewPagamentiCliente.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewPagamentiCliente.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.ui.tableViewPagamentiCliente.setEditTriggers(QAbstractItemView.NoEditTriggers)


        self.ui.tableViewRecensioniCliente.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewRecensioniCliente.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewRecensioniCliente.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.ui.tableViewRecensioniCliente.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.tableViewPagamentiCliente.verticalScrollBar().setValue(self.ui.tableViewPagamentiCliente.verticalScrollBar().minimum())
        self.ui.tableViewRecensioniCliente.verticalScrollBar().setValue(self.ui.tableViewRecensioniCliente.verticalScrollBar().minimum())

        clienteAmministratore = self.clienteAmministratore
        gestorePagamenti = GestorePagamenti()
        gestoreRecensioni = GestoreRecensioni()

        self.ui.labelNomeCliente.setText(clienteAmministratore.getNome())
        self.ui.labelCognomeCliente.setText(clienteAmministratore.getCognome())
        self.ui.labelDataNascitaCliente.setText(clienteAmministratore.getDataNascita().toString("dd/MM/yyyy"))
        self.ui.labelEmailCliente.setText(clienteAmministratore.getEmail())
        self.ui.labelTelefonoCliente.setText(str(clienteAmministratore.getTelefono()))
        self.ui.labelCodiceFiscaleCliente.setText(clienteAmministratore.getCodiceFiscale())
        self.ui.labelPuntiCliente.setText(str(clienteAmministratore.getPunti()))

        self.modelloTabellaPagamentiCliente = QStandardItemModel()
        self.modelloTabellaPagamentiCliente.setHorizontalHeaderLabels(["Data:", "Ora:", "Articolo:", "Tipo:", "Importo", "ImportoPunti:"])

        for pagamento in gestorePagamenti.getListaPagamentiCliente(clienteAmministratore):
            if isinstance(pagamento.getArticolo(), Biglietto):
                testo = pagamento.getArticolo().getSpettacolo().getTitolo()
            elif isinstance(pagamento.getArticolo(), Prodotto):
                testo = pagamento.getArticolo().getNome()
            self.modelloTabellaPagamentiCliente.appendRow([QStandardItem(pagamento.getData().toString("dd/MM/yyyy")), QStandardItem(pagamento.getOra().toString("HH:mm:ss")), QStandardItem(testo), QStandardItem(pagamento.getTipo()), QStandardItem(f"{pagamento.getImporto()} €"), QStandardItem(f"{pagamento.getImportoPunti()} punti")])

        self.ui.tableViewPagamentiCliente.setModel(self.modelloTabellaPagamentiCliente)

        self.modelloTabellaRecensioniCliente = QStandardItemModel()
        self.modelloTabellaRecensioniCliente.setHorizontalHeaderLabels(["Data:", "Ora:", "Stelle:", "Testo:"])

        for recensione in gestoreRecensioni.getListaRecensioniCliente(clienteAmministratore):
           self.modelloTabellaRecensioniCliente.appendRow([QStandardItem(recensione.getData().toString("dd/MM/yyyy")), QStandardItem(recensione.getOra().toString("HH:mm:ss")), QStandardItem(f"{recensione.getStelle()}/5"), QStandardItem(recensione.getTesto())])

        self.ui.tableViewRecensioniCliente.setModel(self.modelloTabellaRecensioniCliente)
