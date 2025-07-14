import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaProfiloPersonaleAmministratore import Ui_VistaVisualizzaProfiloPersonaleAmministratore

class VistaVisualizzaProfiloPersonaleAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProfiloPersonaleAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaProfiloPersonaleAmministratore()
    widget.show()
    sys.exit(app.exec())
