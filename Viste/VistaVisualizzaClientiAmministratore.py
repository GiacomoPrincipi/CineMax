import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaClientiAmministratore import Ui_VistaVisualizzaClientiAmministratore

class VistaVisualizzaClientiAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaClientiAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaClientiAmministratore()
    widget.show()
    sys.exit(app.exec())
