import sys

from PySide6.QtWidgets import QApplication
from VistaPrincipale import VistaPrincipale
from Gestione.GestoreAutenticazione import GestoreAutenticazione

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    statoLogin = GestoreAutenticazione()
    vistaPrincipale = VistaPrincipale(statoLogin)
    vistaPrincipale.show()
    sys.exit(app.exec())
