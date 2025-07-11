class Prodotto():
    def __init__(self, nome, ingredienti, allergeni):
        self.nome = nome
        self.ingredienti = ingredienti
        self.allergeni = allergeni

    def getInfoProdotto(self):
        return {self.nome, self.ingredienti, self.allergeni}

    def getNome(self):
        return self.nome

    def getIngredienti(self):
        return self.ingredienti

    def getAllergeni(self):
        return self.allergeni

    def setInfoProdotto(self, nome, ingredienti, allergeni):
        self.setNome(self, nome)
        self.setIngredienti(self, ingredienti)
        self.setAllergeni(self, allergeni)

    def setNome(self, nome: string):
        self.Spettacolo = spettacolo

    def setIngredienti(self, ingredienti: ArrayList<string>):
        self.ingredienti = ingredienti

    def setAllergeni(self, allergeni: ArrayList<string>):
        self.posto = posto
