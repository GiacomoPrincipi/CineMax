from PySide6.QtWidgets import QWidget
from ui_VistaInserisciProdottoAmministratore import Ui_VistaInserisciProdottoAmministratore
from Gestione.GestoreProdotti import GestoreProdotti
from Sistema.Prodotto import Prodotto

class VistaInserisciProdottoAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaVisualizzaProdottiAmministratore, goVistaVisualizzaProdottoAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaInserisciProdottoAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.goVistaVisualizzaProdottoAmministratore = goVistaVisualizzaProdottoAmministratore

        self.ui.pushButtonAnnulla.clicked.connect(goVistaVisualizzaProdottiAmministratore)
        self.ui.pushButtonConferma.clicked.connect(self.conferma)

        opzioni = [" ", "Si", "No"]
        self.ui.comboBoxDisponibile.addItems(opzioni)

    def showEvent(self, event):
        super().showEvent(event)

        self.ui.lineEditNome.setText("")
        self.ui.lineEditIngredienti.setText("")
        self.ui.checkBoxAllergene1.setChecked(False)
        self.ui.checkBoxAllergene2.setChecked(False)
        self.ui.checkBoxAllergene3.setChecked(False)
        self.ui.checkBoxAllergene4.setChecked(False)
        self.ui.checkBoxAllergene5.setChecked(False)
        self.ui.checkBoxAllergene5.setChecked(False)
        self.ui.lineEditPrezzo.setText("")
        self.ui.lineEditPrezzoPunti.setText("")
        self.ui.comboBoxDisponibile.setCurrentIndex(0)

        self.ui.labelErroreNome.setText("")
        self.ui.labelErroreIngredienti.setText("")
        self.ui.labelErrorePrezzo.setText("")
        self.ui.labelErrorePrezzoPunti.setText("")
        self.ui.labelErroreDisponibile.setText("")

    def conferma(self):
        self.ui.labelErroreNome.setText("")
        self.ui.labelErroreIngredienti.setText("")
        self.ui.labelErrorePrezzo.setText("")
        self.ui.labelErrorePrezzoPunti.setText("")
        self.ui.labelErroreDisponibile.setText("")

        nome = self.ui.lineEditNome.text()
        ingredienti = self.ui.lineEditIngredienti.text().split(",")
        ingradienti = [ingrediente.strip() for ingrediente in ingredienti]
        allergeni = []
        ListaCheckBox = [self.ui.checkBoxAllergene1, self.ui.checkBoxAllergene2, self.ui.checkBoxAllergene3, self.ui.checkBoxAllergene4, self.ui.checkBoxAllergene5, self.ui.checkBoxAllergene6]
        for checkBox in ListaCheckBox:
            if checkBox.isChecked():
                allergeni.append(checkBox.text())
        prezzo = float(self.ui.lineEditPrezzo.text())
        prezzoPunti = int(self.ui.lineEditPrezzoPunti.text())
        if self.ui.comboBoxDisponibile.currentText() == "Si":
            disponibile = True
        if self.ui.comboBoxDisponibile.currentText() == "No":
            disponibile = False

        gestoreProdotti = GestoreProdotti()

        id = gestoreProdotti.generaIdProdotto()

        if nome == "" or ingredienti == [] or prezzo == "" or prezzoPunti == ""  or self.ui.comboBoxDisponibile.currentIndex() == 0:
            if nome == "":
                self.ui.labelErroreNome.setText("Inserisci il nome!")
            if self.ui.lineEditIngredienti.text() == "":
                self.ui.labelErroreIngredienti.setText("Inserisci gli ingredienti!")
            if prezzo == "":
                self.ui.labelErrorePrezzo.setText("Inserisci il prezzo!")
            if prezzoPunti == "":
                self.ui.labelErrorePrezzoPunti.setText("Inserisci il prezzo in punti!")
            if self.ui.comboBoxDisponibile.currentIndex() == 0:
                self.ui.labelErroreDisponibile.setText("Inserisci la disponibilità!")
            return

        prodotto = Prodotto(id, prezzo, prezzoPunti, disponibile, nome, ingredienti, allergeni)
        gestoreProdotti.inserisciProdotto(prodotto)

        self.goVistaVisualizzaProdottoAmministratore(prodotto)

