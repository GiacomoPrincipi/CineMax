# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaProfiloPersonaleAmministratore.ui'
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

class Ui_VistaVisualizzaProfiloPersonaleAmministratore(object):
    def setupUi(self, VistaVisualizzaProfiloPersonaleAmministratore):
        if not VistaVisualizzaProfiloPersonaleAmministratore.objectName():
            VistaVisualizzaProfiloPersonaleAmministratore.setObjectName(u"VistaVisualizzaProfiloPersonaleAmministratore")
        VistaVisualizzaProfiloPersonaleAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
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
        self.labelProfilo = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelProfilo.setObjectName(u"labelProfilo")
        self.labelProfilo.setGeometry(QRect(30, 30, 121, 121))
        self.labelProfilo.setPixmap(QPixmap(u"Viste/Immagini/ProfiloButtonAmministratore.png"))
        self.labelProfilo.setScaledContents(True)
        self.labelNome = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 291, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #D7320C;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelCognome = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelNomeAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelNomeAmministratore.setObjectName(u"labelNomeAmministratore")
        self.labelNomeAmministratore.setGeometry(QRect(180, 130, 131, 20))
        self.labelNomeAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelCognomeAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelCognomeAmministratore.setObjectName(u"labelCognomeAmministratore")
        self.labelCognomeAmministratore.setGeometry(QRect(330, 130, 171, 20))
        self.labelCognomeAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelMatricola = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelMatricola.setObjectName(u"labelMatricola")
        self.labelMatricola.setGeometry(QRect(30, 180, 81, 20))
        self.labelMatricola.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelMatricola.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelMatricolaAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelMatricolaAmministratore.setObjectName(u"labelMatricolaAmministratore")
        self.labelMatricolaAmministratore.setGeometry(QRect(30, 210, 131, 20))
        self.labelMatricolaAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelEmail = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(30, 250, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmailAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelEmailAmministratore.setObjectName(u"labelEmailAmministratore")
        self.labelEmailAmministratore.setGeometry(QRect(30, 280, 251, 20))
        self.labelEmailAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelTelefono = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(30, 320, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefonoAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelTelefonoAmministratore.setObjectName(u"labelTelefonoAmministratore")
        self.labelTelefonoAmministratore.setGeometry(QRect(30, 350, 101, 20))
        self.labelTelefonoAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.pushButtonModifica = QPushButton(VistaVisualizzaProfiloPersonaleAmministratore)
        self.pushButtonModifica.setObjectName(u"pushButtonModifica")
        self.pushButtonModifica.setGeometry(QRect(670, 440, 91, 29))
        self.pushButtonModifica.setStyleSheet(u"QPushButton {\n"
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
        self.labelDataNascita = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelDataNascita.setObjectName(u"labelDataNascita")
        self.labelDataNascita.setGeometry(QRect(520, 100, 121, 20))
        self.labelDataNascita.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelDataNascita.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataNascitaAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelDataNascitaAmministratore.setObjectName(u"labelDataNascitaAmministratore")
        self.labelDataNascitaAmministratore.setGeometry(QRect(520, 130, 111, 20))
        self.labelDataNascitaAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelPassword = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(30, 400, 81, 20))
        self.labelPassword.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPasswordAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelPasswordAmministratore.setObjectName(u"labelPasswordAmministratore")
        self.labelPasswordAmministratore.setGeometry(QRect(30, 430, 121, 20))
        self.labelPasswordAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.pushButtonElimina = QPushButton(VistaVisualizzaProfiloPersonaleAmministratore)
        self.pushButtonElimina.setObjectName(u"pushButtonElimina")
        self.pushButtonElimina.setGeometry(QRect(520, 440, 131, 29))
        self.pushButtonElimina.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(VistaVisualizzaProfiloPersonaleAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaProfiloPersonaleAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaProfiloPersonaleAmministratore):
        VistaVisualizzaProfiloPersonaleAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Profilo Personale - CineMax", None))
        self.Sfondo.setText("")
        self.labelProfilo.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Profilo Personale", None))
        self.labelIndietroButton.setText("")
        self.labelCognome.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Cognome:", None))
        self.labelNomeAmministratore.setText("")
        self.labelCognomeAmministratore.setText("")
        self.labelMatricola.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Matricola:", None))
        self.labelMatricolaAmministratore.setText("")
        self.labelEmail.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Email:", None))
        self.labelEmailAmministratore.setText("")
        self.labelTelefono.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Telefono:", None))
        self.labelTelefonoAmministratore.setText("")
        self.pushButtonModifica.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Modifica", None))
        self.labelDataNascita.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Data di Nascita:", None))
        self.labelDataNascitaAmministratore.setText("")
        self.labelPassword.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Password:", None))
        self.labelPasswordAmministratore.setText("")
        self.pushButtonElimina.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Elimia account", None))
    # retranslateUi

