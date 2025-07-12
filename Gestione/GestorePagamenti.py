import os.path
import pickle

class GestorePagamenti():

    def __init__(self, listaPagamenti):
        self.listaPagamenti = listaPagamenti

    def caricaDatiPagamenti(self):
        listaDatiPagamenti = []
        if os.path.isfile('Dati/DatiPagamenti.pickle'):
            with open('Dati/DatiPagamenti.pickle', 'rb') as file:
                listaDatiPagamenti = pickle.load(file)
        return listaDatiPagamenti

    def salvaDatiPagamenti(self, listaPagamenti):
        with open('Dati/DatiPagamenti.pickle', 'wb') as file:
            pickle.dump(listaPagamenti, file)

    def getListaPagamenti(self):
        listaPagamenti = self.caricaDatiPagamenti()
        return listaPagamenti
    
    def getListaPagamentiCliente(self, cliente):
        listaPagamenti = self.caricaDatiPagamenti()
        listaPagamentiCliente = []
        for pagamento in listaPagamenti:
            if pagamento.cliente == cliente:
                listaPagamentiCliente.append(pagamento)
        return listaPagamentiCliente
    
    def inserisciPagamento(self, listaPagamenti, pagamento):
        listaPagamenti = self.caricaDatiPagamenti()
        listaPagamenti.append(pagamento)
        self.salvaDatiPagamenti(listaPagamenti)

