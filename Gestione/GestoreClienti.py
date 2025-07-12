import os.path
import pickle

class GestoreClienti():

    def __init__(self, listaClienti):
        self.listaClienti = listaClienti

    def caricaDatiClienti(self):
        listaDatiClienti = []
        if os.path.isfile('Dati/DatiClienti.pickle'):
            with open('Dati/DatiClienti.pickle', 'rb') as file:
                listaDatiClienti = pickle.load(file)
        return listaDatiClienti

    def salvaDatiClienti(self, listaClienti):
        with open('Dati/DatiClienti.pickle', 'wb') as file:
            pickle.dump(listaClienti, file)

    def getListaClienti(self):
        listaClienti = self.caricaDatiClienti()
        return listaClienti
    
    def inserisciCliente(self, listaClienti, cliente):
        listaClienti = self.caricaDatiClienti()
        listaClienti.append(cliente)
        self.salvaDatiClienti(listaClienti)
    

    def rimuoviCliente(self, listaClienti, cliente):
        listaClienti = self.caricaDatiClienti()
        listaClienti.remove(cliente)
        self.salvaDatiClienti(listaClienti)
        del cliente