from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, QTime
from Viste.ui_VistaModificaSpettacoloAmministratore import Ui_VistaModificaSpettacoloAmministratore
from Gestione.GestoreSpettacoli import GestoreSpettacoli
from Gestione.GestoreBiglietti import GestoreBiglietti

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

        spettacoloAmministratore = self.spettacoloAmministratore
        gestoreBiglietti = GestoreBiglietti()

        prezzo = gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloAmministratore)[0].getPrezzo()
        prezzoPunti = gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloAmministratore)[0].getPrezzoPunti()
        if gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloAmministratore) == []:
                prezzo = gestoreBiglietti.getListaBigliettiSpettacolo(spettacoloAmministratore)[0].getPrezzo()
                prezzoPunti = gestoreBiglietti.getListaBigliettiSpettacolo(spettacoloAmministratore).getPrezzoPunti()

        self.ui.lineEditTitolo.setText(spettacoloAmministratore.getTitolo())
        self.ui.lineEditGenere.setText(spettacoloAmministratore.getGenere())
        self.ui.comboBoxSala.setCurrentText(spettacoloAmministratore.getSala())
        self.ui.dateEditData.setDate(spettacoloAmministratore.getData())
        self.ui.timeEditOrarioInizio.setTime(spettacoloAmministratore.getOrarioInizio())
        self.ui.timeEditOrarioFine.setTime(spettacoloAmministratore.getOrarioFine())
        self.ui.lineEditDurata.setText(str(spettacoloAmministratore.getDurata()))
        self.ui.lineEditPrezzo.setText(str(prezzo))
        self.ui.lineEditPrezzoPunti.setText(str(prezzoPunti))

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

        spettacoloAmministratore = self.spettacoloAmministratore

        stato = spettacoloAmministratore.getStato()
        id = spettacoloAmministratore.getId()

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

        for spettacoloNellaLista in gestoreSpettacoli.getListaSpettacoli():
            if spettacoloAmministratore.getId() == spettacoloNellaLista.getId():
                spettacoloNellaLista.setInfoSpettacolo(titolo, id, genere, sala, data, orarioInizio, orarioFine, durata, stato)
                spettacoloAmministratore = spettacoloNellaLista

        gestoreSpettacoli.salvaDatiSpettacoli()

        gestoreBiglietti = GestoreBiglietti()

        for bigliettoNellaLista in gestoreBiglietti.getListaBigliettiSpettacolo(spettacoloAmministratore):
            bigliettoNellaLista.setSpettacolo(spettacoloAmministratore)

        for bigliettoNellaLista in gestoreBiglietti.getListaBigliettiDisponibiliSpettacolo(spettacoloAmministratore):
            bigliettoNellaLista.setPrezzo(prezzo)
            bigliettoNellaLista.setPrezzoPunti(prezzoPunti)

        gestoreBiglietti.salvaDatiBiglietti()

        self.goVistaVisualizzaSpettacoloAmministratore(spettacoloAmministratore)

    def annulla(self):
        self.goVistaVisualizzaSpettacoloAmministratore(self.spettacoloAmministratore)



