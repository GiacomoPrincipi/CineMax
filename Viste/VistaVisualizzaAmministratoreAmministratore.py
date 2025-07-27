from PySide6.QtWidgets import QWidget
from ui_VistaVisualizzaAmministratoreAmministratore import Ui_VistaVisualizzaAmministratoreAmministratore

class VistaVisualizzaAmministratoreAmministratore(QWidget):
    def __init__(self, statoLogin, goVistaHomeAmministratore, goVistaVisualizzaAmministratoriAmministratore, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaAmministratoreAmministratore()
        self.ui.setupUi(self)

        self.statoLogin = statoLogin

        self.ui.labelHomeButton.clicked.connect(goVistaHomeAmministratore)
        self.ui.labelIndietroButton.clicked.connect(goVistaVisualizzaAmministratoriAmministratore)

    def showEvent(self, event):
        super().showEvent(event)

        amministratoreAmministratore = self.amministratoreAmministratore

        self.ui.labelNomeAmministratore.setText(amministratoreAmministratore.nome)
        self.ui.labelCognomeAmministratore.setText(amministratoreAmministratore.cognome)
        self.ui.labelDataNascitaAmministratore.setText(amministratoreAmministratore.dataNascita.toString("dd/MM/yyyy"))
        self.ui.labelEmailAmministratore.setText(amministratoreAmministratore.email)
        self.ui.labelTelefonoAmministratore.setText(str(amministratoreAmministratore.telefono))
        self.ui.labelMatricolaAmministratore.setText(amministratoreAmministratore.matricola)
