class Utente():
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
    
    def setInfoUtente(self, nome, cognome, dataNascita, email, telefono, password):
       self.setNome(self, nome)
       self.setCognome(self, cognome)
       self.setDataNascita(self, dataNascita)
       self.setEmail(self, email)
       self.setTelefono(self, telefono)
       self.setPassword(self, password)

    def setNome(self, nome):
        self.nome = nome

    def setCognome(self, cognome):
        self.cognome = cognome
    
    def setDataNascita(self, dataNascita):
        self.dataNascita = dataNascita

    def setEmail(self, email):
        self.email = email

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setPassword(self, password):
        self.password = password
