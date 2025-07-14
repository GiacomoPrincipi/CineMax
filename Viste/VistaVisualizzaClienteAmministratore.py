import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaClienteAmministratore import Ui_VistaVisualizzaClienteAmministratore

class VistaVisualizzaClienteAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaClienteAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaClienteAmministratore()
    widget.show()
    sys.exit(app.exec())
