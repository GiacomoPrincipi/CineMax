from PySide6.QtWidgets import QWidget
from Viste.ui_VistaModificaProdottoAmministratore import Ui_VistaModificaProdottoAmministratore
from Gestione.GestoreProdotti import GestoreProdotti

class VistaModificaProdottoAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaVisualizzaProdottoAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaModificaProdottoAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaProdottoAmministratore = goVistaVisualizzaProdottoAmministratore

        self.ui.pushButtonAnnulla.clicked.connect(self.annulla)
        self.ui.pushButtonConferma.clicked.connect(self.conferma)

        opzioni = [" ", "Si", "No"]
        self.ui.comboBoxDisponibile.addItems(opzioni)

    def showEvent(self, event):
        super().showEvent(event)

        prodottoAmministratore = self.prodottoAmministratore

        self.ui.lineEditNome.setText(prodottoAmministratore.getNome())
        ingredienti = ", ".join(prodottoAmministratore.getIngredienti())
        self.ui.lineEditIngredienti.setText(ingredienti)
        ListaCheckBox = [self.ui.checkBoxAllergene1, self.ui.checkBoxAllergene2, self.ui.checkBoxAllergene3, self.ui.checkBoxAllergene4, self.ui.checkBoxAllergene5, self.ui.checkBoxAllergene6]
        for checkBox in ListaCheckBox:
            for allergene in prodottoAmministratore.getAllergeni():
                if checkBox.text() == allergene:
                    checkBox.setChecked(True)
        self.ui.lineEditPrezzo.setText(str(prodottoAmministratore.getPrezzo()))
        self.ui.lineEditPrezzoPunti.setText(str(prodottoAmministratore.getPrezzoPunti()))
        self.ui.comboBoxDisponibile.setCurrentText(prodottoAmministratore.getTestoDisponibile())

        self.ui.labelErroreNome.setText("")
        self.ui.labelErroreIngredienti.setText("")
        self.ui.labelErrorePrezzo.setText("")
        self.ui.labelErrorePrezzoPunti.setText("")
        self.ui.labelErroreDisponibile.setText("")

    def annulla(self):
        self.goVistaVisualizzaProdottoAmministratore(self.prodottoAmministratore)

    def conferma(self):

        prodottoAmministratore = self.prodottoAmministratore

        self.ui.labelErroreNome.setText("")
        self.ui.labelErroreIngredienti.setText("")
        self.ui.labelErrorePrezzo.setText("")
        self.ui.labelErrorePrezzoPunti.setText("")
        self.ui.labelErroreDisponibile.setText("")

        nome = self.ui.lineEditNome.text().title()
        ingredienti = self.ui.lineEditIngredienti.text().split(",")
        ingredienti = [ingrediente.strip().capitalize() for ingrediente in ingredienti]
        allergeni = []
        ListaCheckBox = [self.ui.checkBoxAllergene1, self.ui.checkBoxAllergene2, self.ui.checkBoxAllergene3, self.ui.checkBoxAllergene4, self.ui.checkBoxAllergene5, self.ui.checkBoxAllergene6]
        for checkBox in ListaCheckBox:
            if checkBox.isChecked():
                allergeni.append(checkBox.text())
        prezzo = self.ui.lineEditPrezzo.text()
        prezzoPunti = self.ui.lineEditPrezzoPunti.text()
        try:
            float(prezzo)
            formatoPrezzo = False
        except ValueError:
            formatoPrezzo = True
        if self.ui.comboBoxDisponibile.currentText() == "Si":
            disponibile = True
        if self.ui.comboBoxDisponibile.currentText() == "No":
            disponibile = False

        gestoreProdotti = GestoreProdotti()

        id = gestoreProdotti.generaIdProdotto()

        esito = False

        if nome == "":
            self.ui.labelErroreNome.setText("Inserisci il nome!")
            esito = True
        elif nome.isdigit():
            self.ui.labelErroreNome.setText("Nome non valido!")
            esito = True
        if self.ui.lineEditIngredienti.text() == "":
            self.ui.labelErroreIngredienti.setText("Inserisci gli ingredienti!")
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
        if self.ui.comboBoxDisponibile.currentIndex() == 0:
            self.ui.labelErroreDisponibile.setText("Inserisci la disponibilità!")
            esito = True

        if esito: return

        prezzo = "{:.2f}".format(float(prezzo))
        prezzoPunti = int(prezzoPunti)

        for prodottoNellaLista in gestoreProdotti.getListaProdotti():
            if prodottoAmministratore.getId() == prodottoNellaLista.getId():
                prodottoNellaLista.setInfoProdotto(id, prezzo, prezzoPunti, disponibile, nome, ingredienti, allergeni)
                prodottoAmministratore = prodottoNellaLista

        gestoreProdotti.salvaDatiProdotti()

        self.goVistaVisualizzaProdottoAmministratore(prodottoAmministratore)


