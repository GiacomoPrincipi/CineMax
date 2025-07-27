class Pagamento():
    
    def __init__(self, cliente, id, data, ora, articolo, tipo, importo, importoPunti):
        self.cliente = cliente
        self.id = id
        self.data = data
        self.ora = ora
        self.articolo = articolo
        self.tipo = tipo
        self.importo = importo
        self.importoPunti = importoPunti
        
    def getInfoPagamento(self):
        return {self.cliente, self.id, self.data, self.ora, self.articolo, self.tipo, self.importo, self.importoPunti}

    def getCliente(self):
        return self.cliente
    
    def getId(self):
        return self.id
    
    def getData(self):
        return self.data
    
    def getOra(self):
        return self.ora

    def getArticolo(self):
        return self.articolo
    
    def getTipo(self):
        return self.tipo
    
    def getImporto(self):
        return self.importo
    
    def getImportoPunti(self):
        return self.importoPunti
    
    def setInfoPagamento(self, cliente, id, data, ora, articolo, tipo, importo, importoPunti):
       self.setCliente(cliente)
       self.setId(id)
       self.setData(data)
       self.setOra(ora)
       self.setArticolo(articolo)
       self.setTipo(tipo)
       self.setImporto(importo)
       self.setImportoPunti(importoPunti)

    def setCliente(self, cliente):
        self.cliente = cliente

    def setId(self, id):
        self.id = id

    def setData(self, data):
        self.data = data

    def setOra(self, ora):
        self.ora = ora

    def setArticolo(self, articolo):
        self.articolo = articolo

    def setTipo(self, tipo):
        self.tipo = tipo

    def setImporto(self, importo):
        self.importo = importo

    def setImportoPunti(self, importoPunti):
        self.importoPunti = importoPunti
