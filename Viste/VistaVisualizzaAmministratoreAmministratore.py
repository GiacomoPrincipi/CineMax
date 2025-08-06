from PySide6.QtWidgets import QWidget
from Viste.ui_VistaVisualizzaAmministratoreAmministratore import Ui_VistaVisualizzaAmministratoreAmministratore

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

        self.ui.labelNomeAmministratore.setText(amministratoreAmministratore.getNome())
        self.ui.labelCognomeAmministratore.setText(amministratoreAmministratore.getCognome())
        self.ui.labelDataNascitaAmministratore.setText(amministratoreAmministratore.getDataNascita().toString("dd/MM/yyyy"))
        self.ui.labelEmailAmministratore.setText(amministratoreAmministratore.getEmail())
        self.ui.labelTelefonoAmministratore.setText(amministratoreAmministratore.getTelefono())
        self.ui.labelMatricolaAmministratore.setText(amministratoreAmministratore.getMatricola())
