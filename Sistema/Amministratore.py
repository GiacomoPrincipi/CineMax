class Amministratore():
    def __init__(self, matricola):
        self.matricola = matricola

    def getInfoAmministratore(self):
        return {self.matricola}

    def getMatricola(self):
        return self.matricola
      
    def setInfoAmministratore(self, matricola):
        self.setMatricola(self, matricola)
        
    def setMatricola(self, matricola: string):
        self.matricola = matricola
