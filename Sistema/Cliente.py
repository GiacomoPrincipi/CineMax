class Cliente():
    def __init__(self, codiceFiscale, punti):
        self.codiceFiscale = codiceFiscale
        self.punti = punti
        
    def getInfoCliente(self):
        return {self.cliente, self.data, self.ora, self.articolo, self.tipo, self.importo}

    def getCodiceFiscale(self):
        return self.codiceFiscale
    
    def getPunti(self):
        return self.punti
    
    def setInfoCliente(self, codiceFiscale, punti):
       self.codiceFiscale(self, codiceFiscale)
       self.punti(self, punti)

    def setCodiceFiscale(self, codiceFiscale: string):
        self.codiceFiscale = codiceFiscale

    def setPunti(self, punti: int):
        self.punti = punti
