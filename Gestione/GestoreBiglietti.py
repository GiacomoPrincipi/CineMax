import os.path
import pickle

from Gestione.GestoreSpettacoli import GestoreSpettacoli

class GestoreBiglietti():

    def __init__(self):
        self.listaBiglietti = self.caricaDatiBiglietti()

    def caricaDatiBiglietti(self):
        try:
            if os.path.isfile('Dati/DatiBiglietti.pickle'):
                with open('Dati/DatiBiglietti.pickle', 'rb') as file:
                    return pickle.load(file)
        except(EOFError): return []

    def salvaDatiBiglietti(self):
        with open('Dati/DatiBiglietti.pickle', 'wb') as file:
            pickle.dump(self.listaBiglietti, file)

    def getListaBiglietti(self):
        return self.listaBiglietti
    
    def getListaBigliettiSpettacolo(self, spettacolo):
        listaBigliettiSpettacolo = []
        for biglietto in self.listaBiglietti:
            if biglietto.getSpettacolo().getId() == spettacolo.getId():
                listaBigliettiSpettacolo.append(biglietto)
        return listaBigliettiSpettacolo
    
    def getListaBigliettiDisponibiliSpettacolo(self, spettacolo):
        listaBigliettiDisponibiliSpettacolo = []
        for biglietto in self.listaBiglietti:
            if biglietto.getSpettacolo().getId() == spettacolo.getId():
                if biglietto.getDisponibile() == True:
                    listaBigliettiDisponibiliSpettacolo.append(biglietto)
        return listaBigliettiDisponibiliSpettacolo
    
    def inserisciBiglietto(self, biglietto):
        self.listaBiglietti.append(biglietto)
        self.salvaDatiBiglietti()
    
    def rimuoviBiglietto(self, biglietto):
        self.listaBiglietti.remove(biglietto)
        self.salvaDatiBiglietti()
        del biglietto

    def generaIdBiglietto(self):
        idMassimo = 0
        if self.listaBiglietti == []:
            return "B00001"
        else: 
            for recensione in self.listaBiglietti:
                if int(recensione.getId()[1:]) > idMassimo:
                    idMassimo = int(recensione.getId()[1:])
            return f"P{idMassimo + 1:05d}"

    def aggiornaBiglietti(self):
        gestoreSpettacoli = GestoreSpettacoli()
        for spettacolo in gestoreSpettacoli.getListaSpettacoli():
            for biglietto in self.getListaBigliettiSpettacolo(spettacolo):
                if spettacolo.getStato() == False:
                    biglietto.getSpettacolo().setStato(False)
                if not spettacolo.getStato():
                    biglietto.setDisponibile(False)
        self.salvaDatiBiglietti()
    

