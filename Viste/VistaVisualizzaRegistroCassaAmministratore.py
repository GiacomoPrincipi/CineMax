import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaRegistroCassaAmministratore import Ui_VistaVisualizzaRegistroCassaAmministratore

class VistaVisualizzaRegistroCassaAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaRegistroCassaAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaRegistroCassaAmministratore()
    widget.show()
    sys.exit(app.exec())
