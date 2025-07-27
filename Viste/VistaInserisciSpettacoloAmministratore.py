from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QTime
from ui_VistaInserisciSpettacoloAmministratore import Ui_VistaInserisciSpettacoloAmministratore
from Gestione.GestoreSpettacoli import GestoreSpettacoli
from Gestione.GestoreBiglietti import GestoreBiglietti
from Sistema.Spettacolo import Spettacolo
from Sistema.Biglietto import Biglietto

class VistaInserisciSpettacoloAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaVisualizzaSpettacoliAmministratore, goVistaVisualizzaSpettacoloAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaInserisciSpettacoloAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaSpettacoloAmministratore = goVistaVisualizzaSpettacoloAmministratore

        self.ui.pushButtonAnnulla.clicked.connect(goVistaVisualizzaSpettacoloAmministratore)
        self.ui.pushButtonConferma.clicked.connect(self.conferma)

        opzioni = [" ", "1", "2", "3", "4", "5", "6"]
        self.ui.comboBoxSala.addItems(opzioni)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.lineEditTitolo.setText("")
        self.ui.lineEditGenere.setText("")
        self.ui.comboBoxSala.setCurrentIndex(0)
        self.ui.dateEditData.setDate(QDate(1950, 1, 1))
        self.ui.timeEditOrarioInizio.setTime(QTime(4, 0, 0))
        self.ui.timeEditOrarioFine.setTime(QTime(4, 0, 0))
        self.ui.lineEditDurata.setText("")
        self.ui.lineEditPrezzo.setText("")
        self.ui.lineEditPrezzoPunti.setText("")


        self.ui.labelErroreTitolo.setText("")
        self.ui.labelErroreGenere.setText("")
        self.ui.labelErroreSala.setText("")
        self.ui.labelErroreData.setText("")
        self.ui.labelErroreOrarioInizio.setText("")
        self.ui.labelErroreOrarioFine.setText("")
        self.ui.labelErroreDurata.setText("")
        self.ui.labelErrorePrezzo.setText("")
        self.ui.labelErrorePrezzoPunti.setText("")

    def conferma(self):
        self.ui.labelErroreTitolo.setText("")
        self.ui.labelErroreGenere.setText("")
        self.ui.labelErroreSala.setText("")
        self.ui.labelErroreData.setText("")
        self.ui.labelErroreOrarioInizio.setText("")
        self.ui.labelErroreOrarioFine.setText("")
        self.ui.labelErroreDurata.setText("")
        self.ui.labelErrorePrezzo.setText("")
        self.ui.labelErrorePrezzoPunti.setText("")

        titolo = self.ui.lineEditTitolo.text()
        genere = self.ui.lineEditGenere.text()
        sala = self.ui.comboBoxSala.currentText()
        data = self.ui.dateEditData.date()
        orarioInizio = self.ui.timeEditOrarioInizio.time()
        orarioFine = self.ui.timeEditOrarioFine.time()
        durata = self.ui.lineEditDurata.text()

        prezzo = float(self.ui.lineEditPrezzo.text())
        prezzoPunti = int(self.ui.lineEditPrezzoPunti.text())

        gestoreSpettacoli = GestoreSpettacoli()

        id = gestoreSpettacoli.generaIdSpettacolo()

        if titolo == "" or genere == "" or self.ui.comboBoxSala.currentIndex() == 0 or data == QDate(1950, 1, 1) or orarioInizio == QTime(4, 0, 0) or orarioFine == QTime(4, 0, 0) or durata == "":
            if titolo == "":
                self.ui.labelErroreTitolo.setText("Inserisci il titolo!")
            if genere == "":
                self.ui.labelErroreGenere.setText("Inserisci il genere!")
            if self.ui.comboBoxSala.currentIndex() == 0:
                self.ui.labelErroreSala.setText("Inserisci la sala!")
            if data == QDate(1950, 1, 1):
                self.ui.labelErroreData.setText("Inserisci la data!")
            elif data <= QDate.currentDate():
                self.ui.labelErroreData.setText("data non valida!")
            if orarioInizio == QTime(4, 0, 0):
                self.ui.labelErroreOrarioInizio.setText("Inserisci l'orario di inizio!")
            if orarioFine == QTime(4, 0, 0):
                self.ui.labelErroreOrarioFine.setText("Inserisci l'orario di fine!")
            if durata == "":
                self.ui.labelErroreDurata.setText("Inserisci la durata!")
            if prezzo == "":
                self.ui.labelErrorePrezzo.setText("Inserisci il prezzo!")
            if prezzoPunti == "":
                self.ui.labelErrorePrezzoPunti.setText("Inserisci il prezzo!")
            return

        spettacolo = Spettacolo(titolo, id, genere, sala, data, orarioInizio, orarioFine, durata)
        gestoreSpettacoli.inserisciSpettacolo(spettacolo)

        gestoreBiglietti = GestoreBiglietti()
        for i in range(1, 71):
            id = gestoreBiglietti.generaIdBiglietto()
            biglietto = Biglietto(id, prezzo, prezzoPunti, True, spettacolo, " ", i)
            gestoreBiglietti.inserisciBiglietto(biglietto)


        self.goVistaVisualizzaSpettacoloAmministratore(spettacolo)

