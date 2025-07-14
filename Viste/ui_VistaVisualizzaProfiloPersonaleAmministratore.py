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
"        stop: 0 #320F00,\n"
"        stop: 1 #641E00\n"
"    );\n"
"}")
        self.labelProfiloAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelProfiloAmministratore.setObjectName(u"labelProfiloAmministratore")
        self.labelProfiloAmministratore.setGeometry(QRect(40, 30, 121, 121))
        self.labelProfiloAmministratore.setPixmap(QPixmap(u"Immagini/profiloButtonAmministratore.png"))
        self.labelProfiloAmministratore.setScaledContents(True)
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
"    color: #C83C00;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIndietroButtonAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelIndietroButtonAmministratore.setObjectName(u"labelIndietroButtonAmministratore")
        self.labelIndietroButtonAmministratore.setGeometry(QRect(700, 20, 63, 61))
        self.labelIndietroButtonAmministratore.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButtonAmministratore.setScaledContents(True)
        self.labelCognome = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelNomeAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelNomeAmministratore.setObjectName(u"labelNomeAmministratore")
        self.labelNomeAmministratore.setGeometry(QRect(180, 120, 131, 20))
        self.labelNomeAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelCognomeAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelCognomeAmministratore.setObjectName(u"labelCognomeAmministratore")
        self.labelCognomeAmministratore.setGeometry(QRect(330, 120, 131, 20))
        self.labelCognomeAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelMatricola = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelMatricola.setObjectName(u"labelMatricola")
        self.labelMatricola.setGeometry(QRect(40, 180, 81, 20))
        self.labelMatricola.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelMatricola.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelMatricolaAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelMatricolaAmministratore.setObjectName(u"labelMatricolaAmministratore")
        self.labelMatricolaAmministratore.setGeometry(QRect(40, 200, 131, 20))
        self.labelMatricolaAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelEmail = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(40, 240, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmailAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelEmailAmministratore.setObjectName(u"labelEmailAmministratore")
        self.labelEmailAmministratore.setGeometry(QRect(40, 260, 251, 20))
        self.labelEmailAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelTelefono = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(40, 300, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefonoAmministratore = QLabel(VistaVisualizzaProfiloPersonaleAmministratore)
        self.labelTelefonoAmministratore.setObjectName(u"labelTelefonoAmministratore")
        self.labelTelefonoAmministratore.setGeometry(QRect(40, 320, 251, 20))
        self.labelTelefonoAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.pushButtonModifica = QPushButton(VistaVisualizzaProfiloPersonaleAmministratore)
        self.pushButtonModifica.setObjectName(u"pushButtonModifica")
        self.pushButtonModifica.setGeometry(QRect(670, 450, 91, 29))
        self.pushButtonModifica.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
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
        self.labelProfiloAmministratore.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Profilo Personale", None))
        self.labelIndietroButtonAmministratore.setText("")
        self.labelCognome.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Cognome:", None))
        self.labelNomeAmministratore.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Amministratore", None))
        self.labelCognomeAmministratore.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Amministratore", None))
        self.labelMatricola.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Matricola:", None))
        self.labelMatricolaAmministratore.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"000000", None))
        self.labelEmail.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Email:", None))
        self.labelEmailAmministratore.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Amministratore@gmail.com", None))
        self.labelTelefono.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Telefono:", None))
        self.labelTelefonoAmministratore.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"3333333333", None))
        self.pushButtonModifica.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleAmministratore", u"Modifica", None))
    # retranslateUi

