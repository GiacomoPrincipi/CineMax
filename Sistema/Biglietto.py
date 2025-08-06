from Sistema.Articolo import Articolo

class Biglietto(Articolo):
    
    def __init__(self, id, prezzo, prezzoPunti, disponibile, spettacolo, tipo, posto):
        super().__init__(id, prezzo, prezzoPunti, disponibile)
        self.spettacolo = spettacolo
        self.tipo = tipo
        self.posto = posto
        self.disponibile = True

    def __eq__(self, biglietto):
        return isinstance(biglietto, Biglietto) and self.getId() == biglietto.getId()

    def getInfoBiglietto(self):
        return {self.id, self.prezzo, self.prezzoPunti, self.disponibile, self.spettacolo, self.tipo, self.posto}

    def getId(self):
        return self.id
    
    def getPrezzo(self):
        return self.prezzo
    
    def getPrezzoPunti(self):
        return self.prezzoPunti

    def getDisponibile(self):
        return self.disponibile
    
    def getTestoDisponibile(self):
        if self.getDisponibile() == True:
            return "Si"
        else: return "No"

    def getSpettacolo(self):
        return self.spettacolo

    def getTipo(self):
        return self.tipo

    def getPosto(self):
        return self.posto

    def setInfoBiglietto(self, id, prezzo, prezzoPunti, disponibile, spettacolo, tipo, posto):
        self.setId(id)
        self.setPrezzo(prezzo)
        self.setPrezzoPunti(prezzoPunti)
        self.setDisponibile(disponibile)
        self.setSpettacolo(spettacolo)
        self.setTipo(tipo)
        self.setPosto(posto)
    
    def setId(self, id):
        self.id = id

    def setPrezzo(self, prezzo):
        self.prezzo = prezzo

    def setPrezzoPunti(self, prezzoPunti):
        self.prezzoPunti = prezzoPunti

    def setDisponibile(self, disponibile):
        self.disponibile = disponibile
    
    def setSpettacolo(self, spettacolo):
        self.Spettacolo = spettacolo

    def setTipo(self, tipo):
        self.tipo = tipo

    def setPosto(self, posto):
        self.posto = posto
