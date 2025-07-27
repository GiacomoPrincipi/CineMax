# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaAmministratoreAmministratore.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

from clickablelabel import ClickableLabel

class Ui_VistaVisualizzaAmministratoreAmministratore(object):
    def setupUi(self, VistaVisualizzaAmministratoreAmministratore):
        if not VistaVisualizzaAmministratoreAmministratore.objectName():
            VistaVisualizzaAmministratoreAmministratore.setObjectName(u"VistaVisualizzaAmministratoreAmministratore")
        VistaVisualizzaAmministratoreAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaAmministratoreAmministratore)
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
        self.labelProfilo = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelProfilo.setObjectName(u"labelProfilo")
        self.labelProfilo.setGeometry(QRect(40, 30, 121, 121))
        self.labelProfilo.setPixmap(QPixmap(u"Immagini/profiloButtonAmministratore.png"))
        self.labelProfilo.setScaledContents(True)
        self.labelNome = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 381, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelHomeButton = ClickableLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelHomeButton.setObjectName(u"labelHomeButton")
        self.labelHomeButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButton.setPixmap(QPixmap(u"Immagini/HomeButtonAmministratore.png"))
        self.labelHomeButton.setScaledContents(True)
        self.labelCognome = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelNomeAmministratore = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelNomeAmministratore.setObjectName(u"labelNomeAmministratore")
        self.labelNomeAmministratore.setGeometry(QRect(180, 120, 131, 20))
        self.labelNomeAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelCognomeAmministratore = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelCognomeAmministratore.setObjectName(u"labelCognomeAmministratore")
        self.labelCognomeAmministratore.setGeometry(QRect(330, 120, 131, 20))
        self.labelCognomeAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelMatricola = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelMatricola.setObjectName(u"labelMatricola")
        self.labelMatricola.setGeometry(QRect(40, 180, 81, 20))
        self.labelMatricola.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelMatricola.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelMatricolaAmministratore = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelMatricolaAmministratore.setObjectName(u"labelMatricolaAmministratore")
        self.labelMatricolaAmministratore.setGeometry(QRect(40, 200, 131, 20))
        self.labelMatricolaAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelEmail = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(40, 240, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmailAmministratore = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelEmailAmministratore.setObjectName(u"labelEmailAmministratore")
        self.labelEmailAmministratore.setGeometry(QRect(40, 260, 251, 20))
        self.labelEmailAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelTelefono = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(40, 300, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefonoAmministratore = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelTelefonoAmministratore.setObjectName(u"labelTelefonoAmministratore")
        self.labelTelefonoAmministratore.setGeometry(QRect(40, 320, 251, 20))
        self.labelTelefonoAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelDataNascita = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelDataNascita.setObjectName(u"labelDataNascita")
        self.labelDataNascita.setGeometry(QRect(510, 100, 121, 20))
        self.labelDataNascita.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelDataNascita.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataNascitaAmministratore = QLabel(VistaVisualizzaAmministratoreAmministratore)
        self.labelDataNascitaAmministratore.setObjectName(u"labelDataNascitaAmministratore")
        self.labelDataNascitaAmministratore.setGeometry(QRect(510, 120, 101, 20))
        self.labelDataNascitaAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")

        self.retranslateUi(VistaVisualizzaAmministratoreAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaAmministratoreAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaAmministratoreAmministratore):
        VistaVisualizzaAmministratoreAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaAmministratoreAmministratore", u"Profilo Amministratore - CineMax", None))
        self.Sfondo.setText("")
        self.labelProfilo.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaVisualizzaAmministratoreAmministratore", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaAmministratoreAmministratore", u"Profilo Amministratore", None))
        self.labelHomeButton.setText("")
        self.labelCognome.setText(QCoreApplication.translate("VistaVisualizzaAmministratoreAmministratore", u"Cognome:", None))
        self.labelNomeAmministratore.setText("")
        self.labelCognomeAmministratore.setText("")
        self.labelMatricola.setText(QCoreApplication.translate("VistaVisualizzaAmministratoreAmministratore", u"Matricola:", None))
        self.labelMatricolaAmministratore.setText("")
        self.labelEmail.setText(QCoreApplication.translate("VistaVisualizzaAmministratoreAmministratore", u"Email:", None))
        self.labelEmailAmministratore.setText("")
        self.labelTelefono.setText(QCoreApplication.translate("VistaVisualizzaAmministratoreAmministratore", u"Telefono:", None))
        self.labelTelefonoAmministratore.setText("")
        self.labelIndietroButton.setText("")
        self.labelDataNascita.setText(QCoreApplication.translate("VistaVisualizzaAmministratoreAmministratore", u"Data di Nascita:", None))
        self.labelDataNascitaAmministratore.setText("")
    # retranslateUi

