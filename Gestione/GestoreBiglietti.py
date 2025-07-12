import os.path
import pickle

class GestoreBiglietti():

    def __init__(self, listaBiglietti):
        self.listaBiglietti = listaBiglietti

    def caricaDatiBiglietti(self):
        listaDatiBiglietti = []
        if os.path.isfile('Dati/DatiBiglietti.pickle'):
            with open('Dati/DatiBiglietti.pickle', 'rb') as file:
                listaDatiBiglietti = pickle.load(file)
        return listaDatiBiglietti

    def salvaDatiBiglietti(self, listaBiglietti):
        with open('Dati/DatiBiglietti.pickle', 'wb') as file:
            pickle.dump(listaBiglietti, file)

    def getListaBiglietti(self):
        listaBiglietti = self.caricaDatiBiglietti()
        return listaBiglietti
    
    def getListaBigliettiSpettacolo(self, spettacolo):
        listaBiglietti = self.caricaDatiBiglietti()
        listaBigliettiSpettacolo = []
        for biglietto in listaBiglietti:
            if biglietto.spettacolo == spettacolo:
                listaBigliettiSpettacolo.append(biglietto)
        return listaBigliettiSpettacolo
    
    def inserisciBiglietto(self, listaBiglietti, biglietto):
        listaBiglietti = self.caricaDatiBiglietti()
        listaBiglietti.append(biglietto)
        self.salvaDatiBiglietti(listaBiglietti)
    

    def rimuoviBiglietto(self, listaBiglietti, biglietto):
        listaBiglietti = self.caricaDatiBiglietti()
        listaBiglietti.remove(biglietto)
        self.salvaDatiBiglietti(listaBiglietti)
        del biglietto

    def controlloDisponibilità(self, bigliettoDaControllare):
        listaBiglietti = self.caricaDatiBiglietti()
        for biglietto in listaBiglietti:
            if biglietto == bigliettoDaControllare:
                return biglietto.disponibile
