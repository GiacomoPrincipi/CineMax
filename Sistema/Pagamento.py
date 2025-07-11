class Pagamento():
    def __init__(self, cliente, data, ora, articolo, tipo, importo):
        self.cliente = cliente
        self.data = data
        self.ora = ora
        self.articolo = articolo
        self.tipo = tipo
        self.importo = importo
        
    def getInfoPagamento(self):
        return {self.cliente, self.data, self.ora, self.articolo, self.tipo, self.importo}

    def getCliente(self):
        return self.cliente
    
    def getData(self):
        return self.data
    
    def getOra(self):
        return self.ora

    def getArticolo(self):
        return self.articolo
    
    def getTipo(self):
        return self.tipo
    
    def gerImporto(self):
        return self.importo
    
    def setInfoPagamento(self, cliente, data, ora, articolo, tipo, importo):
       self.setCliente(self, cliente)
       self.setData(self, data)
       self.setOra(self, ora)
       self.setArticolo(self, articolo)
       self.setTipo(self, tipo)
       self.setImporto(self, importo)

    def setCliente(self, cliente: Cliente):
        self.cliente = cliente

    def setData(self, data: Data):
        self.data = data

    def setOra(self, ora: Ora):
        self.ora = ora

    def setArticolo(self, articolo: Articolo):
        self.articolo = articolo

    def setTipo(self, tipo: string):
        self.tipo = tipo

    def setImporto(self, importo: float):
        self.importo = importo
