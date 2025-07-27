class Spettacolo():
    
    def __init__(self, titolo, id, genere, sala, data, orarioInizio, orarioFine, durata):
        self.titolo = titolo
        self.id = id
        self.genere = genere
        self.sala = sala
        self.data = data
        self.orarioInizio = orarioInizio
        self.orarioFine = orarioFine
        self.durata = durata
        self.stato = True

    def getInfoSpettacolo(self):
        return {self.titolo, self.id, self.genere, self.sala, self.data, self.orarioInizio, self.orarioFine, self.durata, self.stato}

    def getTitolo(self):
        return self.titolo
    
    def getId(self):
        return self.id
    
    def getGenere(self):
        return self.genere
    
    def getSala(self):
        return self.sala
    
    def getData(self):
        return self.data
    
    def getOrarioInizio(self):
        return self.orarioInizio
    
    def getOrarioFine(self):
        return self.orarioFine
    
    def getDurata(self):
        return self.durata
    
    def getStato(self):
        return self.stato
    
    def getTestoStato(self):
        if self.stato == True:
            return "Attivo"
        if self.stato == False:
            return "Non Attivo"
    
    def setInfoSpettacolo(self, titolo, id, genere, sala, data, orarioInizio, orarioFine, durata, stato):
       self.setTitolo(titolo)
       self.setId(id)
       self.setGenere(genere)
       self.setSala(sala)
       self.setData(data)
       self.setOrarioInizio(orarioInizio)
       self.setOrarioFine(orarioFine)
       self.setDurata(durata)
       self.setStato(stato)

    def setTitolo(self, titolo):
        self.titolo = titolo

    def setId(self, id):
        self.id = id

    def setGenere(self, genere):
        self.genere = genere
    
    def setSala(self, sala):
        self.sala = sala

    def setData(self, data):
        self.data = data

    def setOrarioInizio(self, orarioInizio):
        self.orarioInizio = orarioInizio

    def setOrarioFine(self, orarioFine):
        self.orarioFine = orarioFine

    def setDurata(self, durata):
        self.durata = durata

    def setStato(self, stato):
        self.stato = stato

