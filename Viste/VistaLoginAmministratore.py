import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaLoginAmministratore import Ui_VistaLoginAmministratore

class VistaLoginAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaLoginAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaLoginAmministratore()
    widget.show()
    sys.exit(app.exec())
