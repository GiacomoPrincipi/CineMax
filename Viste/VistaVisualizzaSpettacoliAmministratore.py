import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaSpettacoliAmministratore import Ui_VistaVisualizzaSpettacoliAmministratore

class VistaVisualizzaSpettacoliAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaSpettacoliAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaSpettacoliAmministratore()
    widget.show()
    sys.exit(app.exec())
