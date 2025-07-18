import shutil

class GestoreBackup():

    def backupDatiSistema(self):
        self.backupDatiUtenti()
        self.backupDatiArticoli()
        self.backupDatiSpettacoli()
        self.backupDatiPagamenti()
        self.backupDatiRecensioni()

    def backupDatiUtenti(data):
        fileOriginale = 'Dati/DatiClienti.pickle'
        fileCopia = f"Backup/BackupClientiDel{data}.pickle"
        shutil.copy(fileOriginale, fileCopia)
        fileOriginale = 'Dati/DatiAmministratori.pickle'
        fileCopia = f"Backup/BackupAmministratoriDel{data}.pickle"
        shutil.copy(fileOriginale, fileCopia)

    def backupDatiArticoli(data):
        fileOriginale = 'Dati/DatiBiglietti.pickle'
        fileCopia = f"Backup/BackupBigliettiDel{data}.pickle"
        shutil.copy(fileOriginale, fileCopia)
        fileOriginale = 'Dati/DatiProdotti.pickle'
        fileCopia = f"Backup/BackupProdottiDel{data}.pickle"
        shutil.copy(fileOriginale, fileCopia)

    def backupDatiSpettacoli(data):
        fileOriginale = 'Dati/DatiSpettacoli.pickle'
        fileCopia = f"Backup/BackupSpettacoliDel{data}.pickle"
        shutil.copy(fileOriginale, fileCopia)

    def backupDatiPagamenti(data):
        fileOriginale = 'Dati/DatiPagamenti.pickle'
        fileCopia = f"Backup/BackupPagamentiDel{data}.pickle"
        shutil.copy(fileOriginale, fileCopia)

    def backupDatiRecensioni(data):
        fileOriginale = 'Dati/DatiRecensioni.pickle'
        fileCopia = f"Backup/BackupRecensioniDel{data}.pickle"
        shutil.copy(fileOriginale, fileCopia)