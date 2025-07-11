class Amministratore():
    def __init__(self, matricola):
        self.matricola = matricola

    def getInfoAmministratore(self):
        return {self.matricola}

    def getMatricola(self):
        return self.matricola

    def getDisponibile(self):
        return self.disponibile
      
    def setInfoArticolo(self, prezzo, disponibile):
        self.setPrezzo(self,Prezzo)
        self.setDisponibile(self,disponibile)

    def setPrezzo(self, prezzo: float):
        self.prezzo = prezzo

    def setTipo(self, disponibile: bool):
        self.disponibile = disponibile
