from Sistema import Cliente
from Sistema import Amministratore

from email.message import EmailMessage

import smtplib
import random
import string

class GestoreAutenticazione():

    def controlloEmail(listaUtente, emailInserita):
        for utente in listaUtente:
            if emailInserita == utente.getEmail():
                return utente

    def controlloPassword(utente, passwordInserita):
        if passwordInserita == utente.getPassword():
            return True
        else: return False


    def invioEmailRecuperoPassword(self, utente):
        mittente = "cinemax.ripristino@gmail.com"
        passwordMittente = "CineMaxRispristino1#"
        destinatario = utente.getEmail()
        passwordDestinatario = self.generaPassword()
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

    def generaPassword():
        lunghezza = 8
        lettereMinuscole = string.ascii_lowercase
        lettereMaiuscole = string.ascii_uppercase
        numeri = string.digits
        simboli = "!?#@"
        caratteri = lettereMinuscole + lettereMaiuscole + numeri + simboli
        caratteriObbligatori = [random.choice(lettereMaiuscole), random.choice(numeri), random.choice(simboli)]
        caratteriRimanenti = random.choice(caratteri), lunghezza - len(caratteriObbligatori)
        nuovaPassword = random.shuffle(caratteriObbligatori + caratteriRimanenti)
        return nuovaPassword