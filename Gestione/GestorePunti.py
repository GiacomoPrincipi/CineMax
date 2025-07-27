from Sistema.Cliente import Cliente

class GestorePunti():

    @staticmethod
    def controlloPunti(cliente, articolo):
        if cliente.getPunti() <= articolo.getPrezzoPunti():
            return False
        else: return True
    
    def controlloPuntiPunti(cliente, punti):
        if cliente.getPunti() <= punti:
            return False
        else: return True

    @staticmethod
    def aggiungiPunti(cliente, puntiDaAggiungere):
        puntiAggiornati = cliente.getPunti() + puntiDaAggiungere
        cliente.setPunti(puntiAggiornati)

    @staticmethod
    def rimuoviPunti(cliente, puntiDaRimuovere):
        puntiCliente = cliente.getPunti()
        puntiAggiornati = puntiCliente - puntiDaRimuovere
        cliente.setPunti(puntiAggiornati)

    @staticmethod
    def calcoloPunti(prezzo):
        punti = round(prezzo * 10)
        return punti