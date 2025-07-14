import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaSpettacoloCliente import Ui_VistaVisualizzaSpettacoloCliente

class VistaVisualizzaSpettacoloCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaSpettacoloCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaSpettacoloCliente()
    widget.show()
    sys.exit(app.exec())
