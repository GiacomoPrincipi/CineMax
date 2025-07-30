# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaModificaProfiloPersonaleAmministratore.ui'
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

class Ui_VistaModificaProfiloPersonaleAmministratore(object):
    def setupUi(self, VistaModificaProfiloPersonaleAmministratore):
        if not VistaModificaProfiloPersonaleAmministratore.objectName():
            VistaModificaProfiloPersonaleAmministratore.setObjectName(u"VistaModificaProfiloPersonaleAmministratore")
        VistaModificaProfiloPersonaleAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #210A00,\n"
"        stop: 1 #7D2100\n"
"    );\n"
"}")
        self.labelProfilo = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelProfilo.setObjectName(u"labelProfilo")
        self.labelProfilo.setGeometry(QRect(30, 30, 121, 121))
        self.labelProfilo.setPixmap(QPixmap(u"Viste/Immagini/profiloButtonAmministratore.png"))
        self.labelProfilo.setScaledContents(True)
        self.labelNome = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 431, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #D7320C;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCognome = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataNascita = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelDataNascita.setObjectName(u"labelDataNascita")
        self.labelDataNascita.setGeometry(QRect(520, 100, 121, 20))
        self.labelDataNascita.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelDataNascita.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmail = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(30, 250, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefono = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(30, 320, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditEmail = QLineEdit(VistaModificaProfiloPersonaleAmministratore)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setGeometry(QRect(30, 280, 251, 26))
        self.lineEditEmail.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditTelefono = QLineEdit(VistaModificaProfiloPersonaleAmministratore)
        self.lineEditTelefono.setObjectName(u"lineEditTelefono")
        self.lineEditTelefono.setGeometry(QRect(30, 350, 101, 26))
        self.lineEditTelefono.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditNome = QLineEdit(VistaModificaProfiloPersonaleAmministratore)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setGeometry(QRect(180, 130, 131, 26))
        self.lineEditNome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditCognome = QLineEdit(VistaModificaProfiloPersonaleAmministratore)
        self.lineEditCognome.setObjectName(u"lineEditCognome")
        self.lineEditCognome.setGeometry(QRect(330, 130, 171, 26))
        self.lineEditCognome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.pushButtonConferma = QPushButton(VistaModificaProfiloPersonaleAmministratore)
        self.pushButtonConferma.setObjectName(u"pushButtonConferma")
        self.pushButtonConferma.setGeometry(QRect(670, 440, 91, 29))
        self.pushButtonConferma.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.pushButtonAnnulla = QPushButton(VistaModificaProfiloPersonaleAmministratore)
        self.pushButtonAnnulla.setObjectName(u"pushButtonAnnulla")
        self.pushButtonAnnulla.setGeometry(QRect(560, 440, 91, 29))
        self.pushButtonAnnulla.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.labelMatricola = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelMatricola.setObjectName(u"labelMatricola")
        self.labelMatricola.setGeometry(QRect(30, 180, 81, 20))
        self.labelMatricola.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelMatricola.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelMatricolaAmministratore = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelMatricolaAmministratore.setObjectName(u"labelMatricolaAmministratore")
        self.labelMatricolaAmministratore.setGeometry(QRect(30, 210, 111, 20))
        self.labelMatricolaAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelPassword = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(30, 400, 81, 20))
        self.labelPassword.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditPassword = QLineEdit(VistaModificaProfiloPersonaleAmministratore)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(30, 430, 191, 26))
        self.lineEditPassword.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.labelConfermaPassword = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelConfermaPassword.setObjectName(u"labelConfermaPassword")
        self.labelConfermaPassword.setGeometry(QRect(260, 400, 141, 20))
        self.labelConfermaPassword.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelConfermaPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditConfermaPassword = QLineEdit(VistaModificaProfiloPersonaleAmministratore)
        self.lineEditConfermaPassword.setObjectName(u"lineEditConfermaPassword")
        self.lineEditConfermaPassword.setGeometry(QRect(260, 430, 191, 26))
        self.lineEditConfermaPassword.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.dateEditDataNascita = QDateEdit(VistaModificaProfiloPersonaleAmministratore)
        self.dateEditDataNascita.setObjectName(u"dateEditDataNascita")
        self.dateEditDataNascita.setGeometry(QRect(520, 130, 110, 26))
        self.dateEditDataNascita.setStyleSheet(u"QDateEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"")
        self.dateEditDataNascita.setDateTime(QDateTime(QDate(1950, 1, 1), QTime(22, 0, 0)))
        self.dateEditDataNascita.setTime(QTime(22, 0, 0))
        self.dateEditDataNascita.setMaximumDateTime(QDateTime(QDate(2050, 12, 12), QTime(16, 59, 59)))
        self.dateEditDataNascita.setMinimumDateTime(QDateTime(QDate(1949, 12, 31), QTime(19, 0, 0)))
        self.labelErroreNome = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelErroreNome.setObjectName(u"labelErroreNome")
        self.labelErroreNome.setGeometry(QRect(180, 160, 121, 20))
        self.labelErroreNome.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreCognome = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelErroreCognome.setObjectName(u"labelErroreCognome")
        self.labelErroreCognome.setGeometry(QRect(330, 160, 151, 20))
        self.labelErroreCognome.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreDataNascita = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelErroreDataNascita.setObjectName(u"labelErroreDataNascita")
        self.labelErroreDataNascita.setGeometry(QRect(520, 160, 121, 20))
        self.labelErroreDataNascita.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreDataNascita.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreEmail = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelErroreEmail.setObjectName(u"labelErroreEmail")
        self.labelErroreEmail.setGeometry(QRect(290, 280, 121, 20))
        self.labelErroreEmail.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreTelefono = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelErroreTelefono.setObjectName(u"labelErroreTelefono")
        self.labelErroreTelefono.setGeometry(QRect(150, 350, 211, 20))
        self.labelErroreTelefono.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErrorePassword = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelErrorePassword.setObjectName(u"labelErrorePassword")
        self.labelErrorePassword.setGeometry(QRect(30, 460, 141, 20))
        self.labelErrorePassword.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErrorePassword.setText(u"")
        self.labelErrorePassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreConfermaPassword = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelErroreConfermaPassword.setObjectName(u"labelErroreConfermaPassword")
        self.labelErroreConfermaPassword.setGeometry(QRect(260, 460, 221, 20))
        self.labelErroreConfermaPassword.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreConfermaPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErrorePassword2 = QLabel(VistaModificaProfiloPersonaleAmministratore)
        self.labelErrorePassword2.setObjectName(u"labelErrorePassword2")
        self.labelErrorePassword2.setGeometry(QRect(30, 380, 681, 20))
        font2 = QFont()
        font2.setPointSize(7)
        self.labelErrorePassword2.setFont(font2)
        self.labelErrorePassword2.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErrorePassword2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(VistaModificaProfiloPersonaleAmministratore)

        QMetaObject.connectSlotsByName(VistaModificaProfiloPersonaleAmministratore)
    # setupUi

    def retranslateUi(self, VistaModificaProfiloPersonaleAmministratore):
        VistaModificaProfiloPersonaleAmministratore.setWindowTitle(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Modifica Profilo Personale - CineMax", None))
        self.Sfondo.setText("")
        self.labelProfilo.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Modifica Profilo Personale", None))
        self.labelCognome.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Cognome:", None))
        self.labelDataNascita.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Data di Nascita:", None))
        self.labelEmail.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Email:", None))
        self.labelTelefono.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Telefono:", None))
        self.lineEditEmail.setText("")
        self.lineEditTelefono.setText("")
        self.lineEditNome.setText("")
        self.lineEditCognome.setText("")
        self.pushButtonConferma.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Conferma", None))
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Annulla", None))
        self.labelMatricola.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Matricola:", None))
        self.labelMatricolaAmministratore.setText("")
        self.labelPassword.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Password:", None))
        self.lineEditPassword.setText("")
        self.labelConfermaPassword.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleAmministratore", u"Conferma Password:", None))
        self.lineEditConfermaPassword.setText("")
        self.labelErroreNome.setText("")
        self.labelErroreCognome.setText("")
        self.labelErroreDataNascita.setText("")
        self.labelErroreEmail.setText("")
        self.labelErroreTelefono.setText("")
        self.labelErroreConfermaPassword.setText("")
        self.labelErrorePassword2.setText("")
    # retranslateUi

