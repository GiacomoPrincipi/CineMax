import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaRecensioniAmministratore import Ui_VistaVisualizzaRecensioniAmministratore

class VistaVisualizzaRecensioniAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaRecensioniAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaRecensioniAmministratore()
    widget.show()
    sys.exit(app.exec())
