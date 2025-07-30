import os.path
import pickle

class GestoreProdotti():

    def __init__(self):
        self.listaProdotti = self.caricaDatiProdotti()

    def caricaDatiProdotti(self):
        try:
            if os.path.isfile('Dati/DatiProdotti.pickle'):
                with open('Dati/DatiProdotti.pickle', 'rb') as file:
                    return pickle.load(file)
        except(EOFError): return []

    def salvaDatiProdotti(self):
        with open('Dati/DatiProdotti.pickle', 'wb') as file:
            pickle.dump(self.listaProdotti, file)

    def getListaProdotti(self):
        return self.listaProdotti
    
    def getListaProdottiDisponibili(self):
        listaProdottiDisponibili = []
        for prodotto in self.listaProdotti:
            if prodotto.getDisponibile() == True:
                listaProdottiDisponibili.append(prodotto)
        return listaProdottiDisponibili
    
    def inserisciProdotto(self, prodotto):
        self.listaProdotti.append(prodotto)
        self.salvaDatiProdotti()
    
    def rimuoviProdotto(self, prodotto):
        self.listaProdotti.remove(prodotto)
        self.salvaDatiProdotti()
        del prodotto

    def generaIdProdotto(self):
        idMassimo = 0
        if self.listaProdotti == []:
            return "PR00001"
        else: 
            for prodotto in self.listaProdotti:
                if int(prodotto.getId()[2:]) > idMassimo:
                    idMassimo = int(prodotto.getId()[2:])
            return f"PR{idMassimo + 1:05d}"