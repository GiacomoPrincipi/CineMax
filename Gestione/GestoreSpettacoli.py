import os.path
import pickle
from PySide6.QtCore import QDate, QTime

class GestoreSpettacoli():

    def __init__(self):
        self.listaSpettacoli = self.caricaDatiSpettacoli()

    def caricaDatiSpettacoli(self):
        try:
            if os.path.isfile('Dati/DatiSpettacoli.pickle'):
                with open('Dati/DatiSpettacoli.pickle', 'rb') as file:
                    return pickle.load(file)
        except(EOFError): return []

    def salvaDatiSpettacoli(self):
        with open('Dati/DatiSpettacoli.pickle', 'wb') as file:
            pickle.dump(self.listaSpettacoli, file)

    def getListaSpettacoli(self):
        return self.listaSpettacoli
    
    def getListaSpettacoliAttivi(self):
        listaSpettacoliAttivi = []
        for spettacolo in self.listaSpettacoli:
            if spettacolo.getStato():
                listaSpettacoliAttivi.append(spettacolo)
        return listaSpettacoliAttivi
    
    def inserisciSpettacolo(self, spettacolo):
        self.listaSpettacoli.append(spettacolo)
        self.salvaDatiSpettacoli()
    

    def rimuoviSpettacolo(self, spettacolo):
        self.listaSpettacoli.remove(spettacolo)
        self.salvaDatiSpettacoli()
        del spettacolo

    def generaIdSpettacolo(self):
        idMassimo = 0
        if self.listaSpettacoli == []:
            return "S00001"
        else: 
            for spettacolo in self.listaSpettacoli:
                if int(spettacolo.getId()[1:]) > idMassimo:
                    idMassimo = int(spettacolo.getId()[1:])
            return f"S{idMassimo + 1:05d}"
        
    def aggiornaSpettacoli(self):
        for spettacolo in self.getListaSpettacoli():
            if spettacolo.getData() < QDate.currentDate():
                spettacolo.setStato(False)
            elif spettacolo.getData() == QDate.currentDate() and spettacolo.getOrarioInizio() < QTime.currentTime():
                spettacolo.setStato(False)
        self.salvaDatiSpettacoli()

    def controlloSpettacoliIntersecati(self, sala, data, orarioInizio, orarioFine):
        for spettacolo in self.getListaSpettacoliAttivi():
            if spettacolo.getSala() == sala:
                if spettacolo.getData() == data:
                    if spettacolo.getOrarioFine() > orarioInizio and orarioFine > spettacolo.getOrarioInizio():
                        return True
        return False
