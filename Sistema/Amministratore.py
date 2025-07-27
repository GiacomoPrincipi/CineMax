from Sistema.Utente import Utente

class Amministratore(Utente):
    
    def __init__(self, nome, cognome, dataNascita, email, telefono, password, matricola):
        super().__init__(nome, cognome, dataNascita, email, telefono, password)
        self.matricola = matricola

    def getInfoAmministratore(self):
        return {self.nome, self.cognome, self.dataNascita, self.email, self.telefono, self.password, self.matricola}

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
    
    def getMatricola(self):
        return self.matricola
      
    def setInfoAmministratore(self, nome, cognome, dataNascita, email, telefono, password, matricola):
       self.setNome(nome)
       self.setCognome(cognome)
       self.setDataNascita(dataNascita)
       self.setEmail(email)
       self.setTelefono(telefono)
       self.setPassword(password)
       self.setMatricola(matricola)

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
    
    def setMatricola(self, matricola):
        self.matricola = matricola
