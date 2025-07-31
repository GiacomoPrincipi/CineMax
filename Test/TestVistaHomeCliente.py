import unittest

from unittest.mock import MagicMock
from PySide6.QtWidgets import QApplication
from Viste.VistaHomeCliente import VistaHomeCliente

class TestVistaHomeCliente(unittest.TestCase):

    def testCreazioneVistaHomeCliente(self):
        app = QApplication([])
        goVistaHome = MagicMock()
        statoLogin = MagicMock()
        goVistaVisualizzaProfiloPersonaleCliente = MagicMock()
        goVistaVisualizzaSpettacoliCliente = MagicMock()
        goVistaVisualizzaProdottiCliente = MagicMock()
        goVistaVisualizzaPagamentiCliente = MagicMock()
        goVistaVisualizzaRecensioniCliente = MagicMock()

        vistaHomeCliente = VistaHomeCliente(statoLogin, goVistaHome, goVistaVisualizzaProfiloPersonaleCliente, goVistaVisualizzaSpettacoliCliente, goVistaVisualizzaProdottiCliente, goVistaVisualizzaPagamentiCliente, goVistaVisualizzaRecensioniCliente)
        self.assertIsInstance(vistaHomeCliente, VistaHomeCliente)
