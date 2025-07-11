class Spettacolo():
    def __init__(self, nome, cognome, dataNascita, email, telefono, password):
        self.nome = nome
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.email = email
        self.telefono = telefono
        self.password = password

    def getInfoUtente(self):
        return {self.nome, self.cognome, self.dataNascita, self.email, self.telefono, self.password}

    def getNome(self):
        return self.nome
    
    def getCognome(self):
        return self.cognome
    
    def getDataNascita(self):
        return self.dataNascita
    
    def getEmail(self):
        return self.email
    
    def getTelefono(self):
        return self.telefono
    
    def getPassword(self):
        return self.password
    
    def setInfoSpettacolo(self, titolo, genere, sala, data, orarioInizio, orarioFine, durata):
       self.setTitolo(self, titolo)
       self.setGenere(self, genere)
       self.setSala(self, sala)
       self.setData(self, data)
       self.setOrarioInizio(self, orarioInizio)
       self.setOrarioFine(self, orarioFine)
       self.setDurata(self, durata)

    def setTitolo(self, titolo: string):
        self.titolo = titolo

    def setGenere(self, genere: string):
        self.genere = genere
    
    def setSala(self, sala: int):
        self.sala = sala

    def setData(self, data: Data):
        self.data = data

    def setOrarioInizio(self, orarioInizio: Ora):
        self.orarioInizio = orarioInizio

    def setOrarioFine(self, orarioFine: Ora):
        self.orarioFine = orarioFine

    def setDurata(self, durata: int):
        self.durata = durata
