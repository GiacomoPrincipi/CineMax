import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaSpettacoliCliente import Ui_VistaVisualizzaSpettacoliCliente

class VistaVisualizzaSpettacoliCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaSpettacoliCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaSpettacoliCliente()
    widget.show()
    sys.exit(app.exec())
