# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaProfiloPersonaleCliente.ui'
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

from clickablelabel import ClickableLabel

class Ui_VistaVisualizzaProfiloPersonaleCliente(object):
    def setupUi(self, VistaVisualizzaProfiloPersonaleCliente):
        if not VistaVisualizzaProfiloPersonaleCliente.objectName():
            VistaVisualizzaProfiloPersonaleCliente.setObjectName(u"VistaVisualizzaProfiloPersonaleCliente")
        VistaVisualizzaProfiloPersonaleCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"		stop: 0 #211400,\n"
"        stop: 1 #7D4B00\n"
"    );\n"
"}")
        self.labelProfilo = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelProfilo.setObjectName(u"labelProfilo")
        self.labelProfilo.setGeometry(QRect(30, 30, 121, 121))
        self.labelProfilo.setPixmap(QPixmap(u"Viste/Immagini/ProfiloButtonCliente.png"))
        self.labelProfilo.setScaledContents(True)
        self.labelNome = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 291, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #D7AA0C;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelCognome = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelNomeCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelNomeCliente.setObjectName(u"labelNomeCliente")
        self.labelNomeCliente.setGeometry(QRect(180, 130, 131, 20))
        self.labelNomeCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelCognomeCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelCognomeCliente.setObjectName(u"labelCognomeCliente")
        self.labelCognomeCliente.setGeometry(QRect(330, 130, 171, 20))
        self.labelCognomeCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelCodiceFiscale = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelCodiceFiscale.setObjectName(u"labelCodiceFiscale")
        self.labelCodiceFiscale.setGeometry(QRect(30, 180, 111, 20))
        self.labelCodiceFiscale.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelCodiceFiscale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCodiceFiscaleCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelCodiceFiscaleCliente.setObjectName(u"labelCodiceFiscaleCliente")
        self.labelCodiceFiscaleCliente.setGeometry(QRect(30, 210, 131, 20))
        self.labelCodiceFiscaleCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelEmail = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(30, 250, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmailCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelEmailCliente.setObjectName(u"labelEmailCliente")
        self.labelEmailCliente.setGeometry(QRect(30, 280, 251, 20))
        self.labelEmailCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelTelefono = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(30, 320, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefonoCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelTelefonoCliente.setObjectName(u"labelTelefonoCliente")
        self.labelTelefonoCliente.setGeometry(QRect(30, 350, 101, 20))
        self.labelTelefonoCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelPassword = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(30, 400, 81, 20))
        self.labelPassword.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPasswordCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelPasswordCliente.setObjectName(u"labelPasswordCliente")
        self.labelPasswordCliente.setGeometry(QRect(30, 430, 121, 20))
        self.labelPasswordCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.pushButtonModifica = QPushButton(VistaVisualizzaProfiloPersonaleCliente)
        self.pushButtonModifica.setObjectName(u"pushButtonModifica")
        self.pushButtonModifica.setGeometry(QRect(670, 440, 91, 29))
        self.pushButtonModifica.setStyleSheet(u"QPushButton {\n"
"    background-color: #963C00;\n"
"    color: #FF7800;\n"
"    border: 2px solid #502800;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C86400;\n"
"}\n"
"")
        self.labelDataNascita = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelDataNascita.setObjectName(u"labelDataNascita")
        self.labelDataNascita.setGeometry(QRect(520, 100, 131, 20))
        self.labelDataNascita.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelDataNascitaCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelDataNascitaCliente.setObjectName(u"labelDataNascitaCliente")
        self.labelDataNascitaCliente.setGeometry(QRect(520, 130, 101, 20))
        self.labelDataNascitaCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelPunti = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelPunti.setObjectName(u"labelPunti")
        self.labelPunti.setGeometry(QRect(180, 400, 81, 20))
        self.labelPunti.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPuntiCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelPuntiCliente.setObjectName(u"labelPuntiCliente")
        self.labelPuntiCliente.setGeometry(QRect(180, 430, 91, 20))
        self.labelPuntiCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.pushButtonElimina = QPushButton(VistaVisualizzaProfiloPersonaleCliente)
        self.pushButtonElimina.setObjectName(u"pushButtonElimina")
        self.pushButtonElimina.setGeometry(QRect(520, 440, 131, 29))
        self.pushButtonElimina.setStyleSheet(u"QPushButton {\n"
"    background-color: #963C00;\n"
"    color: #FF7800;\n"
"    border: 2px solid #502800;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C86400;\n"
"}\n"
"")

        self.retranslateUi(VistaVisualizzaProfiloPersonaleCliente)

        QMetaObject.connectSlotsByName(VistaVisualizzaProfiloPersonaleCliente)
    # setupUi

    def retranslateUi(self, VistaVisualizzaProfiloPersonaleCliente):
        VistaVisualizzaProfiloPersonaleCliente.setWindowTitle(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Profilo Personale - CineMax", None))
        self.Sfondo.setText("")
        self.labelProfilo.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Profilo Personale", None))
        self.labelIndietroButton.setText("")
        self.labelCognome.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Cognome:", None))
        self.labelNomeCliente.setText("")
        self.labelCognomeCliente.setText("")
        self.labelCodiceFiscale.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Codice Fiscale:", None))
        self.labelCodiceFiscaleCliente.setText("")
        self.labelEmail.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Email:", None))
        self.labelEmailCliente.setText("")
        self.labelTelefono.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Telefono:", None))
        self.labelTelefonoCliente.setText("")
        self.labelPassword.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Password:", None))
        self.labelPasswordCliente.setText("")
        self.pushButtonModifica.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Modifica", None))
        self.labelDataNascita.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Data di Nascita:", None))
        self.labelDataNascitaCliente.setText("")
        self.labelPunti.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Punti:", None))
        self.labelPuntiCliente.setText("")
        self.pushButtonElimina.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Elimia account", None))
    # retranslateUi

