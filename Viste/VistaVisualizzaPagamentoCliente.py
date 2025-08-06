from PySide6.QtWidgets import QWidget
from Viste.ui_VistaVisualizzaPagamentoCliente import Ui_VistaVisualizzaPagamentoCliente
from Sistema.Biglietto import Biglietto
from Sistema.Prodotto import Prodotto

class VistaVisualizzaPagamentoCliente(QWidget):
    def __init__(self, statoLogin, goVistaHomeCliente, goVistaVisualizzaPagamentiCliente, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaPagamentoCliente()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.ui.labelHomeButton.clicked.connect(goVistaHomeCliente)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaPagamentiCliente)

    def showEvent(self, event):
        super().showEvent(event)

        pagamentoCliente = self.pagamentoCliente

        if isinstance(pagamentoCliente.getArticolo(), Biglietto):
            testo = pagamentoCliente.getArticolo().getSpettacolo().getId()
        elif isinstance(pagamentoCliente.getArticolo(), Prodotto):
            testo = pagamentoCliente.getArticolo().getId()

        self.ui.labelIdArticoloPagamento.setText(testo)
        self.ui.labelIdPagamento.setText(pagamentoCliente.getId())
        self.ui.labelDataPagamento.setText(pagamentoCliente.getData().toString("dd/MM/yyyy"))
        self.ui.labelOraPagamento.setText(pagamentoCliente.getOra().toString("HH:mm:ss"))
        self.ui.labelTipoPagamento.setText(pagamentoCliente.getTipo())
        self.ui.labelImportoPagamento.setText(f"{pagamentoCliente.getImporto()} €")
        self.ui.labelImportoPuntiPagamento.setText(f"{pagamentoCliente.getImportoPunti()} Punti")
