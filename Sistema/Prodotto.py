from Sistema.Articolo import Articolo

class Prodotto(Articolo):
    
    def __init__(self, id, prezzo, prezzoPunti, disponibile, nome, ingredienti, allergeni):
        super().__init__(id, prezzo, prezzoPunti, disponibile)
        self.nome = nome
        self.ingredienti = ingredienti
        self.allergeni = allergeni

    def getInfoProdotto(self):
        return {self.id, self.prezzo, self.prezzoPunti, self.disponibile, self.nome, self.ingredienti, self.allergeni}

    def getId(self):
        return self.id
    
    def getPrezzo(self):
        return self.prezzo
    
    def getPrezzoPunti(self):
        return self.prezzoPunti

    def getDisponibile(self):
        return self.disponibile
    
    def getNome(self):
        return self.nome

    def getIngredienti(self):
        return self.ingredienti

    def getAllergeni(self):
        return self.allergeni

    def setInfoProdotto(self, id, prezzo, prezzoPunti, disponibile, nome, ingredienti, allergeni):
        self.setId(id)
        self.setPrezzo(prezzo)
        self.setPrezzoPunti(prezzoPunti)
        self.setDisponibile(disponibile)
        self.setNome(nome)
        self.setIngredienti(ingredienti)
        self.setAllergeni(allergeni)

    def setId(self, id):
        self.id = id

    def setPrezzo(self, prezzo):
        self.prezzo = prezzo

    def setPrezzoPunti(self, prezzoPunti):
        self.prezzoPunti = prezzoPunti

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

    def getTestoDisponibile(self):
        if self.getDisponibile() == True:
            return "Si"
        else: return "No"