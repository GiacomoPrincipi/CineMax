from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QTime
from ui_VistaAcquistoProdottoCliente import Ui_VistaAcquistoProdottoCliente
from Gestione.GestorePagamenti import GestorePagamenti
from Gestione.GestoreClienti import GestoreClienti
from Gestione.GestorePunti import GestorePunti
from Sistema.Pagamento import Pagamento

class VistaAcquistoProdottoCliente(QWidget):
    def __init__(self, statoLogin, goVistaVisualizzaProdottoCliente, goVistaVisualizzaPagamentoCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaAcquistoProdottoCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaProdottoCliente = goVistaVisualizzaProdottoCliente
        self.goVistaVisualizzaPagamentoCliente = goVistaVisualizzaPagamentoCliente

        self.ui.pushButtonAnnulla.clicked.connect(self.annulla)
        self.ui.pushButtonAcquista.clicked.connect(self.conferma)

        opzioni = [" ", "Normale", "Punti"]
        self.ui.comboBoxTipoPagamento.addItems(opzioni)

    def showEvent(self, event):
        super().showEvent(event)

        prodottoCliente = self.prodottoCliente

        self.ui.labelPrezzoProdotto.setText(str(prodottoCliente.getPrezzo()))
        self.ui.labelPrezzoPuntiProdotto.setText(str(prodottoCliente.getPrezzoPunti()))
        self.ui.comboBoxTipoPagamento.setCurrentIndex(0)
        self.ui.labelPuntiCliente.setText(str(self.statoLogin.clienteAutenticato.getPunti()))

        self.ui.labelErroreTipoPagamento.setText("")
        self.ui.labelErrorePuntiInsufficenti.setText("")

    def annulla(self):
        self.goVistaVisualizzaProdottoCliente(self.prodottoCliente)

    def conferma(self):
        self.ui.labelErroreTipoPagamento.setText("")
        self.ui.labelErrorePuntiInsufficenti.setText("")

        prodottoCliente = self.prodottoCliente

        esito = False

        if self.ui.comboBoxTipoPagamento.currentIndex() == 0:
            self.ui.labelErroreTipoPagamento.setText("Inserisci il metodo di pagamento!")
            esito = True


        if self.ui.comboBoxTipoPagamento.currentText() == "Punti":
            if not GestorePunti.controlloPunti(self.statoLogin.clienteAutenticato, prodottoCliente):
                self.ui.labelErrorePuntiInsufficenti.setText("Punti non sufficenti!")
                esito = True


        if esito: return

        gestorePagamenti = GestorePagamenti()
        gestoreClienti =  GestoreClienti()

        id = gestorePagamenti.generaIdPagamento()
        data = QDate.currentDate()
        ora = QTime.currentTime()
        tipo = self.ui.comboBoxTipoPagamento.currentText()

        if self.ui.comboBoxTipoPagamento.currentText() == "Punti":
            importo = 0
            importoPunti = prodottoCliente.getPrezzoPunti()
            GestorePunti.rimuoviPunti(self.statoLogin.clienteAutenticato, importoPunti)
        else:
            importo = prodottoCliente.getPrezzo()
            importoPunti = 0

        pagamento = Pagamento(self.statoLogin.clienteAutenticato, id, data, ora, prodottoCliente, tipo, importo, importoPunti)
        gestorePagamenti.inserisciPagamento(pagamento)

        if self.ui.comboBoxTipoPagamento.currentText() == "Normale":
            puntiDaAggiungere = GestorePunti.calcoloPunti(prodottoCliente.getPrezzo())
            GestorePunti.aggiungiPunti(self.statoLogin.clienteAutenticato, puntiDaAggiungere)

        for clienteNellaLista in gestoreClienti.listaClienti:
            if clienteNellaLista.getCodiceFiscale() == self.statoLogin.clienteAutenticato.getCodiceFiscale():
                clienteNellaLista.setPunti(self.statoLogin.clienteAutenticato.getPunti())
                self.statoLogin.loginCliente(clienteNellaLista)

        gestoreClienti.salvaDatiClienti()

        self.goVistaVisualizzaPagamentoCliente(pagamento)
