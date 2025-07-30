from email.message import EmailMessage
import re
import dns.resolver
import smtplib
import random
import string

class GestoreAutenticazione():

    def __init__(self):
        self.amministratoreAutenticato = None
        self.clienteAutenticato = None

    def loginAmministratore(self, amministratore):
        self.amministratoreAutenticato = amministratore

    def loginCliente(self, cliente):
        self.clienteAutenticato = cliente

    def logoutAmministratore(self):
        self.amministratoreAutenticato = None

    def logoutCliente(self):
        self.clienteAutenticato = None

    @staticmethod
    def controlloEmail(listaUtente, emailInserita):
        esito = False
        for utente in listaUtente:
            if emailInserita == utente.getEmail():
                esito = True
                break
        return esito
    
    @staticmethod
    def controlloPassword(utente, passwordInserita):
        if passwordInserita == utente.getPassword():
            return True
        else: return False

    @staticmethod
    def invioEmailRecuperoPassword(utente):
        mittente = "cinemax.ripristino@gmail.com"
        passwordMittente = "tuqc wjxn igxy crjo"
        destinatario = utente.getEmail()
        passwordDestinatario = GestoreAutenticazione.generaPassword()
        utente.setPassword(passwordDestinatario)
        oggetto = "Recupero Password"
        testo = f"Salve,\nla informiamo che la sua password è stata cambiata in: {passwordDestinatario}.\n\nLa direzione."
        email = EmailMessage()
        email["From"] = mittente
        email["To"] = destinatario
        email["Subject"] = oggetto
        email.set_content(testo)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(mittente, passwordMittente)
            server.send_message(email)

    @staticmethod
    def generaPassword():
        lunghezza = 8
        lettereMinuscole = string.ascii_lowercase
        lettereMaiuscole = string.ascii_uppercase
        numeri = string.digits
        simboli = "!?#@"
        caratteri = lettereMinuscole + lettereMaiuscole + numeri + simboli
        caratteriObbligatori = [random.choice(lettereMaiuscole), random.choice(numeri), random.choice(simboli)]
        caratteriRimanenti = [random.choice(caratteri) for _ in range(lunghezza - len(caratteriObbligatori))]
        nuovaPassword = caratteriObbligatori + caratteriRimanenti
        random.shuffle(nuovaPassword)
        return "".join(nuovaPassword)
    
    @staticmethod
    def controlloStrutturaPassword(password):
        numero = False
        maiuscola = False
        simbolo = False
        simboliIdonei = "!?#@"

        if len(password) < 8:
            return False
        
        for carattere in password:
            if carattere.isdigit():
                numero = True
            if carattere.isupper():
                maiuscola = True
            if carattere in simboliIdonei:
                simbolo = True
            if carattere  == " ":
                return False
        
        if numero and maiuscola and simbolo: return True
        else: return False

    @staticmethod
    def controlloStrutturaEmail(email):
        struttura = r"^[\w\.-]+@([\w\-]+\.[\w\-]+)$"
        compatibile = re.match(struttura, email)
        if not compatibile:
            return False

        dominio = compatibile.group(1)
        try:
            dns.resolver.resolve(dominio, 'MX')
            return True
        except: return False
        