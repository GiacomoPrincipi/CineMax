import os.path
import pickle

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
            if biglietto.getSpettacolo() == spettacolo:
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
        
    def aggiornaDisponibileBiglietti(self):
        for biglietto in self.getListaBiglietti():
            if not biglietto.getSpettacolo().getStato():
                biglietto.setDisponibile(False)
        self.salvaDatiBiglietti()

