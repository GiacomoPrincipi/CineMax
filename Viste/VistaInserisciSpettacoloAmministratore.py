from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QTime
from Viste.ui_VistaInserisciSpettacoloAmministratore import Ui_VistaInserisciSpettacoloAmministratore
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

        self.ui.pushButtonAnnulla.clicked.connect(goVistaVisualizzaSpettacoliAmministratore)
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

        titolo = self.ui.lineEditTitolo.text().title()
        genere = self.ui.lineEditGenere.text().title()
        sala = self.ui.comboBoxSala.currentText()
        data = self.ui.dateEditData.date()
        orarioInizio = self.ui.timeEditOrarioInizio.time()
        orarioFine = self.ui.timeEditOrarioFine.time()
        durata = self.ui.lineEditDurata.text()

        prezzo = self.ui.lineEditPrezzo.text()
        prezzoPunti = self.ui.lineEditPrezzoPunti.text()
        try:
            float(prezzo)
            formatoPrezzo = False
        except ValueError:
            formatoPrezzo = True

        gestoreSpettacoli = GestoreSpettacoli()

        id = gestoreSpettacoli.generaIdSpettacolo()

        esito = False
        sottoesito1 = True
        sottoesito2 = True

        if titolo == "":
            self.ui.labelErroreTitolo.setText("Inserisci il titolo!")
            esito = True
        if genere == "":
            self.ui.labelErroreGenere.setText("Inserisci il genere!")
            esito = True
        if self.ui.comboBoxSala.currentIndex() == 0:
            self.ui.labelErroreSala.setText("Inserisci la sala!")
            esito = True
        if data == QDate(1950, 1, 1):
            self.ui.labelErroreData.setText("Inserisci la data!")
            esito = True
        elif data <= QDate.currentDate():
            self.ui.labelErroreData.setText("Data non valida!")
            esito = True
        if orarioInizio == QTime(4, 0, 0):
            self.ui.labelErroreOrarioInizio.setText("Inserisci l'orario di inizio!")
            esito = True
            sottoesito1 = False
        if orarioFine == QTime(4, 0, 0):
            self.ui.labelErroreOrarioFine.setText("Inserisci l'orario di fine!")
            esito = True
            sottoestiro2 = False
        if sottoesito1 and sottoesito2 and orarioFine <= orarioInizio:
            self.ui.labelErroreOrarioFine.setText("")
            self.ui.labelErroreOrarioInizio.setText("Orario non valido!")
            esito = True
        elif gestoreSpettacoli.controlloSpettacoliIntersecati(sala, data, orarioInizio, orarioFine):
            self.ui.labelErroreOrarioFine.setText("")
            self.ui.labelErroreOrarioInizio.setText("C'è già un altro spettacolo!")
            esito = True
        if durata == "":
            self.ui.labelErroreDurata.setText("Inserisci la durata!")
            esito = True
        elif not durata.isdigit():
            self.ui.labelErroreDurata.setText("Durata non valida!")
            esito = True
        if prezzo == "":
            self.ui.labelErrorePrezzo.setText("Inserisci il prezzo!")
            esito = True
        elif "," in prezzo:
            self.ui.labelErrorePrezzo.setText("Formato non valido!")
            esito = True
        elif "." not in prezzo and not prezzo.isdigit():
            self.ui.labelErrorePrezzo.setText("Prezzo non valido!")
            esito = True
        elif formatoPrezzo:
            self.ui.labelErrorePrezzo.setText("Prezzo non valido!")
            esito = True
        if prezzoPunti == "":
            self.ui.labelErrorePrezzoPunti.setText("Inserisci il prezzo in punti!")
            esito = True
        elif not prezzoPunti.isdigit():
            self.ui.labelErrorePrezzoPunti.setText("Prezzo non valido!")
            esito = True

        if esito: return

        durata = int(durata)
        prezzo = "{:.2f}".format(float(prezzo))
        prezzoPunti = int(prezzoPunti)

        spettacolo = Spettacolo(titolo, id, genere, sala, data, orarioInizio, orarioFine, durata)
        gestoreSpettacoli.inserisciSpettacolo(spettacolo)

        gestoreBiglietti = GestoreBiglietti()
        for i in range(1, 71):
            id = gestoreBiglietti.generaIdBiglietto()
            biglietto = Biglietto(id, prezzo, prezzoPunti, True, spettacolo, " ", i)
            gestoreBiglietti.inserisciBiglietto(biglietto)

        self.goVistaVisualizzaSpettacoloAmministratore(spettacolo)

