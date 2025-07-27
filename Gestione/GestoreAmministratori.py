import os.path
import pickle

class GestoreAmministratori():

    def __init__(self):
        self.listaAmministratori = self.caricaDatiAmministratori()

    def caricaDatiAmministratori(self):
        try:
            if os.path.isfile('Dati/DatiAmministratori.pickle'):
                with open('Dati/DatiAmministratori.pickle', 'rb') as file:
                    return pickle.load(file)
        except(EOFError): return []

    def salvaDatiAmministratori(self):
        with open('Dati/DatiAmministratori.pickle', 'wb') as file:
            pickle.dump(self.listaAmministratori, file)

    def getListaAmministratori(self):
        return self.listaAmministratori
    
    def getAmministratore(self, email):
        for amministratore in self.listaAmministratori:
            if email == amministratore.getEmail():
                return amministratore
        return None
    
    def inserisciAmministratore(self, amministratore):
        self.listaAmministratori.append(amministratore)
        self.salvaDatiAmministratori()
    

    def rimuoviAmministratore(self, amministratore):
        self.listaAmministratori.remove(amministratore)
        self.salvaDatiAmministratori()
        del amministratore

    def controlloMatricola(self, matricola):
        for amministratore in self.listaAmministratori:
            if amministratore.getMatricola() == matricola:
                return False
        return True