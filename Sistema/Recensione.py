class Recensione():
    def __init__(self, cliente, data, ora, stelle, testo):
        self.cliente = cliente
        self.data = data
        self.ora = ora
        self.articolo = stelle
        self.tipo = testo
      
    def getInfoRecensione(self):
        return {self.cliente, self.data, self.ora, self.stelle, self.testo}

    def getCliente(self):
        return self.cliente
    
    def getData(self):
        return self.data
    
    def getOra(self):
        return self.ora

    def getStelle(self):
        return self.stelle
    
    def getTesto(self):
        return self.testo
    
    def setInfoRecensione(self, cliente, data, ora, stelle, testo):
       self.setCliente(self, cliente)
       self.setData(self, data)
       self.setOra(self, ora)
       self.setStelle(self, stelle)
       self.setTesto(self, testo)

    def setCliente(self, cliente):
        self.cliente = cliente

    def setData(self, data):
        self.data = data

    def setOra(self, ora):
        self.ora = ora

    def setStelle(self, stelle):
        self.articolo = articolo

    def setTesto(self, testo):
        self.testo = testo
