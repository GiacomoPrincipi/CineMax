import os.path
import pickle

class GestoreAmministratori():

    def __init__(self, listaAmministratori):
        self.listaAmministratori = listaAmministratori

    def caricaDatiAmministratori(self):
        listaDatiAmministratori = []
        if os.path.isfile('Dati/DatiAmministratori.pickle'):
            with open('Dati/DatiAmministratori.pickle', 'rb') as file:
                listaDatiAmministratori = pickle.load(file)
        return listaDatiAmministratori

    def salvaDatiAmministratori(self, listaAmministratori):
        with open('Dati/DatiAmministratori.pickle', 'wb') as file:
            pickle.dump(listaAmministratori, file)

    def getListaAmministratori(self):
        listaAmministratori = self.caricaDatiAmministratori()
        return listaAmministratori
    
    def inserisciAmministratore(self, listaAmministratori, amministratore):
        listaAmministratori = self.caricaDatiAmministratori()
        listaAmministratori.append(amministratore)
        self.salvaDatiAmministratori(listaAmministratori)
    

    def rimuoviAmministratore(self, listaAmministratori, amministratore):
        listaAmministratori = self.caricaDatiAmministratori()
        listaAmministratori.remove(amministratore)
        self.salvaDatiAmministratori(listaAmministratori)
        del amministratore