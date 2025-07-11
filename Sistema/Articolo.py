class Articolo():
    def __init__(self, prezzo, disponibile):
        self.prezzo = prezzo
        self.disponibile = disponibile

    def getInfoArticolo(self):
        return {self.prezzo, self.disponibile}

    def getPrezzo(self):
        return self.prezzo

    def getDisponibile(self):
        return self.disponibile
      
    def setInfoArticolo(self, prezzo, disponibile):
        self.setPrezzo(self, prezzo)
        self.setDisponibile(self, disponibile)

    def setPrezzo(self, prezzo):
        self.prezzo = prezzo

    def setDisponibile(self, disponibile):
        self.disponibile = disponibile
