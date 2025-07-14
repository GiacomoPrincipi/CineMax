# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaRegistrazioneCliente.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_VistaModificaRegistrazioneCliente(object):
    def setupUi(self, VistaModificaRegistrazioneCliente):
        if not VistaModificaRegistrazioneCliente.objectName():
            VistaModificaRegistrazioneCliente.setObjectName(u"VistaModificaRegistrazioneCliente")
        VistaModificaRegistrazioneCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaModificaRegistrazioneCliente)
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
        self.labelProfiloCliente = QLabel(VistaModificaRegistrazioneCliente)
        self.labelProfiloCliente.setObjectName(u"labelProfiloCliente")
        self.labelProfiloCliente.setGeometry(QRect(40, 30, 121, 121))
        self.labelProfiloCliente.setPixmap(QPixmap(u"Immagini/profiloButtonCliente.png"))
        self.labelProfiloCliente.setScaledContents(True)
        self.labelNome = QLabel(VistaModificaRegistrazioneCliente)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaModificaRegistrazioneCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 271, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C8B400;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCognome = QLabel(VistaModificaRegistrazioneCliente)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCodiceFiscale = QLabel(VistaModificaRegistrazioneCliente)
        self.labelCodiceFiscale.setObjectName(u"labelCodiceFiscale")
        self.labelCodiceFiscale.setGeometry(QRect(40, 180, 111, 20))
        self.labelCodiceFiscale.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelCodiceFiscale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmail = QLabel(VistaModificaRegistrazioneCliente)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(40, 240, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefono = QLabel(VistaModificaRegistrazioneCliente)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(40, 300, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPunti = QLabel(VistaModificaRegistrazioneCliente)
        self.labelPunti.setObjectName(u"labelPunti")
        self.labelPunti.setGeometry(QRect(40, 360, 81, 20))
        self.labelPunti.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButtonConferma = QPushButton(VistaModificaRegistrazioneCliente)
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
        self.lineEditEmail = QLineEdit(VistaModificaRegistrazioneCliente)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setGeometry(QRect(40, 260, 251, 26))
        self.lineEditEmail.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditPunti = QLineEdit(VistaModificaRegistrazioneCliente)
        self.lineEditPunti.setObjectName(u"lineEditPunti")
        self.lineEditPunti.setGeometry(QRect(40, 380, 71, 26))
        self.lineEditPunti.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditNome = QLineEdit(VistaModificaRegistrazioneCliente)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setGeometry(QRect(180, 120, 121, 26))
        self.lineEditNome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditCognome = QLineEdit(VistaModificaRegistrazioneCliente)
        self.lineEditCognome.setObjectName(u"lineEditCognome")
        self.lineEditCognome.setGeometry(QRect(330, 120, 171, 26))
        self.lineEditCognome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditCodiceFiscale = QLineEdit(VistaModificaRegistrazioneCliente)
        self.lineEditCodiceFiscale.setObjectName(u"lineEditCodiceFiscale")
        self.lineEditCodiceFiscale.setGeometry(QRect(40, 200, 141, 26))
        self.lineEditCodiceFiscale.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditTelefono = QLineEdit(VistaModificaRegistrazioneCliente)
        self.lineEditTelefono.setObjectName(u"lineEditTelefono")
        self.lineEditTelefono.setGeometry(QRect(40, 320, 121, 26))
        self.lineEditTelefono.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.pushButtonAnnulla = QPushButton(VistaModificaRegistrazioneCliente)
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

        self.retranslateUi(VistaModificaRegistrazioneCliente)

        QMetaObject.connectSlotsByName(VistaModificaRegistrazioneCliente)
    # setupUi

    def retranslateUi(self, VistaModificaRegistrazioneCliente):
        VistaModificaRegistrazioneCliente.setWindowTitle(QCoreApplication.translate("VistaModificaRegistrazioneCliente", u"Registrazione - CineMax", None))
        self.Sfondo.setText("")
        self.labelProfiloCliente.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaModificaRegistrazioneCliente", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaModificaRegistrazioneCliente", u"Registrazione", None))
        self.labelCognome.setText(QCoreApplication.translate("VistaModificaRegistrazioneCliente", u"Cognome:", None))
        self.labelCodiceFiscale.setText(QCoreApplication.translate("VistaModificaRegistrazioneCliente", u"Codice Fiscale:", None))
        self.labelEmail.setText(QCoreApplication.translate("VistaModificaRegistrazioneCliente", u"Email:", None))
        self.labelTelefono.setText(QCoreApplication.translate("VistaModificaRegistrazioneCliente", u"Telefono:", None))
        self.labelPunti.setText(QCoreApplication.translate("VistaModificaRegistrazioneCliente", u"Punti:", None))
        self.pushButtonConferma.setText(QCoreApplication.translate("VistaModificaRegistrazioneCliente", u"Conferma", None))
        self.lineEditEmail.setText("")
        self.lineEditPunti.setText("")
        self.lineEditNome.setText("")
        self.lineEditCognome.setText("")
        self.lineEditCodiceFiscale.setText("")
        self.lineEditTelefono.setText("")
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaModificaRegistrazioneCliente", u"Annulla", None))
    # retranslateUi

