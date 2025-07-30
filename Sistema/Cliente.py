from Sistema.Utente import Utente

class Cliente(Utente):
    
    def __init__(self, nome, cognome, dataNascita, email, telefono, password, codiceFiscale):
        super().__init__(nome, cognome, dataNascita, email, telefono, password)
        self.codiceFiscale = codiceFiscale
        self.punti = 0

    def __eq__(self, cliente):
        return isinstance(cliente, Cliente) and self.getCodiceFiscale() == cliente.getCodiceFiscale()
        
    def getInfoCliente(self):
        return {self.nome, self.cognome, self.dataNascita, self.email, self.telefono, self.password, self.codiceFiscale, self.punti}

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
    
    def getCodiceFiscale(self):
        return self.codiceFiscale
    
    def getPunti(self):
        return self.punti
    
    def setInfoCliente(self, nome, cognome, dataNascita, email, telefono, password, codiceFiscale, punti):
       self.setNome(nome)
       self.setCognome(cognome)
       self.setDataNascita(dataNascita)
       self.setEmail(email)
       self.setTelefono(telefono)
       self.setPassword(password)
       self.setCodiceFiscale(codiceFiscale)
       self.setPunti(punti)

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

    def setCodiceFiscale(self, codiceFiscale):
        self.codiceFiscale = codiceFiscale

    def setPunti(self, punti):
        self.punti = punti
