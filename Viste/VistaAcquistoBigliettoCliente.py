from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QTime
from Viste.ui_VistaAcquistoBigliettoCliente import Ui_VistaAcquistoBigliettoCliente
from Gestione.GestoreClienti import GestoreClienti
from Gestione.GestoreBiglietti import GestoreBiglietti
from Gestione.GestorePagamenti import GestorePagamenti
from Gestione.GestorePunti import GestorePunti
from Sistema.Pagamento import Pagamento

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

        bigliettoCliente = self.bigliettoCliente

        self.ui.labelPostoBiglietto.setText(str(bigliettoCliente.getPosto()))
        self.ui.comboBoxTipo.setCurrentIndex(0)
        self.ui.comboBoxTipoPagamento.setCurrentIndex(0)
        self.ui.labelPrezzoBiglietto.setText(str(bigliettoCliente.getPrezzo()))
        self.ui.labelPrezzoPuntiBiglietto.setText(str(bigliettoCliente.getPrezzoPunti()))
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

        bigliettoCliente = self.bigliettoCliente
        
        prezzoRidotto = bigliettoCliente.getPrezzo() / 2
        prezzoPuntiRidotto = bigliettoCliente.getPrezzoPunti() / 2

        esito = False

        if self.ui.comboBoxTipo.currentIndex() == 0:
            self.ui.labelErroreTipo.setText("Inserisci il tipo di biglietto!")
            esito = True

        if self.ui.comboBoxTipoPagamento.currentIndex() == 0:
            self.ui.labelErroreTipoPagamento.setText("Inserisci il metodo di pagamento!")
            esito = True

        if self.ui.comboBoxTipo.currentText() == "Ridotto":
            if self.ui.comboBoxTipoPagamento.currentText() == "Punti":
                if not GestorePunti.controlloPuntiPunti(self.statoLogin.clienteAutenticato, prezzoPuntiRidotto):
                    self.ui.labelErrorePuntiInsufficenti.setText("Punti non sufficenti!")
                    esito = True
        if self.ui.comboBoxTipo.currentText() == "Adulto":
            if self.ui.comboBoxTipoPagamento.currentText() == "Punti":
                if not GestorePunti.controlloPunti(self.statoLogin.clienteAutenticato, bigliettoCliente):
                    self.ui.labelErrorePuntiInsufficenti.setText("punti non sufficenti")
                    esito = True

        if esito: return

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
                importoPunti = bigliettoCliente.getPrezzoPunti()
                GestorePunti.rimuoviPunti(self.statoLogin.clienteAutenticato, importoPunti)
            else:
                importo = bigliettoCliente.getPrezzo()
                importoPunti = 0

        pagamento = Pagamento(self.statoLogin.clienteAutenticato, id, data, ora, bigliettoCliente, tipoPagamento, importo, importoPunti)
        gestorePagamenti.inserisciPagamento(pagamento)

        if self.ui.comboBoxTipoPagamento.currentText() == "Normale":
            puntiDaAggiungere = GestorePunti.calcoloPunti(bigliettoCliente.getPrezzo())
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

        for bigliettoNellaLista in gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(bigliettoCliente.getSpettacolo()):
            if bigliettoNellaLista.getId() == bigliettoCliente.getId():
                bigliettoNellaLista.setTipo(tipo)
                bigliettoNellaLista.setDisponibile(False)

        gestoreBiglietti.salvaDatiBiglietti()

        self.goVistaVisualizzaPagamentoCliente(pagamento)
