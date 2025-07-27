# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaModificaProfiloPersonaleCliente.ui'
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

class Ui_VistaModificaProfiloPersonaleCliente(object):
    def setupUi(self, VistaModificaProfiloPersonaleCliente):
        if not VistaModificaProfiloPersonaleCliente.objectName():
            VistaModificaProfiloPersonaleCliente.setObjectName(u"VistaModificaProfiloPersonaleCliente")
        VistaModificaProfiloPersonaleCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaModificaProfiloPersonaleCliente)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"                stop: 0 #321E00,\n"
"        stop: 1 #643C00\n"
"    );\n"
"}")
        self.labelProfilo = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelProfilo.setObjectName(u"labelProfilo")
        self.labelProfilo.setGeometry(QRect(40, 30, 121, 121))
        self.labelProfilo.setPixmap(QPixmap(u"Immagini/profiloButtonCliente.png"))
        self.labelProfilo.setScaledContents(True)
        self.labelNome = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 441, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C8B400;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCognome = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCodiceFiscale = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelCodiceFiscale.setObjectName(u"labelCodiceFiscale")
        self.labelCodiceFiscale.setGeometry(QRect(40, 180, 111, 20))
        self.labelCodiceFiscale.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelCodiceFiscale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmail = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(40, 260, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefono = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(40, 340, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPassword = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(40, 420, 81, 20))
        self.labelPassword.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButtonConferma = QPushButton(VistaModificaProfiloPersonaleCliente)
        self.pushButtonConferma.setObjectName(u"pushButtonConferma")
        self.pushButtonConferma.setGeometry(QRect(670, 450, 91, 29))
        self.pushButtonConferma.setStyleSheet(u"QPushButton {\n"
"    background-color: #963C00;\n"
"    color: #FF7800;\n"
"    border: 2px solid #502800;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C86400;\n"
"}\n"
"")
        self.lineEditEmail = QLineEdit(VistaModificaProfiloPersonaleCliente)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setGeometry(QRect(40, 290, 251, 26))
        self.lineEditEmail.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditNome = QLineEdit(VistaModificaProfiloPersonaleCliente)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setGeometry(QRect(180, 130, 121, 26))
        self.lineEditNome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditCognome = QLineEdit(VistaModificaProfiloPersonaleCliente)
        self.lineEditCognome.setObjectName(u"lineEditCognome")
        self.lineEditCognome.setGeometry(QRect(330, 130, 171, 26))
        self.lineEditCognome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditTelefono = QLineEdit(VistaModificaProfiloPersonaleCliente)
        self.lineEditTelefono.setObjectName(u"lineEditTelefono")
        self.lineEditTelefono.setGeometry(QRect(40, 370, 121, 26))
        self.lineEditTelefono.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.pushButtonAnnulla = QPushButton(VistaModificaProfiloPersonaleCliente)
        self.pushButtonAnnulla.setObjectName(u"pushButtonAnnulla")
        self.pushButtonAnnulla.setGeometry(QRect(560, 450, 91, 29))
        self.pushButtonAnnulla.setStyleSheet(u"QPushButton {\n"
"    background-color: #963C00;\n"
"    color: #FF7800;\n"
"    border: 2px solid #502800;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C86400;\n"
"}\n"
"")
        self.lineEditPassword = QLineEdit(VistaModificaProfiloPersonaleCliente)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(40, 450, 191, 26))
        self.lineEditPassword.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditConfermaPassword = QLineEdit(VistaModificaProfiloPersonaleCliente)
        self.lineEditConfermaPassword.setObjectName(u"lineEditConfermaPassword")
        self.lineEditConfermaPassword.setGeometry(QRect(260, 450, 191, 26))
        self.lineEditConfermaPassword.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.labelConfermaPassword = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelConfermaPassword.setObjectName(u"labelConfermaPassword")
        self.labelConfermaPassword.setGeometry(QRect(260, 420, 141, 20))
        self.labelConfermaPassword.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelConfermaPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.dateEditDataNascita = QDateEdit(VistaModificaProfiloPersonaleCliente)
        self.dateEditDataNascita.setObjectName(u"dateEditDataNascita")
        self.dateEditDataNascita.setGeometry(QRect(540, 130, 110, 26))
        self.dateEditDataNascita.setStyleSheet(u"QDateEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"	transition: border-color 1.5s ease;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border-color: #FF7800;\n"
"	transition: border-color 1.5s ease;\n"
"}\n"
"\n"
"")
        self.dateEditDataNascita.setDateTime(QDateTime(QDate(1950, 1, 1), QTime(22, 0, 0)))
        self.dateEditDataNascita.setTime(QTime(22, 0, 0))
        self.dateEditDataNascita.setMaximumDateTime(QDateTime(QDate(2050, 12, 12), QTime(20, 59, 59)))
        self.dateEditDataNascita.setMinimumDateTime(QDateTime(QDate(1949, 12, 31), QTime(23, 0, 0)))
        self.labelDataNascita = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelDataNascita.setObjectName(u"labelDataNascita")
        self.labelDataNascita.setGeometry(QRect(540, 100, 121, 20))
        self.labelDataNascita.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelDataNascita.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreNome = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelErroreNome.setObjectName(u"labelErroreNome")
        self.labelErroreNome.setGeometry(QRect(180, 160, 121, 20))
        self.labelErroreNome.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00\n"
"}")
        self.labelErroreNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreCognome = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelErroreCognome.setObjectName(u"labelErroreCognome")
        self.labelErroreCognome.setGeometry(QRect(330, 160, 151, 20))
        self.labelErroreCognome.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00\n"
"}")
        self.labelErroreCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreDataNascita = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelErroreDataNascita.setObjectName(u"labelErroreDataNascita")
        self.labelErroreDataNascita.setGeometry(QRect(540, 160, 121, 20))
        self.labelErroreDataNascita.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00\n"
"}")
        self.labelErroreDataNascita.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreEmail = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelErroreEmail.setObjectName(u"labelErroreEmail")
        self.labelErroreEmail.setGeometry(QRect(300, 290, 121, 20))
        self.labelErroreEmail.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00\n"
"}")
        self.labelErroreEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreTelefono = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelErroreTelefono.setObjectName(u"labelErroreTelefono")
        self.labelErroreTelefono.setGeometry(QRect(170, 370, 211, 20))
        self.labelErroreTelefono.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00\n"
"}")
        self.labelErroreTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErrorePassword = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelErrorePassword.setObjectName(u"labelErrorePassword")
        self.labelErrorePassword.setGeometry(QRect(110, 420, 141, 20))
        self.labelErrorePassword.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00\n"
"}")
        self.labelErrorePassword.setText(u"")
        self.labelErrorePassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreConfermaPassword = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelErroreConfermaPassword.setObjectName(u"labelErroreConfermaPassword")
        self.labelErroreConfermaPassword.setGeometry(QRect(400, 420, 221, 20))
        self.labelErroreConfermaPassword.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00\n"
"}")
        self.labelErroreConfermaPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErrorePassword2 = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelErrorePassword2.setObjectName(u"labelErrorePassword2")
        self.labelErrorePassword2.setGeometry(QRect(40, 400, 681, 20))
        font2 = QFont()
        font2.setPointSize(7)
        self.labelErrorePassword2.setFont(font2)
        self.labelErrorePassword2.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00\n"
"}")
        self.labelErrorePassword2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCodiceFiscaleCliente = QLabel(VistaModificaProfiloPersonaleCliente)
        self.labelCodiceFiscaleCliente.setObjectName(u"labelCodiceFiscaleCliente")
        self.labelCodiceFiscaleCliente.setGeometry(QRect(40, 210, 131, 20))
        self.labelCodiceFiscaleCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")

        self.retranslateUi(VistaModificaProfiloPersonaleCliente)

        QMetaObject.connectSlotsByName(VistaModificaProfiloPersonaleCliente)
    # setupUi

    def retranslateUi(self, VistaModificaProfiloPersonaleCliente):
        VistaModificaProfiloPersonaleCliente.setWindowTitle(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Modifica Profilo Personale - CineMax", None))
        self.Sfondo.setText("")
        self.labelProfilo.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Modifica Profilo Personale", None))
        self.labelCognome.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Cognome:", None))
        self.labelCodiceFiscale.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Codice Fiscale:", None))
        self.labelEmail.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Email:", None))
        self.labelTelefono.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Telefono:", None))
        self.labelPassword.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Password:", None))
        self.pushButtonConferma.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Conferma", None))
        self.lineEditEmail.setText("")
        self.lineEditNome.setText("")
        self.lineEditCognome.setText("")
        self.lineEditTelefono.setText("")
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Annulla", None))
        self.lineEditPassword.setText("")
        self.lineEditConfermaPassword.setText("")
        self.labelConfermaPassword.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Conferma Password:", None))
        self.labelDataNascita.setText(QCoreApplication.translate("VistaModificaProfiloPersonaleCliente", u"Data di Nascita:", None))
        self.labelErroreNome.setText("")
        self.labelErroreCognome.setText("")
        self.labelErroreDataNascita.setText("")
        self.labelErroreEmail.setText("")
        self.labelErroreTelefono.setText("")
        self.labelErroreConfermaPassword.setText("")
        self.labelErrorePassword2.setText("")
        self.labelCodiceFiscaleCliente.setText("")
    # retranslateUi

