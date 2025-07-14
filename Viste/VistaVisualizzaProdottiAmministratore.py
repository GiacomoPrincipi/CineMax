import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaProdottiAmministratore import Ui_VistaVisualizzaProdottiAmministratore

class VistaVisualizzaProdottiAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProdottiAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaProdottiAmministratore()
    widget.show()
    sys.exit(app.exec())
