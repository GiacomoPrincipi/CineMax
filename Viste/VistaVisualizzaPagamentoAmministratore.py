from PySide6.QtWidgets import QWidget
from ui_VistaVisualizzaPagamentoAmministratore import Ui_VistaVisualizzaPagamentoAmministratore
from Sistema.Biglietto import Biglietto
from Sistema.Prodotto import Prodotto

class VistaVisualizzaPagamentoAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaRegistroCassaAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaPagamentoAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.ui.labelHomeButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaRegistroCassaAmministratore)

    def showEvent(self, event):
        super().showEvent(event)

        pagamentoAmministratore = self.pagamentoAmministratore

        if isinstance(pagamentoAmministratore.getArticolo(), Biglietto):
            testo = pagamentoAmministratore.getArticolo().getSpettacolo().getTitolo()
        elif isinstance(pagamentoAmministratore.getArticolo(), Prodotto):
            testo = pagamentoAmministratore.getArticolo().getNome()

        self.ui.labelCodiceFiscalePagamento.setText(pagamentoAmministratore.getCliente().getCodiceFiscale())
        self.ui.labelNomePagamento.setText(testo)
        self.ui.labelIdPagamento.setText(pagamentoAmministratore.getId())
        self.ui.labelDataPagamento.setText(pagamentoAmministratore.getData().toString("dd/MM/yyyy"))
        self.ui.labelOraPagamento.setText(pagamentoAmministratore.getOra().toString("HH:mm:ss"))
        self.ui.labelTipoPagamento.setText(pagamentoAmministratore.getTipo())
        self.ui.labelImportoPagamento.setText(f"{pagamentoAmministratore.getImporto()} €")
        self.ui.labelImportoPuntiPagamento.setText(f"{pagamentoAmministratore.getImportoPunti()} Punti")
