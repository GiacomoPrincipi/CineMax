from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from ui_VistaVisualizzaClienteAmministratore import Ui_VistaVisualizzaClienteAmministratore
from Gestione.GestorePagamenti import GestorePagamenti
from Gestione.GestoreRecensioni import GestoreRecensioni

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

        clienteAmministratore = self.clienteAmministratore
        gestorePagamenti = GestorePagamenti()
        gestoreRecensioni = GestoreRecensioni()

        self.ui.labelNomeCliente.setText(clienteAmministratore.nome)
        self.ui.labelCognomeCliente.setText(clienteAmministratore.cognome)
        self.ui.labelDataNascitaCliente.setText(clienteAmministratore.dataNascita.toString("dd/MM/yyyy"))
        self.ui.labelEmailCliente.setText(clienteAmministratore.email)
        self.ui.labelTelefonoCliente.setText(str(clienteAmministratore.telefono))
        self.ui.labelCodiceFiscaleCliente.setText(clienteAmministratore.codiceFiscale)
        self.ui.labelPuntiCliente.setText(str(clienteAmministratore.punti))

        self.modelloTabellaPagamentiCliente = QStandardItemModel()
        self.modelloTabellaPagamentiCliente.setHorizontalHeaderLabels(["Data:", "Ora:", "Articolo:", "Tipo:", "Importo"])

        for pagamento in gestorePagamenti.getListaPagamentiCliente(clienteAmministratore):
           self.modelloTabellaPagamentiCliente.appendRow([QStandardItem(pagamento.getData().toString("dd/MM/yyyy")), QStandardItem(pagamento.getOra().toString("HH:mm:ss")), QStandardItem(pagamento.getArticolo().getNome()), QStandardItem(str(pagamento.getTipo())), QStandardItem(str(pagamento.getImporto()))])

        self.ui.tableViewPagamentiCliente.setModel(self.modelloTabellaPagamentiCliente)

        self.modelloTabellaRecensioniCliente = QStandardItemModel()
        self.modelloTabellaRecensioniCliente.setHorizontalHeaderLabels(["Data:", "Ora:", "Stelle:"])

        for recensione in gestoreRecensioni.getListaRecensioniCliente(clienteAmministratore):
           self.modelloTabellaRecensioniCliente.appendRow([QStandardItem(recensione.getData().toString("dd/MM/yyyy")), QStandardItem(recensione.getOra().toString("HH:mm:ss")), QStandardItem(str(recensione.getStelle()))])

        self.ui.tableViewRecensioniCliente.setModel(self.modelloTabellaRecensioniCliente)
