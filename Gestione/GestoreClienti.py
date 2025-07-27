import os.path
import pickle

class GestoreClienti():

    def __init__(self):
        self.listaClienti = self.caricaDatiClienti()

    def caricaDatiClienti(self):
        try:
            if os.path.isfile('Dati/DatiClienti.pickle'):
                with open('Dati/DatiClienti.pickle', 'rb') as file:
                    return pickle.load(file)
        except(EOFError): return []

    def salvaDatiClienti(self):
        with open('Dati/DatiClienti.pickle', 'wb') as file:
            pickle.dump(self.listaClienti, file)

    def getListaClienti(self):
        return self.listaClienti
    
    def getCliente(self, email):
        for cliente in self.listaClienti:
            if email == cliente.getEmail():
                return cliente
        return None
    
    def inserisciCliente(self, cliente):
        self.listaClienti.append(cliente)
        self.salvaDatiClienti()
    

    def rimuoviCliente(self, cliente):
        self.listaClienti.remove(cliente)
        self.salvaDatiClienti()
        del cliente

    def controlloCodiceFiscale(self, codiceFiscale):
        for cliente in self.listaClienti:
            if cliente.getCodiceFiscale() == codiceFiscale:
                return False
        return True