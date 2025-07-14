import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaSpettacoloAmministratore import Ui_VistaVisualizzaSpettacoloAmministratore

class VistaVisualizzaSpettacoloAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaSpettacoloAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaSpettacoloAmministratore()
    widget.show()
    sys.exit(app.exec())
