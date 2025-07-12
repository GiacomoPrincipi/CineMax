import os.path
import pickle

class GestoreSpettacoli():

    def __init__(self, listaSpettacoli):
        self.listaSpettacoli = listaSpettacoli

    def caricaDatiSpettacoli(self):
        listaDatiSpettacoli = []
        if os.path.isfile('Dati/DatiSpettacoli.pickle'):
            with open('Dati/DatiSpettacoli.pickle', 'rb') as file:
                listaDatiSpettacoli = pickle.load(file)
        return listaDatiSpettacoli

    def salvaDatiSpettacoli(self, listaSpettacoli):
        with open('Dati/DatiSpettacoli.pickle', 'wb') as file:
            pickle.dump(listaSpettacoli, file)

    def getListaSpettacoli(self):
        listaSpettacoli = self.caricaDatiSpettacoli()
        return listaSpettacoli
    
    def inserisciSpettacolo(self, listaSpettacoli, spettacolo):
        listaSpettacoli = self.caricaDatiSpettacoli()
        listaSpettacoli.append(spettacolo)
        self.salvaDatiSpettacoli(listaSpettacoli)
    

    def rimuoviSpettacolo(self, listaSpettacoli, spettacolo):
        listaSpettacoli = self.caricaDatiSpettacoli()
        listaSpettacoli.remove(spettacolo)
        self.salvaDatiSpettacoli(listaSpettacoli)
        del spettacolo
