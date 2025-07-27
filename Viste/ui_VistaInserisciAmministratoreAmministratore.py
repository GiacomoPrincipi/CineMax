# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaInserisciAmministratoreAmministratore.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_VistaInserisciAmministratoreAmministratore(object):
    def setupUi(self, VistaInserisciAmministratoreAmministratore):
        if not VistaInserisciAmministratoreAmministratore.objectName():
            VistaInserisciAmministratoreAmministratore.setObjectName(u"VistaInserisciAmministratoreAmministratore")
        VistaInserisciAmministratoreAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaInserisciAmministratoreAmministratore)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #320F00,\n"
"        stop: 1 #641E00\n"
"    );\n"
"}")
        self.labelProfilo = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelProfilo.setObjectName(u"labelProfilo")
        self.labelProfilo.setGeometry(QRect(40, 30, 121, 121))
        self.labelProfilo.setPixmap(QPixmap(u"Immagini/profiloButtonAmministratore.png"))
        self.labelProfilo.setScaledContents(True)
        self.labelNome = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 431, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCognome = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelMatricola = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelMatricola.setObjectName(u"labelMatricola")
        self.labelMatricola.setGeometry(QRect(40, 180, 81, 20))
        self.labelMatricola.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelMatricola.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmail = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(40, 240, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefono = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(40, 300, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditEmail = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setGeometry(QRect(40, 260, 231, 26))
        self.lineEditEmail.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditTelefono = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditTelefono.setObjectName(u"lineEditTelefono")
        self.lineEditTelefono.setGeometry(QRect(40, 330, 111, 26))
        self.lineEditTelefono.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditMatricola = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditMatricola.setObjectName(u"lineEditMatricola")
        self.lineEditMatricola.setGeometry(QRect(40, 200, 81, 26))
        self.lineEditMatricola.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditNome = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setGeometry(QRect(180, 120, 131, 26))
        self.lineEditNome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditCognome = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditCognome.setObjectName(u"lineEditCognome")
        self.lineEditCognome.setGeometry(QRect(330, 120, 191, 26))
        self.lineEditCognome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.pushButtonConferma = QPushButton(VistaInserisciAmministratoreAmministratore)
        self.pushButtonConferma.setObjectName(u"pushButtonConferma")
        self.pushButtonConferma.setGeometry(QRect(680, 450, 91, 29))
        self.pushButtonConferma.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.pushButtonAnnulla = QPushButton(VistaInserisciAmministratoreAmministratore)
        self.pushButtonAnnulla.setObjectName(u"pushButtonAnnulla")
        self.pushButtonAnnulla.setGeometry(QRect(570, 450, 91, 29))
        self.pushButtonAnnulla.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.labelDataNascita = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelDataNascita.setObjectName(u"labelDataNascita")
        self.labelDataNascita.setGeometry(QRect(580, 100, 121, 20))
        self.labelDataNascita.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelDataNascita.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.dateEditDataNascita = QDateEdit(VistaInserisciAmministratoreAmministratore)
        self.dateEditDataNascita.setObjectName(u"dateEditDataNascita")
        self.dateEditDataNascita.setGeometry(QRect(580, 120, 110, 26))
        self.dateEditDataNascita.setStyleSheet(u"QDateEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"	transition: border-color 1.5s ease;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border-color:#FF3C00;\n"
"	transition: border-color 1.5s ease;\n"
"}\n"
"\n"
"")
        self.dateEditDataNascita.setDateTime(QDateTime(QDate(1950, 1, 1), QTime(22, 0, 0)))
        self.dateEditDataNascita.setTime(QTime(22, 0, 0))
        self.dateEditDataNascita.setMaximumDateTime(QDateTime(QDate(2050, 12, 12), QTime(16, 59, 59)))
        self.dateEditDataNascita.setMinimumDateTime(QDateTime(QDate(1949, 12, 31), QTime(19, 0, 0)))
        self.labelPassword = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(40, 390, 81, 20))
        self.labelPassword.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditPassword = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(40, 410, 191, 26))
        self.lineEditPassword.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.labelConfermaPassword = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelConfermaPassword.setObjectName(u"labelConfermaPassword")
        self.labelConfermaPassword.setGeometry(QRect(320, 390, 141, 20))
        self.labelConfermaPassword.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelConfermaPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditConfermaPassword = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditConfermaPassword.setObjectName(u"lineEditConfermaPassword")
        self.lineEditConfermaPassword.setGeometry(QRect(320, 410, 191, 26))
        self.lineEditConfermaPassword.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.labelErroreNome = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelErroreNome.setObjectName(u"labelErroreNome")
        self.labelErroreNome.setGeometry(QRect(180, 150, 121, 20))
        self.labelErroreNome.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreCognome = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelErroreCognome.setObjectName(u"labelErroreCognome")
        self.labelErroreCognome.setGeometry(QRect(330, 150, 151, 20))
        self.labelErroreCognome.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreDataNascita = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelErroreDataNascita.setObjectName(u"labelErroreDataNascita")
        self.labelErroreDataNascita.setGeometry(QRect(580, 150, 121, 20))
        self.labelErroreDataNascita.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreDataNascita.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreEmail = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelErroreEmail.setObjectName(u"labelErroreEmail")
        self.labelErroreEmail.setGeometry(QRect(280, 260, 121, 20))
        self.labelErroreEmail.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreTelefono = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelErroreTelefono.setObjectName(u"labelErroreTelefono")
        self.labelErroreTelefono.setGeometry(QRect(160, 330, 211, 20))
        self.labelErroreTelefono.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErrorePassword2 = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelErrorePassword2.setObjectName(u"labelErrorePassword2")
        self.labelErrorePassword2.setGeometry(QRect(40, 360, 681, 20))
        font2 = QFont()
        font2.setPointSize(7)
        self.labelErrorePassword2.setFont(font2)
        self.labelErrorePassword2.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErrorePassword2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErrorePassword = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelErrorePassword.setObjectName(u"labelErrorePassword")
        self.labelErrorePassword.setGeometry(QRect(110, 390, 141, 20))
        self.labelErrorePassword.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErrorePassword.setText(u"")
        self.labelErrorePassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreConfermaPassword = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelErroreConfermaPassword.setObjectName(u"labelErroreConfermaPassword")
        self.labelErroreConfermaPassword.setGeometry(QRect(460, 390, 221, 20))
        self.labelErroreConfermaPassword.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreConfermaPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreMatricola = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelErroreMatricola.setObjectName(u"labelErroreMatricola")
        self.labelErroreMatricola.setGeometry(QRect(130, 200, 151, 20))
        self.labelErroreMatricola.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreMatricola.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(VistaInserisciAmministratoreAmministratore)

        QMetaObject.connectSlotsByName(VistaInserisciAmministratoreAmministratore)
    # setupUi

    def retranslateUi(self, VistaInserisciAmministratoreAmministratore):
        VistaInserisciAmministratoreAmministratore.setWindowTitle(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Inserisci Amministratore - CineMax", None))
        self.Sfondo.setText("")
        self.labelProfilo.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Inserisci Amministratore", None))
        self.labelCognome.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Cognome:", None))
        self.labelMatricola.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Matricola:", None))
        self.labelEmail.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Email:", None))
        self.labelTelefono.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Telefono:", None))
        self.lineEditEmail.setText("")
        self.lineEditTelefono.setText("")
        self.lineEditMatricola.setText("")
        self.lineEditNome.setText("")
        self.lineEditCognome.setText("")
        self.pushButtonConferma.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Conferma", None))
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Annulla", None))
        self.labelDataNascita.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Data di Nascita:", None))
        self.labelPassword.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Password:", None))
        self.lineEditPassword.setText("")
        self.labelConfermaPassword.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Conferma Password:", None))
        self.lineEditConfermaPassword.setText("")
        self.labelErroreNome.setText("")
        self.labelErroreCognome.setText("")
        self.labelErroreDataNascita.setText("")
        self.labelErroreEmail.setText("")
        self.labelErroreTelefono.setText("")
        self.labelErrorePassword2.setText("")
        self.labelErroreConfermaPassword.setText("")
        self.labelErroreMatricola.setText("")
    # retranslateUi

