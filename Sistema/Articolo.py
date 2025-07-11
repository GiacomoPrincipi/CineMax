from abc import abstractmethod

class Articolo():
    def __init__(self, prezzo, disponibile):
        self.prezzo = prezzo
        self.disponibile = disponibile

    def getInfoArticolo(self):
        return {self.prezzo, self.disponibile}
    
    @abstractmethod
    def getPrezzo(self):
        pass
        
    @abstractmethod
    def getDisponibile(self):
        pass

    def setInfoArticolo(self, prezzo, disponibile):
        self.setPrezzo(self, prezzo)
        self.setDisponibile(self, disponibile)

    @abstractmethod
    def setPrezzo(self, prezzo):
        pass

    @abstractmethod
    def setDisponibile(self, disponibile):
        pass
