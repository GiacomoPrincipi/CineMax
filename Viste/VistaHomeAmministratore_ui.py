# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaHomeAmministratore.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_VistaHomeAmministratore(object):
    def setupUi(self, VistaHomeAmministratore):
        if not VistaHomeAmministratore.objectName():
            VistaHomeAmministratore.setObjectName(u"VistaHomeAmministratore")
        VistaHomeAmministratore.resize(790, 499)
        self.pushButtonSpettacoli = QPushButton(VistaHomeAmministratore)
        self.pushButtonSpettacoli.setObjectName(u"pushButtonSpettacoli")
        self.pushButtonSpettacoli.setGeometry(QRect(180, 140, 201, 101))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButtonSpettacoli.setFont(font)
        self.pushButtonSpettacoli.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.Sfondo = QLabel(VistaHomeAmministratore)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 90, 791, 411))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font1)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #320F00,\n"
"        stop: 1 #641E00\n"
"    );\n"
"}")
        self.labelBarra = QLabel(VistaHomeAmministratore)
        self.labelBarra.setObjectName(u"labelBarra")
        self.labelBarra.setGeometry(QRect(0, 0, 791, 91))
        self.labelBarra.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #962D00,\n"
"        stop: 1 #B43700\n"
"    );\n"
"}")
        self.labelProfiloButtonAmministratore = QLabel(VistaHomeAmministratore)
        self.labelProfiloButtonAmministratore.setObjectName(u"labelProfiloButtonAmministratore")
        self.labelProfiloButtonAmministratore.setGeometry(QRect(710, 10, 63, 61))
        self.labelProfiloButtonAmministratore.setPixmap(QPixmap(u"Immagini/profiloButtonAmministratore.png"))
        self.labelProfiloButtonAmministratore.setScaledContents(True)
        self.labelProfiloAmministratore = QLabel(VistaHomeAmministratore)
        self.labelProfiloAmministratore.setObjectName(u"labelProfiloAmministratore")
        self.labelProfiloAmministratore.setGeometry(QRect(710, 70, 63, 20))
        self.labelProfiloAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #501400;\n"
"}")
        self.labelProfiloAmministratore.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLogoutAmministratore = QLabel(VistaHomeAmministratore)
        self.labelLogoutAmministratore.setObjectName(u"labelLogoutAmministratore")
        self.labelLogoutAmministratore.setGeometry(QRect(20, 70, 63, 20))
        self.labelLogoutAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #501400;\n"
"}")
        self.labelLogoutAmministratore.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLogoutButtonAmministratore = QLabel(VistaHomeAmministratore)
        self.labelLogoutButtonAmministratore.setObjectName(u"labelLogoutButtonAmministratore")
        self.labelLogoutButtonAmministratore.setGeometry(QRect(20, 10, 63, 61))
        self.labelLogoutButtonAmministratore.setPixmap(QPixmap(u"Immagini/LogoutButtonAmministratore.png"))
        self.labelLogoutButtonAmministratore.setScaledContents(True)
        self.labelBackup = QLabel(VistaHomeAmministratore)
        self.labelBackup.setObjectName(u"labelBackup")
        self.labelBackup.setGeometry(QRect(710, 460, 63, 20))
        self.labelBackup.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelBackup.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelBackupButtonAmministratore = QLabel(VistaHomeAmministratore)
        self.labelBackupButtonAmministratore.setObjectName(u"labelBackupButtonAmministratore")
        self.labelBackupButtonAmministratore.setGeometry(QRect(710, 390, 63, 61))
        self.labelBackupButtonAmministratore.setPixmap(QPixmap(u"Immagini/IconaBackupAmministratore.png"))
        self.labelBackupButtonAmministratore.setScaledContents(True)
        self.pushButtonProdotti = QPushButton(VistaHomeAmministratore)
        self.pushButtonProdotti.setObjectName(u"pushButtonProdotti")
        self.pushButtonProdotti.setGeometry(QRect(410, 140, 201, 101))
        self.pushButtonProdotti.setFont(font)
        self.pushButtonProdotti.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.pushButtonClienti = QPushButton(VistaHomeAmministratore)
        self.pushButtonClienti.setObjectName(u"pushButtonClienti")
        self.pushButtonClienti.setGeometry(QRect(180, 260, 201, 101))
        self.pushButtonClienti.setFont(font)
        self.pushButtonClienti.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.pushButtonAmministratori = QPushButton(VistaHomeAmministratore)
        self.pushButtonAmministratori.setObjectName(u"pushButtonAmministratori")
        self.pushButtonAmministratori.setGeometry(QRect(410, 260, 201, 101))
        self.pushButtonAmministratori.setFont(font)
        self.pushButtonAmministratori.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.pushButtonClientiRegistroCassa = QPushButton(VistaHomeAmministratore)
        self.pushButtonClientiRegistroCassa.setObjectName(u"pushButtonClientiRegistroCassa")
        self.pushButtonClientiRegistroCassa.setGeometry(QRect(180, 380, 201, 61))
        self.pushButtonClientiRegistroCassa.setFont(font)
        self.pushButtonClientiRegistroCassa.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.pushButtonClientiRecensioni = QPushButton(VistaHomeAmministratore)
        self.pushButtonClientiRecensioni.setObjectName(u"pushButtonClientiRecensioni")
        self.pushButtonClientiRecensioni.setGeometry(QRect(410, 380, 201, 61))
        self.pushButtonClientiRecensioni.setFont(font)
        self.pushButtonClientiRecensioni.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.labelTitolo = QLabel(VistaHomeAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(140, 10, 511, 71))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.labelTitolo.setFont(font2)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #501400;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Sfondo.raise_()
        self.pushButtonSpettacoli.raise_()
        self.labelBarra.raise_()
        self.labelProfiloButtonAmministratore.raise_()
        self.labelProfiloAmministratore.raise_()
        self.labelLogoutAmministratore.raise_()
        self.labelLogoutButtonAmministratore.raise_()
        self.labelBackup.raise_()
        self.labelBackupButtonAmministratore.raise_()
        self.pushButtonProdotti.raise_()
        self.pushButtonClienti.raise_()
        self.pushButtonAmministratori.raise_()
        self.pushButtonClientiRegistroCassa.raise_()
        self.pushButtonClientiRecensioni.raise_()
        self.labelTitolo.raise_()

        self.retranslateUi(VistaHomeAmministratore)

        QMetaObject.connectSlotsByName(VistaHomeAmministratore)
    # setupUi

    def retranslateUi(self, VistaHomeAmministratore):
        VistaHomeAmministratore.setWindowTitle(QCoreApplication.translate("VistaHomeAmministratore", u"Area Riservata Amministratore - CineMax", None))
        self.pushButtonSpettacoli.setText(QCoreApplication.translate("VistaHomeAmministratore", u"Spettacoli", None))
        self.Sfondo.setText("")
        self.labelBarra.setText("")
        self.labelProfiloButtonAmministratore.setText("")
        self.labelProfiloAmministratore.setText(QCoreApplication.translate("VistaHomeAmministratore", u"Profilo", None))
        self.labelLogoutAmministratore.setText(QCoreApplication.translate("VistaHomeAmministratore", u"Logout", None))
        self.labelLogoutButtonAmministratore.setText("")
        self.labelBackup.setText(QCoreApplication.translate("VistaHomeAmministratore", u"Backup", None))
        self.labelBackupButtonAmministratore.setText("")
        self.pushButtonProdotti.setText(QCoreApplication.translate("VistaHomeAmministratore", u"Prodotti", None))
        self.pushButtonClienti.setText(QCoreApplication.translate("VistaHomeAmministratore", u"Clienti", None))
        self.pushButtonAmministratori.setText(QCoreApplication.translate("VistaHomeAmministratore", u"Amministratori", None))
        self.pushButtonClientiRegistroCassa.setText(QCoreApplication.translate("VistaHomeAmministratore", u"Registo Cassa", None))
        self.pushButtonClientiRecensioni.setText(QCoreApplication.translate("VistaHomeAmministratore", u"Recensioni", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaHomeAmministratore", u"Area Riservata Amministratore", None))
    # retranslateUi

