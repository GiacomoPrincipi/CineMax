class Biglietto:
    def __init__(self,spettacolo,tipo,posto):
        self.Spettacolo = spettacolo
        self.tipo = tipo
        self.posto = posto

    def getInfoBiglietto(self):
        return {self.Spettacolo, self.tipo, self.posto}

    def getSpettacolo(self):
        return self.spettacolo

    def getTipo(self):
        return self.tipo

    def getPosto(self):
        return self.posto

    def setInfoBiglietto(self, spettacolo, tipo, posto):
        self.setSpettacolo(self,spettacolo)
        self.setTipo(self,tipo)
        self.setPosto(self,posto)

    def setSpettacolo(self, spettacolo: Spettacolo):
        self.Spettacolo = spettacolo

    def setTipo(self, tipo: str):
        self.tipo = tipo

    def setPosto(self, posto: int):
        self.posto = posto
