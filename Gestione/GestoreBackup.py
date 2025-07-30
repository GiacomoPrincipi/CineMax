import shutil

from PySide6.QtCore import QDate, QTime

class GestoreBackup():

    @staticmethod
    def backupDatiSistema():
        GestoreBackup.backupDatiUtenti()
        GestoreBackup.backupDatiArticoli()
        GestoreBackup.backupDatiSpettacoli()
        GestoreBackup.backupDatiPagamenti()
        GestoreBackup.backupDatiRecensioni()

    @staticmethod
    def backupDatiUtenti():
        fileOriginale = 'Dati/DatiClienti.pickle'
        fileCopia = f'Backup/BackupClientiDel{QDate.currentDate().toString("ddMMyyyy")}Alle{QTime.currentTime().toString("HHmmss")}.pickle'
        shutil.copy(fileOriginale, fileCopia)
        fileOriginale = 'Dati/DatiAmministratori.pickle'
        fileCopia = f'Backup/BackupAmministratoriDel{QDate.currentDate().toString("ddMMyyyy")}Alle{QTime.currentTime().toString("HHmmss")}.pickle'
        shutil.copy(fileOriginale, fileCopia)

    @staticmethod    
    def backupDatiArticoli():
        fileOriginale = 'Dati/DatiBiglietti.pickle'
        fileCopia = f'Backup/BackupBigliettiDel{QDate.currentDate().toString("ddMMyyyy")}Alle{QTime.currentTime().toString("HHmmss")}.pickle'
        shutil.copy(fileOriginale, fileCopia)
        fileOriginale = 'Dati/DatiProdotti.pickle'
        fileCopia = f'Backup/BackupProdottiDel{QDate.currentDate().toString("ddMMyyyy")}Alle{QTime.currentTime().toString("HHmmss")}.pickle'
        shutil.copy(fileOriginale, fileCopia)

    @staticmethod
    def backupDatiSpettacoli():
        fileOriginale = 'Dati/DatiSpettacoli.pickle'
        fileCopia = f'Backup/BackupSpettacoliDel{QDate.currentDate().toString("ddMMyyyy")}Alle{QTime.currentTime().toString("HHmmss")}.pickle'
        shutil.copy(fileOriginale, fileCopia)

    @staticmethod
    def backupDatiPagamenti():
        fileOriginale = 'Dati/DatiPagamenti.pickle'
        fileCopia = f'Backup/BackupPagamentiDel{QDate.currentDate().toString("ddMMyyyy")}Alle{QTime.currentTime().toString("HHmmss")}.pickle'
        shutil.copy(fileOriginale, fileCopia)

    @staticmethod
    def backupDatiRecensioni():
        fileOriginale = 'Dati/DatiRecensioni.pickle'
        fileCopia = f'Backup/BackupRecensioniDel{QDate.currentDate().toString("ddMMyyyy")}Alle{QTime.currentTime().toString("HHmmss")}.pickle'
        shutil.copy(fileOriginale, fileCopia)