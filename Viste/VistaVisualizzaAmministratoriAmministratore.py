import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaAmministratoriAmministratore import Ui_VistaVisualizzaAmministratoriAmministratore

class VistaVisualizzaAmministratoriAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaAmministratoriAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaAmministratoriAmministratore()
    widget.show()
    sys.exit(app.exec())
