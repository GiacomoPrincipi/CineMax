from abc import abstractmethod

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

    @abstractmethod
    def getNome(self):
        pass

    @abstractmethod
    def getCognome(self):
        pass

    @abstractmethod
    def getDataNascita(self):
        return self.dataNascita

    @abstractmethod
    def getEmail(self):
        pass

    @abstractmethod
    def getTelefono(self):
        pass

    @abstractmethod
    def getPassword(self):
        pass
    
    def setInfoUtente(self, nome, cognome, dataNascita, email, telefono, password):
       self.setNome(nome)
       self.setCognome(cognome)
       self.setDataNascita(dataNascita)
       self.setEmail(email)
       self.setTelefono(telefono)
       self.setPassword(password)

    @abstractmethod
    def setNome(self, nome):
        pass

    @abstractmethod
    def setCognome(self, cognome):
        pass

    @abstractmethod
    def setDataNascita(self, dataNascita):
        pass

    @abstractmethod
    def setEmail(self, email):
        pass

    @abstractmethod
    def setTelefono(self, telefono):
        pass

    @abstractmethod
    def setPassword(self, password):
        pass
