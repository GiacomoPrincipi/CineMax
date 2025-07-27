from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QTime
from ui_VistaModificaSpettacoloAmministratore import Ui_VistaModificaSpettacoloAmministratore
from Gestione.GestoreSpettacoli import GestoreSpettacoli
from Gestione.GestoreBiglietti import GestoreBiglietti
from Sistema.Spettacolo import Spettacolo
from Sistema.Biglietto import Biglietto

class VistaModificaSpettacoloAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaVisualizzaSpettacoloAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaModificaSpettacoloAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaSpettacoloAmministratore = goVistaVisualizzaSpettacoloAmministratore
        self.goVistaVisualizzaSpettacoloAmministratore = goVistaVisualizzaSpettacoloAmministratore

        self.ui.pushButtonAnnulla.clicked.connect(self.annulla)
        self.ui.pushButtonConferma.clicked.connect(self.conferma)

        opzioni = [" ", "1", "2", "3", "4", "5", "6"]
        self.ui.comboBoxSala.addItems(opzioni)

    def showEvent(self, event):
        super().showEvent(event)

        spettacolo = self.spettacoloAmministratore
        gestoreBiglietti = GestoreBiglietti()

        self.ui.lineEditTitolo.setText(spettacolo.getTitolo())
        self.ui.lineEditGenere.setText(spettacolo.getGenere())
        self.ui.comboBoxSala.setCurrentText(spettacolo.getSala())
        self.ui.dateEditData.setDate(spettacolo.getData())
        self.ui.timeEditOrarioInizio.setTime(spettacolo.getOrarioInizio())
        self.ui.timeEditOrarioFine.setTime(spettacolo.getOrarioFine())
        self.ui.lineEditDurata.setText(str(spettacolo.getDurata()))

        self.ui.labelErroreTitolo.setText("")
        self.ui.labelErroreGenere.setText("")
        self.ui.labelErroreSala.setText("")
        self.ui.labelErroreData.setText("")
        self.ui.labelErroreOrarioInizio.setText("")
        self.ui.labelErroreOrarioFine.setText("")
        self.ui.labelErroreDurata.setText("")

    def conferma(self):
        self.ui.labelErroreTitolo.setText("")
        self.ui.labelErroreGenere.setText("")
        self.ui.labelErroreSala.setText("")
        self.ui.labelErroreData.setText("")
        self.ui.labelErroreOrarioInizio.setText("")
        self.ui.labelErroreOrarioFine.setText("")
        self.ui.labelErroreDurata.setText("")

        titolo = self.ui.lineEditTitolo.text()
        genere = self.ui.lineEditGenere.text()
        sala = self.ui.comboBoxSala.currentText()
        data = self.ui.dateEditData.date()
        orarioInizio = self.ui.timeEditOrarioInizio.time()
        orarioFine = self.ui.timeEditOrarioFine.time()
        durata = self.ui.lineEditDurata.text()


        gestoreSpettacoli = GestoreSpettacoli()

        spettacolo = self.spettacoloAmministratore

        stato = spettacolo.getStato()
        id = spettacolo.getId()

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

        for spettacoloNellaLista in gestoreSpettacoli.getListaSpettacoli():
            if spettacolo.getId() == spettacoloNellaLista.getId():
                spettacoloNellaLista.setInfoSpettacolo(titolo, id, genere, sala, data, orarioInizio, orarioFine, durata, stato)
                spettacolo = spettacoloNellaLista

        gestoreSpettacoli.salvaDatiSpettacoli()

        gestoreBiglietti = GestoreBiglietti()


        for bigliettoNellaLista in gestoreBiglietti.getListaBigliettiSpettacolo(spettacolo):
            if bigliettoNellaLista.getSpettacolo().getId() == spettacolo.getId():
                bigliettoNellaLista.setSpettacolo(spettacolo)

        gestoreBiglietti.salvaDatiBiglietti()

        self.goVistaVisualizzaSpettacoloAmministratore(spettacolo)

    def annulla(self):
        self.goVistaVisualizzaSpettacoloAmministratore(self.spettacoloAmministratore)



