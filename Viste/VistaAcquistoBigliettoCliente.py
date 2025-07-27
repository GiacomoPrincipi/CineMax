from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QTime
from ui_VistaAcquistoBigliettoCliente import Ui_VistaAcquistoBigliettoCliente
from Gestione.GestoreClienti import GestoreClienti
from Gestione.GestoreBiglietti import GestoreBiglietti
from Gestione.GestorePagamenti import GestorePagamenti
from Gestione.GestorePunti import GestorePunti
from Sistema.Pagamento import Pagamento
from Sistema.Biglietto import Biglietto

class VistaAcquistoBigliettoCliente(QWidget):
    def __init__(self, statoLogin, goVistaVisualizzaSpettacoloCliente, goVistaVisualizzaPagamentoCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaAcquistoBigliettoCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaSpettacoloCliente = goVistaVisualizzaSpettacoloCliente
        self.goVistaVisualizzaPagamentoCliente = goVistaVisualizzaPagamentoCliente

        self.ui.pushButtonAnnulla.clicked.connect(self.annulla)
        self.ui.pushButtonAcquista.clicked.connect(self.conferma)

        opzioniTipo = [" ", "Adulto", "Ridotto"]
        self.ui.comboBoxTipo.addItems(opzioniTipo)

        opzioniTipoPagamento = [" ", "Normale", "Punti"]
        self.ui.comboBoxTipoPagamento.addItems(opzioniTipoPagamento)

    def showEvent(self, event):
        super().showEvent(event)

        biglietto = self.bigliettoCliente

        self.ui.labelPostoBiglietto.setText(str(biglietto.getPosto()))
        self.ui.comboBoxTipo.setCurrentIndex(0)
        self.ui.comboBoxTipoPagamento.setCurrentIndex(0)
        self.ui.labelPrezzoBiglietto.setText(str(biglietto.getPrezzo()))
        self.ui.labelPrezzoPuntiBiglietto.setText(str(biglietto.getPrezzoPunti()))
        self.ui.labelPuntiCliente.setText(str(self.statoLogin.clienteAutenticato.getPunti()))

        self.ui.labelErroreTipo.setText("")
        self.ui.labelErroreTipoPagamento.setText("")
        self.ui.labelErrorePuntiInsufficenti.setText("")

    def annulla(self):

        gestoreBiglietti = GestoreBiglietti()
        for biglietto in gestoreBiglietti.getListaBiglietti():
            if biglietto.getSpettacolo().getId() == self.bigliettoCliente.getSpettacolo().getId():
                spettacoloCliente = biglietto.getSpettacolo()

        self.goVistaVisualizzaSpettacoloCliente(spettacoloCliente)

    def conferma(self):
        self.ui.labelErroreTipo.setText("")
        self.ui.labelErroreTipoPagamento.setText("")
        self.ui.labelErrorePuntiInsufficenti.setText("")

        biglietto = self.bigliettoCliente

        prezzoRidotto = biglietto.getPrezzo() / 2
        prezzoPuntiRidotto = biglietto.getPrezzoPunti() / 2

        esito = False

        if self.ui.comboBoxTipo.currentIndex() == 0:
            self.ui.labelErroreTipo.setText("inserisci il tipo di biglietto!")
            esito = True

        if self.ui.comboBoxTipoPagamento.currentIndex() == 0:
            self.ui.labelErroreTipoPagamento.setText("inserisci il metodo di pagamento!")
            esito = True

        if self.ui.comboBoxTipo.currentText() == "Ridotto":
            if self.ui.comboBoxTipoPagamento.currentText() == "Punti":
                if not GestorePunti.controlloPuntiPunti(self.statoLogin.clienteAutenticato, prezzoPuntiRidotto):
                    self.ui.labelErrorePuntiInsufficenti.setText("punti non sufficenti")
                    esito = True
        if self.ui.comboBoxTipo.currentText() == "Adulto":
            if self.ui.comboBoxTipoPagamento.currentText() == "Punti":
                if not GestorePunti.controlloPunti(self.statoLogin.clienteAutenticato, biglietto):
                    self.ui.labelErrorePuntiInsufficenti.setText("punti non sufficenti")
                    esito = True

        if esito:
            return

        gestorePagamenti = GestorePagamenti()

        gestoreClienti =  GestoreClienti()

        tipo = self.ui.comboBoxTipo.currentText()

        id = gestorePagamenti.generaIdPagamento()
        data = QDate.currentDate()
        ora = QTime.currentTime()
        tipoPagamento = self.ui.comboBoxTipoPagamento.currentText()

        if self.ui.comboBoxTipo.currentText() == "Ridotto":
            if self.ui.comboBoxTipoPagamento.currentText() == "Punti":
                importo = 0
                importoPunti = prezzoPuntiRidotto
                GestorePunti.rimuoviPunti(self.statoLogin.clienteAutenticato, importoPunti)
            else:
                importo = prezzoRidotto
                importoPunti = 0
        else:
            if self.ui.comboBoxTipoPagamento.currentText() == "Punti":
                importo = 0
                importoPunti = biglietto.getPrezzoPunti()
                GestorePunti.rimuoviPunti(self.statoLogin.clienteAutenticato, importoPunti)
            else:
                importo = biglietto.getPrezzo()
                importoPunti = 0

        pagamento = Pagamento(self.statoLogin.clienteAutenticato, id, data, ora, biglietto, tipoPagamento, importo, importoPunti)
        gestorePagamenti.inserisciPagamento(pagamento)

        if self.ui.comboBoxTipoPagamento.currentText() == "Normale":
            puntiDaAggiungere = GestorePunti.calcoloPunti(biglietto.getPrezzo())
            GestorePunti.aggiungiPunti(self.statoLogin.clienteAutenticato, puntiDaAggiungere)

        if self.ui.comboBoxTipoPagamento.currentText() == "Ridotto":
            puntiDaAggiungere = GestorePunti.calcoloPunti(prezzoRidotto)
            GestorePunti.aggiungiPunti(self.statoLogin.clienteAutenticato, puntiDaAggiungere)

        for clienteNellaLista in gestoreClienti.listaClienti:
            if clienteNellaLista.getCodiceFiscale() == self.statoLogin.clienteAutenticato.getCodiceFiscale():
                clienteNellaLista.setPunti(self.statoLogin.clienteAutenticato.getPunti())
                self.statoLogin.loginCliente(clienteNellaLista)

        gestoreClienti.salvaDatiClienti()

        gestoreBiglietti = GestoreBiglietti()

        for bigliettoNellaLista in gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(biglietto.getSpettacolo()):
            if bigliettoNellaLista.getId() == biglietto.getId():
                bigliettoNellaLista.setTipo(tipo)
                bigliettoNellaLista.setDisponibile(False)

        gestoreBiglietti.salvaDatiBiglietti()

        self.goVistaVisualizzaPagamentoCliente(pagamento)
