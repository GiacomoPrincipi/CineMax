from Sistema.Articolo import Articolo

class Biglietto(Articolo):
    
    def __init__(self, prezzo, disponibile, spettacolo, tipo, posto):
        super().__init__(prezzo, disponibile)
        self.spettacolo = spettacolo
        self.tipo = tipo
        self.posto = posto

    def getInfoBiglietto(self):
        return {self.prezzo, self.disponibile, self.spettacolo, self.tipo, self.posto}

    def getPrezzo(self):
        return self.prezzo

    def getDisponibile(self):
        return self.disponibile

    def getSpettacolo(self):
        return self.spettacolo

    def getTipo(self):
        return self.tipo

    def getPosto(self):
        return self.posto

    def setInfoBiglietto(self, prezzo, disponibile, spettacolo, tipo, posto):
        self.setPrezzo(self, prezzo)
        self.setDisponibile(self, disponibile)
        self.setSpettacolo(self, spettacolo)
        self.setTipo(self, tipo)
        self.setPosto(self, posto)

    def setPrezzo(self, prezzo):
        self.prezzo = prezzo

    def setDisponibile(self, disponibile):
        self.disponibile = disponibile
    
    def setSpettacolo(self, spettacolo):
        self.Spettacolo = spettacolo

    def setTipo(self, tipo):
        self.tipo = tipo

    def setPosto(self, posto):
        self.posto = posto
