from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from Viste.ui_VistaVisualizzaAmministratoriAmministratore import Ui_VistaVisualizzaAmministratoriAmministratore
from Gestione.GestoreAmministratori import GestoreAmministratori

class VistaVisualizzaAmministratoriAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaAmministratoreAmministratore, goVistaInserisciAmministratoreAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaAmministratoriAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaAmministratoreAmministratore = goVistaVisualizzaAmministratoreAmministratore

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.pushButtonInserisci.clicked.connect(goVistaInserisciAmministratoreAmministratore)

        self.ui.tableViewAmministratori.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewAmministratori.horizontalHeader().setFixedHeight(25)
        self.ui.tableViewAmministratori.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.ui.tableViewAmministratori.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.tableViewAmministratori.verticalScrollBar().setValue(self.ui.tableViewAmministratori.verticalScrollBar().minimum())

        gestoreAmministratori = GestoreAmministratori()

        self.modelloTabella = QStandardItemModel()
        self.modelloTabella.setHorizontalHeaderLabels(["Matricola:", "Nome:", "Cognome:","Data di Nascita:", "Email:", "Telefono:"])

        for amministratore in gestoreAmministratori.getListaAmministratori():
            self.modelloTabella.appendRow([QStandardItem(amministratore.getMatricola()), QStandardItem(amministratore.getNome()), QStandardItem(amministratore.getCognome()), QStandardItem(amministratore.getDataNascita().toString("dd/MM/yyyy")), QStandardItem(amministratore.getEmail()), QStandardItem(amministratore.getTelefono())])

        self.ui.tableViewAmministratori.setModel(self.modelloTabella)
        self.ui.tableViewAmministratori.doubleClicked.connect(self.apriAmministratore)

    def apriAmministratore(self):

        gestoreAmministratori = GestoreAmministratori()

        riga = self.ui.tableViewAmministratori.selectionModel().currentIndex().row()
        amministratoreAmministratore = gestoreAmministratori.getListaAmministratori()[riga]

        self.goVistaVisualizzaAmministratoreAmministratore(amministratoreAmministratore)
