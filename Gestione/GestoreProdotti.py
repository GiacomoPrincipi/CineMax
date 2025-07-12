import os.path
import pickle

class GestoreProdotti():

    def __init__(self, listaProdotti):
        self.listaProdotti = listaProdotti

    def caricaDatiProdotti(self):
        listaDatiProdotti = []
        if os.path.isfile('Dati/DatiProdotti.pickle'):
            with open('Dati/DatiProdotti.pickle', 'rb') as file:
                listaDatiProdotti = pickle.load(file)
        return listaDatiProdotti

    def salvaDatiProdotti(self, listaProdotti):
        with open('Dati/DatiProdotti.pickle', 'wb') as file:
            pickle.dump(listaProdotti, file)

    def getListaProdotti(self):
        listaProdotti = self.caricaDatiProdotti()
        return listaProdotti
    
    def inserisciProdottto(self, listaProdotti, prodotto):
        listaProdotti = self.caricaDatiProdotti()
        listaProdotti.append(prodotto)
        self.salvaDatiProdotti(listaProdotti)
    

    def rimuoviProdotto(self, listaProdotti, prodotto):
        listaProdotti = self.caricaDatiProdotti()
        listaProdotti.remove(prodotto)
        self.salvaDatiProdotti(listaProdotti)
        del prodotto

    def controlloDisponibilità(self, prodottoDaControllare):
        listaProdotti = self.caricaDatiProdotti()
        for prodotto in listaProdotti:
            if prodotto == prodottoDaControllare:
                return prodotto.disponibile
