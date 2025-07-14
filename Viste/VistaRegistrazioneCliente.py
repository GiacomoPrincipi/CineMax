import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaRegistrazioneCliente import Ui_VistaRegistrazioneCliente

class VistaRegistrazioneCliente(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaRegistrazioneCliente()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaRegistrazioneCliente()
    widget.show()
    sys.exit(app.exec())
