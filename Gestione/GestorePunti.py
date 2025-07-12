from Sistema.Cliente import Cliente

class GestorePunti():

    def controlloPunti(cliente, articolo):
        if cliente.getPunti() <= articolo.getPrezzo():
            return False
        else: return True

    def aggiungiPunti(cliente, puntiDaAggiungere):
        puntiAggiornati = cliente.getPunti() + puntiDaAggiungere
        cliente.setPunti(puntiAggiornati)

    def rimuoviPunti(cliente, puntiDaRimuovere):
        puntiCliente = cliente.getPunti()
        puntiAggiornati = puntiCliente - puntiDaRimuovere
        cliente.setPunti(puntiAggiornati)