import os.path
import pickle

class GestoreRecensioni():

    def __init__(self):
        self.listaRecensioni = self.caricaDatiRecensioni()

    def caricaDatiRecensioni(self):
        try:
            if os.path.isfile('Dati/DatiRecensioni.pickle'):
                with open('Dati/DatiRecensioni.pickle', 'rb') as file:
                    return pickle.load(file)
        except(EOFError): return []

    def salvaDatiRecensioni(self):
        with open('Dati/DatiRecensioni.pickle', 'wb') as file:
            pickle.dump(self.listaRecensioni, file)

    def getListaRecensioni(self):
        return self.listaRecensioni
    
    def getListaRecensioniCliente(self, cliente):
        listaRecensioniCliente = []
        for recensione in self.listaRecensioni:
            if  recensione.getCliente().getCodiceFiscale() == cliente.getCodiceFiscale():
                listaRecensioniCliente.append(recensione)
        return listaRecensioniCliente
    
    def inserisciRecensione(self, recensione):
        self.listaRecensioni.append(recensione)
        self.salvaDatiRecensioni()
    

    def rimuoviRecensione(self, recensione):
        self.listaRecensioni.remove(recensione)
        self.salvaDatiRecensioni()
        del recensione

    def generaIdRecensione(self):
        idMassimo = 0
        if self.listaRecensioni == []:
            return "R00001"
        else: 
            for recensione in self.listaRecensioni:
                if int(recensione.getId()[1:]) > idMassimo:
                    idMassimo = int(recensione.getId()[1:])
            return f"R{idMassimo + 1:05d}"
