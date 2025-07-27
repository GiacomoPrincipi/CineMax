class Recensione():

    def __init__(self, cliente, id, data, ora, stelle, testo):
        self.cliente = cliente
        self.id = id
        self.data = data
        self.ora = ora
        self.stelle = stelle
        self.testo = testo
      
    def getInfoRecensione(self):
        return {self.cliente, self.id, self.data, self.ora, self.stelle, self.testo}

    def getCliente(self):
        return self.cliente
    
    def getId(self):
        return self.id
    
    def getData(self):
        return self.data
    
    def getOra(self):
        return self.ora

    def getStelle(self):
        return self.stelle
    
    def getTesto(self):
        return self.testo
    
    def setInfoRecensione(self, cliente, id, data, ora, stelle, testo):
       self.setCliente(cliente)
       self.setId(id)
       self.setData(data)
       self.setOra(ora)
       self.setStelle(stelle)
       self.setTesto(testo)

    def setCliente(self, cliente):
        self.cliente = cliente

    def setId(self, id):
        self.id = id

    def setData(self, data):
        self.data = data

    def setOra(self, ora):
        self.ora = ora

    def setStelle(self, stelle):
        self.stelle = stelle

    def setTesto(self, testo):
        self.testo = testo
