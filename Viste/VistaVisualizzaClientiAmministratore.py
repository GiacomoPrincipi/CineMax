from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from ui_VistaVisualizzaClientiAmministratore import Ui_VistaVisualizzaClientiAmministratore
from Gestione.GestoreClienti import GestoreClienti

class VistaVisualizzaClientiAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaClienteAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaClientiAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaClienteAmministratore = goVistaVisualizzaClienteAmministratore

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeAmministratore)

        self.ui.tableViewClienti.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewClienti.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewClienti.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.ui.tableViewClienti.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.tableViewClienti.verticalScrollBar().setValue(self.ui.tableViewClienti.verticalScrollBar().minimum())

        gestoreClienti = GestoreClienti()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Codice Fiscale:", "Nome:", "Cognome:", "Data di Nascita:", "Email:", "Telefono:"])

        for cliente in gestoreClienti.getListaClienti():
            self.modelloTabella.appendRow([QStandardItem(cliente.getCodiceFiscale()), QStandardItem(cliente.getNome()), QStandardItem(cliente.getCognome()), QStandardItem(cliente.getDataNascita().toString("dd/MM/yyyy")), QStandardItem(cliente.getEmail()), QStandardItem(cliente.getTelefono())])

        self.ui.tableViewClienti.setModel(self.modelloTabella)
        self.ui.tableViewClienti.doubleClicked.connect(self.apriCliente)

    def apriCliente(self):

        gestoreClienti = GestoreClienti()

        riga = self.ui.tableViewClienti.selectionModel().currentIndex().row()
        clienteAmministratore = gestoreClienti.getListaClienti()[riga]

        self.goVistaVisualizzaClienteAmministratore(clienteAmministratore)
