from Sistema.Recensione import Recensione

import os.path
import pickle

class GestoreRecensioni():

    def __init__(self, listaRecensioni):
        self.listaRecensioni = listaRecensioni

    def caricaDatiRecensioni(self):
        listaDatiRecensioni = []
        if os.path.isfile('Dati/DatiRecensioni.pickle'):
            with open('Dati/DatiRecensioni.pickle', 'rb') as file:
                listaDatiRecensioni = pickle.load(file)
        return listaDatiRecensioni

    def salvaDatiRecensioni(self, listaRecensioni):
        with open('Dati/DatiRecensioni.pickle', 'wb') as file:
            pickle.dump(listaRecensioni, file)

    def getListaRecensioni(self):
        listaRecensioni = self.caricaDatiRecensioni()
        return listaRecensioni
    
    def getListaRecensioniCliente(self, cliente):
        listaRecensioni = self.caricaDatiRecensioni()
        listaRecensioniCliente = []
        for recensione in listaRecensioni:
            if recensione.getCliente() == cliente:
                listaRecensioniCliente.append(recensione)
        return listaRecensioniCliente
    
    def inserisciRecensione(self, listaRecensioni, recensione):
        listaRecensioni = self.caricaDatiRecensioni()
        listaRecensioni.append(recensione)
        self.salvaDatiRecensioni(listaRecensioni)
    

    def rimuoviRecensione(self, listaRecensioni, recensione):
        listaRecensioni = self.caricaDatiRecensioni()
        listaRecensioni.remove(recensione)
        self.salvaDatiRecensioni(listaRecensioni)
        del recensione
