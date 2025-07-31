import unittest

from PySide6.QtCore import QDate
from Sistema.Cliente import Cliente

class TestCliente(unittest.TestCase):
    
    def testCreazioneCliente(self):
        nome = "Elena"
        cognome = "Russo"
        dataNascita = QDate(1992, 9, 5)
        email = "elena.russo@gmail.com"
        telefono = "3284719653"
        password = "Russo9?z"
        codiceFiscale = "RSSLNE92P45F205X"

        cliente = Cliente(nome, cognome, dataNascita, email, telefono, password, codiceFiscale)
        
        self.assertEqual(cliente.getNome(), nome)
        self.assertEqual(cliente.getCognome(), cognome)
        self.assertEqual(cliente.getDataNascita(), dataNascita)
        self.assertEqual(cliente.getEmail(), email)
        self.assertEqual(cliente.getTelefono(), telefono)
        self.assertEqual(cliente.getPassword(), password)
        self.assertEqual(cliente.getCodiceFiscale(), codiceFiscale)

if __name__ == "__main__":
    unittest.main()
