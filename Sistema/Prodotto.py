from Sistema.Articolo import Articolo

class Prodotto(Articolo):
    
    def __init__(self, prezzo, disponibile, nome, ingredienti, allergeni):
        super().__init__(prezzo, disponibile)
        self.nome = nome
        self.ingredienti = ingredienti
        self.allergeni = allergeni

    def getInfoProdotto(self):
        return {self.prezzo, self.disponibile, self.nome, self.ingredienti, self.allergeni}

    def getPrezzo(self):
        return self.prezzo

    def getDisponibile(self):
        return self.disponibile
    
    def getNome(self):
        return self.nome

    def getIngredienti(self):
        return self.ingredienti

    def getAllergeni(self):
        return self.allergeni

    def setInfoProdotto(self, prezzo, disponibile, nome, ingredienti, allergeni):
        self.setPrezzo(self, prezzo)
        self.setDisponibile(self, disponibile)
        self.setNome(self, nome)
        self.setIngredienti(self, ingredienti)
        self.setAllergeni(self, allergeni)

    def setPrezzo(self, prezzo):
        self.prezzo = prezzo

    def setDisponibile(self, disponibile):
        self.disponibile = disponibile

    def setNome(self, nome):
        self.nome = nome

    def setIngredienti(self, ingredienti):
        self.ingredienti = ingredienti

    def setAllergeni(self, allergeni):
        self.allergeni = allergeni

    def aggiungiIngrediente(self, ingrediente):
        self.ingredienti.append(ingrediente)

    def rimuoviIngrediente(self, ingrediente):
        self.ingredienti.remove(ingrediente)

    def aggiungiAllergene(self, allergene):
        self.allergeni.append(allergene)

    def rimuoviAllergene(self, allergene):
        self.allergeni.remove(allergene)