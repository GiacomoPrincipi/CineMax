from Sistema.Pagamento import Pagamento

import os.path
import pickle

class GestorePagamenti():

    def __init__(self):
        self.listaPagamenti = self.caricaDatiPagamenti()

    def caricaDatiPagamenti(self):
        try:
            if os.path.isfile('Dati/DatiPagamenti.pickle'):
                with open('Dati/DatiPagamenti.pickle', 'rb') as file:
                    return pickle.load(file)
        except(EOFError): return []

    def salvaDatiPagamenti(self):
        with open('Dati/DatiPagamenti.pickle', 'wb') as file:
            pickle.dump(self.listaPagamenti, file)

    def getListaPagamenti(self):
        return self.listaPagamenti
    
    def getListaPagamentiCliente(self, cliente):
        listaPagamentiCliente = []
        for pagamento in self.listaPagamenti:
            if pagamento.getCliente().getCodiceFiscale() == cliente.getCodiceFiscale():
                listaPagamentiCliente.append(pagamento)
        return listaPagamentiCliente
    
    def inserisciPagamento(self, pagamento):
        self.listaPagamenti.append(pagamento)
        self.salvaDatiPagamenti()

    def generaIdPagamento(self):
        idMassimo = 0
        if self.listaPagamenti == []:
            return "P00001"
        else: 
            for pagamento in self.listaPagamenti:
                if int(pagamento.getId()[1:]) > idMassimo:
                    idMassimo = int(pagamento.getId()[1:])
            return f"P{idMassimo + 1:05d}"