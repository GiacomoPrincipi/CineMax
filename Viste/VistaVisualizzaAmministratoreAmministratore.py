import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaAmministratoreAmministratore import Ui_VistaVisualizzaAmministratoreAmministratore

class VistaVisualizzaAmministratoreAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaAmministratoreAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaAmministratoreAmministratore()
    widget.show()
    sys.exit(app.exec())
