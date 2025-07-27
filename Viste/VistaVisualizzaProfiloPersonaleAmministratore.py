from PySide6.QtWidgets import QWidget
from ui_VistaVisualizzaProfiloPersonaleAmministratore import Ui_VistaVisualizzaProfiloPersonaleAmministratore

class VistaVisualizzaProfiloPersonaleAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaModificaProfiloPersonaleAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProfiloPersonaleAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.ui.labelIndietroButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.pushButtonModifica.clicked.connect(goVistaModificaProfiloPersonaleAmministratore)

    def showEvent(self, event):
        super().showEvent(event)

        amministratore = self.statoLogin.amministratoreAutenticato

        self.ui.labelNomeAmministratore.setText(amministratore.nome)
        self.ui.labelCognomeAmministratore.setText(amministratore.cognome)
        self.ui.labelDataNascitaAmministratore.setText(amministratore.dataNascita.toString("dd/MM/yyyy"))
        self.ui.labelEmailAmministratore.setText(amministratore.email)
        self.ui.labelTelefonoAmministratore.setText(str(amministratore.telefono))
        self.ui.labelPasswordAmministratore.setText(amministratore.password)
        self.ui.labelMatricolaAmministratore.setText(amministratore.matricola)
