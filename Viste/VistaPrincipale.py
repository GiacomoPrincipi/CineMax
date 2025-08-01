from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtGui import QIcon

from Viste.VistaHome import VistaHome

from Viste.VistaLoginAmministratore import VistaLoginAmministratore
from Viste.VistaHomeAmministratore import VistaHomeAmministratore
from Viste.VistaVisualizzaProfiloPersonaleAmministratore import VistaVisualizzaProfiloPersonaleAmministratore
from Viste.VistaModificaProfiloPersonaleAmministratore import VistaModificaProfiloPersonaleAmministratore
from Viste.VistaVisualizzaSpettacoliAmministratore import VistaVisualizzaSpettacoliAmministratore
from Viste.VistaVisualizzaSpettacoloAmministratore import VistaVisualizzaSpettacoloAmministratore
from Viste.VistaInserisciSpettacoloAmministratore import VistaInserisciSpettacoloAmministratore
from Viste.VistaModificaSpettacoloAmministratore import VistaModificaSpettacoloAmministratore
from Viste.VistaVisualizzaProdottiAmministratore import VistaVisualizzaProdottiAmministratore
from Viste.VistaVisualizzaProdottoAmministratore import VistaVisualizzaProdottoAmministratore
from Viste.VistaInserisciProdottoAmministratore import VistaInserisciProdottoAmministratore
from Viste.VistaModificaProdottoAmministratore import VistaModificaProdottoAmministratore
from Viste.VistaVisualizzaRegistroCassaAmministratore import VistaVisualizzaRegistroCassaAmministratore
from Viste.VistaVisualizzaPagamentoAmministratore import VistaVisualizzaPagamentoAmministratore
from Viste.VistaVisualizzaRecensioniAmministratore import VistaVisualizzaRecensioniAmministratore
from Viste.VistaVisualizzaRecensioneAmministratore import VistaVisualizzaRecensioneAmministratore
from Viste.VistaVisualizzaAmministratoriAmministratore import VistaVisualizzaAmministratoriAmministratore
from Viste.VistaVisualizzaAmministratoreAmministratore import VistaVisualizzaAmministratoreAmministratore
from Viste.VistaInserisciAmministratoreAmministratore import VistaInserisciAmministratoreAmministratore
from Viste.VistaVisualizzaClientiAmministratore import VistaVisualizzaClientiAmministratore
from Viste.VistaVisualizzaClienteAmministratore import VistaVisualizzaClienteAmministratore

from Viste.VistaLoginCliente import VistaLoginCliente
from Viste.VistaRegistrazioneCliente import VistaRegistrazioneCliente
from Viste.VistaHomeCliente import VistaHomeCliente
from Viste.VistaVisualizzaProfiloPersonaleCliente import VistaVisualizzaProfiloPersonaleCliente
from Viste.VistaModificaProfiloPersonaleCliente import VistaModificaProfiloPersonaleCliente
from Viste.VistaVisualizzaSpettacoliCliente import VistaVisualizzaSpettacoliCliente
from Viste.VistaVisualizzaSpettacoloCliente import VistaVisualizzaSpettacoloCliente
from Viste.VistaAcquistoBigliettoCliente import VistaAcquistoBigliettoCliente
from Viste.VistaVisualizzaProdottiCliente import VistaVisualizzaProdottiCliente
from Viste.VistaVisualizzaProdottoCliente import VistaVisualizzaProdottoCliente
from Viste.VistaAcquistoProdottoCliente import VistaAcquistoProdottoCliente
from Viste.VistaVisualizzaPagamentiCliente import VistaVisualizzaPagamentiCliente
from Viste.VistaVisualizzaPagamentoCliente import VistaVisualizzaPagamentoCliente
from Viste.VistaVisualizzaRecensioniCliente import VistaVisualizzaRecensioniCliente
from Viste.VistaVisualizzaRecensioneCliente import VistaVisualizzaRecensioneCliente
from Viste.VistaInserisciRecensioneCliente import VistaInserisciRecensioneCliente
from Viste.VistaModificaRecensioneCliente import VistaModificaRecensioneCliente

class VistaPrincipale(QMainWindow):
    def __init__(self, statoLogin, parent = None):
        super().__init__(parent)

        self.setFixedSize(790, 499)
        self.setWindowTitle("Home - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaHome.ico"))

        self.vistaHome = VistaHome(statoLogin, self.goVistaLoginAmministratore, self.goVistaLoginCliente)

        self.vistaLoginAmministratore = VistaLoginAmministratore(statoLogin, self.goVistaHome, self.goVistaHomeAmministratore)
        self.vistaHomeAmministratore = VistaHomeAmministratore(statoLogin, self.goVistaHome, self.goVistaVisualizzaProfiloPersonaleAmministratore, self.goVistaVisualizzaSpettacoliAmministratore, self.goVistaVisualizzaProdottiAmministratore, self.goVistaVisualizzaRegistroCassaAmministratore, self.goVistaVisualizzaRecensioniAmministratore, self.goVistaVisualizzaAmministratoriAmministratore, self.goVistaVisualizzaClientiAmministratore)
        self.vistaVisualizzaProfiloPersonaleAmministratore = VistaVisualizzaProfiloPersonaleAmministratore(statoLogin, self.goVistaHome, self.goVistaHomeAmministratore, self.goVistaModificaProfiloPersonaleAmministratore)
        self.vistaModificaProfiloPersonaleAmministratore = VistaModificaProfiloPersonaleAmministratore(statoLogin, self.goVistaVisualizzaProfiloPersonaleAmministratore)
        self.vistaVisualizzaSpettacoliAmministratore = VistaVisualizzaSpettacoliAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaSpettacoloAmministratore, self.goVistaInserisciSpettacoloAmministratore)
        self.vistaVisualizzaSpettacoloAmministratore = VistaVisualizzaSpettacoloAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaSpettacoliAmministratore, self.goVistaModificaSpettacoloAmministratore)
        self.vistaInserisciSpettacoloAmministratore = VistaInserisciSpettacoloAmministratore(statoLogin, self.goVistaVisualizzaSpettacoliAmministratore, self.goVistaVisualizzaSpettacoloAmministratore)
        self.vistaModificaSpettacoloAmministratore = VistaModificaSpettacoloAmministratore(statoLogin, self.goVistaVisualizzaSpettacoloAmministratore)
        self.vistaVisualizzaProdottiAmministratore = VistaVisualizzaProdottiAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaProdottoAmministratore, self.goVistaInserisciProdottoAmministratore)
        self.vistaVisualizzaProdottoAmministratore = VistaVisualizzaProdottoAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaProdottiAmministratore, self.goVistaModificaProdottoAmministratore)
        self.vistaInserisciProdottoAmministratore = VistaInserisciProdottoAmministratore(statoLogin, self.goVistaVisualizzaProdottiAmministratore, self.goVistaVisualizzaProdottoAmministratore)
        self.vistaModificaProdottoAmministratore = VistaModificaProdottoAmministratore(statoLogin, self.goVistaVisualizzaProdottoAmministratore)
        self.vistaVisualizzaRegistroCassaAmministratore = VistaVisualizzaRegistroCassaAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaPagamentoAmministratore)
        self.vistaVisualizzaPagamentoAmministratore = VistaVisualizzaPagamentoAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaRegistroCassaAmministratore)
        self.vistaVisualizzaRecensioniAmministratore = VistaVisualizzaRecensioniAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaRecensioneAmministratore)
        self.vistaVisualizzaRecensioneAmministratore = VistaVisualizzaRecensioneAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaRecensioniAmministratore)
        self.vistaVisualizzaAmministratoriAmministratore = VistaVisualizzaAmministratoriAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaAmministratoreAmministratore, self.goVistaInserisciAmministratoreAmministratore)
        self.vistaVisualizzaAmministratoreAmministratore = VistaVisualizzaAmministratoreAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaAmministratoriAmministratore)
        self.vistaInserisciAmministratoreAmministratore = VistaInserisciAmministratoreAmministratore(statoLogin, self.goVistaVisualizzaAmministratoriAmministratore)
        self.vistaVisualizzaClientiAmministratore = VistaVisualizzaClientiAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaClienteAmministratore)
        self.vistaVisualizzaClienteAmministratore = VistaVisualizzaClienteAmministratore(statoLogin, self.goVistaHomeAmministratore, self.goVistaVisualizzaClientiAmministratore)

        self.vistaLoginCliente = VistaLoginCliente(statoLogin, self.goVistaHome, self.goVistaRegistrazioneCliente, self.goVistaHomeCliente)
        self.vistaRegistrazioneCliente = VistaRegistrazioneCliente(statoLogin, self.goVistaLoginCliente, self.goVistaHomeCliente)
        self.vistaHomeCliente = VistaHomeCliente(statoLogin, self.goVistaHome, self.goVistaVisualizzaProfiloPersonaleCliente, self.goVistaVisualizzaSpettacoliCliente, self.goVistaVisualizzaProdottiCliente, self.goVistaVisualizzaPagamentiCliente, self.goVistaVisualizzaRecensioniCliente)
        self.vistaVisualizzaProfiloPersonaleCliente = VistaVisualizzaProfiloPersonaleCliente(statoLogin, self.goVistaHome, self.goVistaHomeCliente, self.goVistaModificaProfiloPersonaleCliente)
        self.vistaModificaProfiloPersonaleCliente = VistaModificaProfiloPersonaleCliente(statoLogin, self.goVistaVisualizzaProfiloPersonaleCliente)
        self.vistaVisualizzaSpettacoliCliente = VistaVisualizzaSpettacoliCliente(statoLogin, self.goVistaHomeCliente, self.goVistaVisualizzaSpettacoloCliente)
        self.vistaVisualizzaSpettacoloCliente = VistaVisualizzaSpettacoloCliente(statoLogin, self.goVistaHomeCliente, self.goVistaVisualizzaSpettacoliCliente, self.goVistaAcquistoBigliettoCliente)
        self.vistaAcquistoBigliettoCliente = VistaAcquistoBigliettoCliente(statoLogin, self.goVistaVisualizzaSpettacoloCliente, self.goVistaVisualizzaPagamentoCliente)
        self.vistaVisualizzaProdottiCliente = VistaVisualizzaProdottiCliente(statoLogin, self.goVistaHomeCliente, self.goVistaVisualizzaProdottoCliente)
        self.vistaVisualizzaProdottoCliente = VistaVisualizzaProdottoCliente(statoLogin, self.goVistaHomeCliente, self.goVistaVisualizzaProdottiCliente, self.goVistaAcquistoProdottoCliente)
        self.vistaAcquistoProdottoCliente = VistaAcquistoProdottoCliente(statoLogin, self.goVistaVisualizzaProdottoCliente, self.goVistaVisualizzaPagamentoCliente)
        self.vistaVisualizzaPagamentiCliente = VistaVisualizzaPagamentiCliente(statoLogin, self.goVistaHomeCliente, self.goVistaVisualizzaPagamentoCliente)
        self.vistaVisualizzaPagamentoCliente = VistaVisualizzaPagamentoCliente(statoLogin, self.goVistaHomeCliente, self.goVistaVisualizzaPagamentiCliente)
        self.vistaVisualizzaRecensioniCliente = VistaVisualizzaRecensioniCliente(statoLogin, self.goVistaHomeCliente, self.goVistaVisualizzaRecensioneCliente, self.goVistaInserisciRecensioneCliente)
        self.vistaVisualizzaRecensioneCliente = VistaVisualizzaRecensioneCliente(statoLogin, self.goVistaHomeCliente, self.goVistaVisualizzaRecensioniCliente, self.goVistaModificaRecensioneCliente)
        self.vistaInserisciRecensioneCliente = VistaInserisciRecensioneCliente(statoLogin, self.goVistaVisualizzaRecensioniCliente, self.goVistaVisualizzaRecensioneCliente)
        self.vistaModificaRecensioneCliente = VistaModificaRecensioneCliente(statoLogin, self.goVistaVisualizzaRecensioneCliente)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.vistaHome)

        self.stack.addWidget(self.vistaLoginAmministratore)
        self.stack.addWidget(self.vistaHomeAmministratore)
        self.stack.addWidget(self.vistaVisualizzaProfiloPersonaleAmministratore)
        self.stack.addWidget(self.vistaModificaProfiloPersonaleAmministratore)
        self.stack.addWidget(self.vistaVisualizzaSpettacoliAmministratore)
        self.stack.addWidget(self.vistaVisualizzaSpettacoloAmministratore)
        self.stack.addWidget(self.vistaInserisciSpettacoloAmministratore)
        self.stack.addWidget(self.vistaModificaSpettacoloAmministratore)
        self.stack.addWidget(self.vistaVisualizzaProdottiAmministratore)
        self.stack.addWidget(self.vistaVisualizzaProdottoAmministratore)
        self.stack.addWidget(self.vistaInserisciProdottoAmministratore)
        self.stack.addWidget(self.vistaModificaProdottoAmministratore)
        self.stack.addWidget(self.vistaVisualizzaRegistroCassaAmministratore)
        self.stack.addWidget(self.vistaVisualizzaPagamentoAmministratore)
        self.stack.addWidget(self.vistaVisualizzaRecensioniAmministratore)
        self.stack.addWidget(self.vistaVisualizzaRecensioneAmministratore)
        self.stack.addWidget(self.vistaVisualizzaAmministratoriAmministratore)
        self.stack.addWidget(self.vistaVisualizzaAmministratoreAmministratore)
        self.stack.addWidget(self.vistaInserisciAmministratoreAmministratore)
        self.stack.addWidget(self.vistaVisualizzaClientiAmministratore)
        self.stack.addWidget(self.vistaVisualizzaClienteAmministratore)

        self.stack.addWidget(self.vistaLoginCliente)
        self.stack.addWidget(self.vistaRegistrazioneCliente)
        self.stack.addWidget(self.vistaHomeCliente)
        self.stack.addWidget(self.vistaVisualizzaProfiloPersonaleCliente)
        self.stack.addWidget(self.vistaModificaProfiloPersonaleCliente)
        self.stack.addWidget(self.vistaVisualizzaSpettacoliCliente)
        self.stack.addWidget(self.vistaVisualizzaSpettacoloCliente)
        self.stack.addWidget(self.vistaAcquistoBigliettoCliente)
        self.stack.addWidget(self.vistaVisualizzaProdottiCliente)
        self.stack.addWidget(self.vistaVisualizzaProdottoCliente)
        self.stack.addWidget(self.vistaAcquistoProdottoCliente)
        self.stack.addWidget(self.vistaVisualizzaPagamentiCliente)
        self.stack.addWidget(self.vistaVisualizzaPagamentoCliente)
        self.stack.addWidget(self.vistaVisualizzaRecensioniCliente)
        self.stack.addWidget(self.vistaVisualizzaRecensioneCliente)
        self.stack.addWidget(self.vistaInserisciRecensioneCliente)
        self.stack.addWidget(self.vistaModificaRecensioneCliente)

        self.setCentralWidget(self.stack)
        self.stack.setCurrentWidget(self.vistaHome)

    def goVistaHome(self):
        self.stack.setCurrentWidget(self.vistaHome)
        self.setWindowTitle("Home - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaHome.ico"))

    def goVistaLoginAmministratore(self):
        self.stack.setCurrentWidget(self.vistaLoginAmministratore)
        self.setWindowTitle("Login Amministratore - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaHomeAmministratore(self):
        self.stack.setCurrentWidget(self.vistaHomeAmministratore)
        self.setWindowTitle("Area Riservata Amministratore - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaProfiloPersonaleAmministratore(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaProfiloPersonaleAmministratore)
        self.setWindowTitle("Profilo Personale - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaModificaProfiloPersonaleAmministratore(self):
        self.stack.setCurrentWidget(self.vistaModificaProfiloPersonaleAmministratore)
        self.setWindowTitle("Modifica Profilo Personale - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaSpettacoliAmministratore(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaSpettacoliAmministratore)
        self.setWindowTitle("Spettacoli - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaSpettacoloAmministratore(self, spettacoloAmministratore):
        self.vistaVisualizzaSpettacoloAmministratore.spettacoloAmministratore = spettacoloAmministratore
        self.stack.setCurrentWidget(self.vistaVisualizzaSpettacoloAmministratore)
        self.setWindowTitle("Spettacolo - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaInserisciSpettacoloAmministratore(self):
        self.stack.setCurrentWidget(self.vistaInserisciSpettacoloAmministratore)
        self.setWindowTitle("Inserisci Spettacolo - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaModificaSpettacoloAmministratore(self, spettacoloAmministratore):
        self.vistaModificaSpettacoloAmministratore.spettacoloAmministratore = spettacoloAmministratore
        self.stack.setCurrentWidget(self.vistaModificaSpettacoloAmministratore)
        self.setWindowTitle("Modifica Spettacolo - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaProdottiAmministratore(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaProdottiAmministratore)
        self.setWindowTitle("Prodotti - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaProdottoAmministratore(self, prodottoAmministratore):
        self.vistaVisualizzaProdottoAmministratore.prodottoAmministratore = prodottoAmministratore
        self.stack.setCurrentWidget(self.vistaVisualizzaProdottoAmministratore)
        self.setWindowTitle("Prodotto - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaInserisciProdottoAmministratore(self):
        self.stack.setCurrentWidget(self.vistaInserisciProdottoAmministratore)
        self.setWindowTitle("Inserisci Prodotto - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaModificaProdottoAmministratore(self, prodottoAmministratore):
        self.vistaModificaProdottoAmministratore.prodottoAmministratore = prodottoAmministratore
        self.stack.setCurrentWidget(self.vistaModificaProdottoAmministratore)
        self.setWindowTitle("Modifica Prodotto - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaRegistroCassaAmministratore(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaRegistroCassaAmministratore)
        self.setWindowTitle("Registro Cassa - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaPagamentoAmministratore(self, pagamentoAmministratore):
        self.vistaVisualizzaPagamentoAmministratore.pagamentoAmministratore = pagamentoAmministratore
        self.stack.setCurrentWidget(self.vistaVisualizzaPagamentoAmministratore)
        self.setWindowTitle("Pagamento - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaRecensioniAmministratore(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaRecensioniAmministratore)
        self.setWindowTitle("Recensioni - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaRecensioneAmministratore(self, recensioneAmministratore):
        self.vistaVisualizzaRecensioneAmministratore.recensioneAmministratore = recensioneAmministratore
        self.stack.setCurrentWidget(self.vistaVisualizzaRecensioneAmministratore)
        self.setWindowTitle("Recensione - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaAmministratoriAmministratore(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaAmministratoriAmministratore)
        self.setWindowTitle("Amministratori - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaAmministratoreAmministratore(self, amministratoreAmministratore):
        self.vistaVisualizzaAmministratoreAmministratore.amministratoreAmministratore = amministratoreAmministratore
        self.stack.setCurrentWidget(self.vistaVisualizzaAmministratoreAmministratore)
        self.setWindowTitle("Amministratore - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaInserisciAmministratoreAmministratore(self):
        self.stack.setCurrentWidget(self.vistaInserisciAmministratoreAmministratore)
        self.setWindowTitle("Inserisci Amministratore - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaClientiAmministratore(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaClientiAmministratore)
        self.setWindowTitle("Clienti - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaVisualizzaClienteAmministratore(self, clienteAmministratore):
        self.vistaVisualizzaClienteAmministratore.clienteAmministratore = clienteAmministratore
        self.stack.setCurrentWidget(self.vistaVisualizzaClienteAmministratore)
        self.setWindowTitle("Cliente - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaAmministratore.ico"))

    def goVistaLoginCliente(self):
        self.stack.setCurrentWidget(self.vistaLoginCliente)
        self.setWindowTitle("Login Cliente - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaRegistrazioneCliente(self):
        self.stack.setCurrentWidget(self.vistaRegistrazioneCliente)
        self.setWindowTitle("Registrazione - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaHomeCliente(self):
        self.stack.setCurrentWidget(self.vistaHomeCliente)
        self.setWindowTitle("Area Riservata Cliente - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaVisualizzaProfiloPersonaleCliente(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaProfiloPersonaleCliente)
        self.setWindowTitle("Profilo Personale - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaModificaProfiloPersonaleCliente(self):
        self.stack.setCurrentWidget(self.vistaModificaProfiloPersonaleCliente)
        self.setWindowTitle("Modifica Profilo Personale - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaVisualizzaSpettacoliCliente(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaSpettacoliCliente)
        self.setWindowTitle("Spettacoli - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaVisualizzaSpettacoloCliente(self, spettacoloCliente):
        self.vistaVisualizzaSpettacoloCliente.spettacoloCliente = spettacoloCliente
        self.stack.setCurrentWidget(self.vistaVisualizzaSpettacoloCliente)
        self.setWindowTitle("Spettacolo - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaAcquistoBigliettoCliente(self, bigliettoCliente):
        self.vistaAcquistoBigliettoCliente.bigliettoCliente = bigliettoCliente
        self.stack.setCurrentWidget(self.vistaAcquistoBigliettoCliente)
        self.setWindowTitle("Acquisto Biglietto - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaVisualizzaProdottiCliente(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaProdottiCliente)
        self.setWindowTitle("Prodotti - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaVisualizzaProdottoCliente(self, prodottoCliente):
        self.vistaVisualizzaProdottoCliente.prodottoCliente = prodottoCliente
        self.stack.setCurrentWidget(self.vistaVisualizzaProdottoCliente)
        self.setWindowTitle("Prodotto - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaAcquistoProdottoCliente(self, prodottoCliente):
        self.vistaAcquistoProdottoCliente.prodottoCliente = prodottoCliente
        self.stack.setCurrentWidget(self.vistaAcquistoProdottoCliente)
        self.setWindowTitle("Acquisto Prodotto - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaVisualizzaPagamentiCliente(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaPagamentiCliente)
        self.setWindowTitle("Pagamenti - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaVisualizzaPagamentoCliente(self, pagamentoCliente):
        self.vistaVisualizzaPagamentoCliente.pagamentoCliente = pagamentoCliente
        self.stack.setCurrentWidget(self.vistaVisualizzaPagamentoCliente)
        self.setWindowTitle("Pagamento - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaVisualizzaRecensioniCliente(self):
        self.stack.setCurrentWidget(self.vistaVisualizzaRecensioniCliente)
        self.setWindowTitle("Recensioni Personali - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaVisualizzaRecensioneCliente(self, recensioneCliente):
        self.vistaVisualizzaRecensioneCliente.recensioneCliente = recensioneCliente
        self.stack.setCurrentWidget(self.vistaVisualizzaRecensioneCliente)
        self.setWindowTitle("Recensione - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaInserisciRecensioneCliente(self):
        self.stack.setCurrentWidget(self.vistaInserisciRecensioneCliente)
        self.setWindowTitle("Inserisci Recensione - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))

    def goVistaModificaRecensioneCliente(self, recensioneCliente):
        self.vistaModificaRecensioneCliente.recensioneCliente = recensioneCliente
        self.stack.setCurrentWidget(self.vistaModificaRecensioneCliente)
        self.setWindowTitle("Modifica Recensione - CineMax")
        self.setWindowIcon(QIcon("Viste/Immagini/IconaCliente.ico"))
