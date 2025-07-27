from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QTime
from ui_VistaModificaRecensioneCliente import Ui_VistaModificaRecensioneCliente
from Gestione.GestoreRecensioni import GestoreRecensioni

class VistaModificaRecensioneCliente(QWidget):
    def __init__(self, statoLogin, goVistaVisualizzaRecensioneCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaModificaRecensioneCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaRecensioneCliente = goVistaVisualizzaRecensioneCliente

        self.ui.pushButtonAnnulla.clicked.connect(self.annulla)
        self.ui.pushButtonConferma.clicked.connect(self.conferma)


        opzioni = [" ", "0", "1", "2", "3", "4", "5"]
        self.ui.comboBoxStelle.addItems(opzioni)

    def showEvent(self, event):
        super().showEvent(event)

        recensione = self.recensioneCliente

        self.ui.comboBoxStelle.setCurrentText(recensione.getStelle())
        self.ui.textEditTesto.setText(recensione.getTesto())

        self.ui.labelErroreStelle.setText("")
        self.ui.labelErroreTesto.setText("")

    def annulla(self):
        self.goVistaVisualizzaRecensioneCliente(self.recensioneCliente)

    def conferma(self):
        self.ui.labelErroreStelle.setText("")
        self.ui.labelErroreTesto.setText("")

        stelle = self.ui.comboBoxStelle.currentText()
        testo = self.ui.textEditTesto.toPlainText()
        data = QDate.currentDate()
        ora = QTime.currentTime()

        gestoreRecensioni = GestoreRecensioni()

        if self.ui.comboBoxStelle.currentIndex() == 0 or testo == "":
            if self.ui.comboBoxStelle.currentIndex() == 0:
                self.ui.labelErroreStelle.setText("Inserisci la valutazione!")
            if testo == "":
                self.ui.labelErroreTesto.setText("Inserisci il testo!")

            return

        recensione = self.recensioneCliente

        id = recensione.getId()

        gestoreRecensioni = GestoreRecensioni()

        for recensioneNellaLista in gestoreRecensioni.getListaRecensioniCliente(self.statoLogin.clienteAutenticato):
            if recensione.getId() == recensioneNellaLista.getId():
                recensioneNellaLista.setInfoRecensione(self.statoLogin.clienteAutenticato, id, data, ora, stelle, testo)
                recensione = recensioneNellaLista

        gestoreRecensioni.salvaDatiRecensioni()


        self.goVistaVisualizzaRecensioneCliente(recensione)
