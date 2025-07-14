import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaProdottoAmministratore import Ui_VistaVisualizzaProdottoAmministratore

class VistaVisualizzaProdottoAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaProdottoAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaProdottoAmministratore()
    widget.show()
    sys.exit(app.exec())
