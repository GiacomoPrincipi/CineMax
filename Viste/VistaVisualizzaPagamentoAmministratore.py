import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_VistaVisualizzaPagamentoAmministratore import Ui_VistaVisualizzaPagamentoAmministratore

class VistaVisualizzaPagamentoAmministratore(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_VistaVisualizzaPagamentoAmministratore()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VistaVisualizzaPagamentoAmministratore()
    widget.show()
    sys.exit(app.exec())
