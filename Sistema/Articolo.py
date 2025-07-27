from abc import abstractmethod

class Articolo():
    
    def __init__(self, id, prezzo, prezzoPunti, disponibile):
        self.id = id
        self.prezzo = prezzo
        self.prezzoPunti = prezzoPunti
        self.disponibile = disponibile

    def getInfoArticolo(self):
        return {self.id, self.prezzo, self.prezzoPunti, self.disponibile}
    
    @abstractmethod
    def getId(self):
        pass

    @abstractmethod
    def getPrezzo(self):
        pass

    @abstractmethod
    def getPrezzoPunti(self):
        pass
        
    @abstractmethod
    def getDisponibile(self):
        pass

    def setInfoArticolo(self, id, prezzo, prezzoPunti, disponibile):
        self.setId(id)
        self.setPrezzo(prezzo)
        self.setPrezzo(prezzoPunti)
        self.setDisponibile(disponibile)

    @abstractmethod
    def setId():
        pass
    
    @abstractmethod
    def setPrezzo(self, prezzo):
        pass

    @abstractmethod
    def setPrezzoPunti(self, prezzoPunti):
        pass

    @abstractmethod
    def setDisponibile(self, disponibile):
        pass
