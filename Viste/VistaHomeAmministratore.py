import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaHomeAmministratore import Ui_VistaHomeAmministratore

class VistaHomeAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaHomeAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaHomeAmministratore()
    widget.show()
    sys.exit(app.exec())
