import unittest

from unittest.mock import patch, mock_open
from Gestione.GestoreClienti import GestoreClienti

class TestGestoreClienti(unittest.TestCase) :

    @patch('Gestione.GestoreClienti.os.path.isfile')
    @patch('Gestione.GestoreClienti.pickle.load')
    @patch('builtins.open', new_callable = mock_open)
    def testCreazioneGestoreClienti(self, mock_open_file, mock_load, mock_isfile):
        mock_isfile.return_value = True
        mock_load.return_value = ["cliente1", "cliente2"]

        gestoreClienti = GestoreClienti()
        
        self.assertEqual(gestoreClienti.getListaClienti(), ["cliente1", "cliente2"])

        mock_open_file.assert_called_once_with('Dati/DatiClienti.pickle', 'rb')

if __name__ == '__main__':
    unittest.main()
    