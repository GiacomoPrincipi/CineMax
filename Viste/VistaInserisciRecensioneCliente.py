from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QTime
from Viste.ui_VistaInserisciRecensioneCliente import Ui_VistaInserisciRecensioneCliente
from Gestione.GestoreRecensioni import GestoreRecensioni
from Sistema.Recensione import Recensione

class VistaInserisciRecensioneCliente(QWidget):
    def __init__(self, statoLogin, goVistaVisualizzaRecensioniCliente, goVistaVisualizzaRecensioneCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaInserisciRecensioneCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaRecensioneCliente = goVistaVisualizzaRecensioneCliente

        self.ui.pushButtonAnnulla.clicked.connect(goVistaVisualizzaRecensioniCliente)
        self.ui.pushButtonConferma.clicked.connect(self.conferma)

        opzioni = [" ", "0", "1", "2", "3", "4", "5"]
        self.ui.comboBoxStelle.addItems(opzioni)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.comboBoxStelle.setCurrentIndex(0)
        self.ui.textEditTesto.setText("")

        self.ui.labelErroreStelle.setText("")
        self.ui.labelErroreTesto.setText("")

    def conferma(self):
        self.ui.labelErroreStelle.setText("")
        self.ui.labelErroreTesto.setText("")

        stelle = self.ui.comboBoxStelle.currentText()
        testo = self.ui.textEditTesto.toPlainText()
        data = QDate.currentDate()
        ora = QTime.currentTime()

        gestoreRecensioni = GestoreRecensioni()

        id = gestoreRecensioni.generaIdRecensione()

        esito = False

        if self.ui.comboBoxStelle.currentIndex() == 0:
            self.ui.labelErroreStelle.setText("Inserisci la valutazione!")
            esito = True
        if testo == "":
            self.ui.labelErroreTesto.setText("Inserisci il testo!")
            esito = True

        if esito: return

        stelle = int(stelle)

        recensione = Recensione(self.statoLogin.clienteAutenticato, id, data, ora, stelle, testo)
        gestoreRecensioni.inserisciRecensione(recensione)

        self.goVistaVisualizzaRecensioneCliente(recensione)
