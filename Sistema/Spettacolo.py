class Spettacolo():

    def __init__(self, titolo, genere, sala, data, orarioInizio, orarioFine, durata):

        self.titolo = titolo
        self.genere = genere
        self.sala = sala
        self.data = data
        self.orarioInizio = orarioInizio
        self.orarioFine = orarioFine
        self.durata = durata


    def getInfoSpettacolo(self):

        return {self.titolo, self.genere, self.sala, self.data, self.orarioInizio, self.orarioFine, self.durata}
    

    def getTitolo(self):

        return self.titolo
    

    def getGenere(self):

        return self.genere
    

    def getSala(self):

        return self.sala
    

    def getData(self):

        return self.data
    

    def getOrarioInizio(self):

        return self.orarioInizio
    
    def gerOrarioFine(self):

        return self.orarioFine
    

    def getDurata(self):

        return self.durata
    

    def setInfoSpettacolo(self, titolo, genere, sala, data, orarioInizio, orarioFine, durata):

       self.setTitolo(self, titolo)
       self.setGenere(self, genere)
       self.setSala(self, sala)
       self.setData(self, data)
       self.setOrarioInizio(self, orarioInizio)
       self.setOrarioFine(self, orarioFine)
       self.setDurata(self, durata)


    def setTitolo(self, titolo):

        self.titolo = titolo


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
