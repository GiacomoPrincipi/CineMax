# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaLoginAmministratore.ui'
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

from Viste.clickablelabel import ClickableLabel

class Ui_VistaLoginAmministratore(object):
    def setupUi(self, VistaLoginAmministratore):
        if not VistaLoginAmministratore.objectName():
            VistaLoginAmministratore.setObjectName(u"VistaLoginAmministratore")
        VistaLoginAmministratore.resize(790, 499)
        self.labelTitolo = QLabel(VistaLoginAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(30, 20, 371, 71))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable"])
        font.setPointSize(20)
        font.setBold(True)
        self.labelTitolo.setFont(font)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #D7320C;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButtonAccedi = QPushButton(VistaLoginAmministratore)
        self.pushButtonAccedi.setObjectName(u"pushButtonAccedi")
        self.pushButtonAccedi.setGeometry(QRect(420, 310, 91, 29))
        self.pushButtonAccedi.setStyleSheet(u"QPushButton {\n"
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
        self.lineEditEmail = QLineEdit(VistaLoginAmministratore)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setGeometry(QRect(280, 200, 231, 26))
        self.lineEditEmail.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditPassword = QLineEdit(VistaLoginAmministratore)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(280, 270, 231, 26))
        self.lineEditPassword.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.labelEmail = QLabel(VistaLoginAmministratore)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(280, 170, 63, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPassword = QLabel(VistaLoginAmministratore)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(280, 240, 71, 20))
        self.labelPassword.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.pushButtonRecuperoPassword = QPushButton(VistaLoginAmministratore)
        self.pushButtonRecuperoPassword.setObjectName(u"pushButtonRecuperoPassword")
        self.pushButtonRecuperoPassword.setGeometry(QRect(610, 450, 161, 29))
        self.pushButtonRecuperoPassword.setStyleSheet(u"QPushButton {\n"
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
        self.Sfondo = QLabel(VistaLoginAmministratore)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font1)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #210A00,\n"
"        stop: 1 #7D2100\n"
"    );\n"
"}")
        self.labelIndietroButton = ClickableLabel(VistaLoginAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelErroreEmail = QLabel(VistaLoginAmministratore)
        self.labelErroreEmail.setObjectName(u"labelErroreEmail")
        self.labelErroreEmail.setGeometry(QRect(520, 200, 191, 20))
        self.labelErroreEmail.setStyleSheet(u"QLabel {\n"
"    color: #FF0000;\n"
"}")
        self.labelErroreEmail.setScaledContents(False)
        self.labelErrorePassword = QLabel(VistaLoginAmministratore)
        self.labelErrorePassword.setObjectName(u"labelErrorePassword")
        self.labelErrorePassword.setGeometry(QRect(520, 270, 151, 20))
        self.labelErrorePassword.setStyleSheet(u"QLabel {\n"
"    color: #FF0000;\n"
"}")
        self.labelRecuperoPassword = QLabel(VistaLoginAmministratore)
        self.labelRecuperoPassword.setObjectName(u"labelRecuperoPassword")
        self.labelRecuperoPassword.setGeometry(QRect(390, 450, 211, 31))
        self.labelRecuperoPassword.setStyleSheet(u"QLabel {\n"
"    color: #FF0000;\n"
"}")
        self.labelRecuperoPassword.setScaledContents(False)
        self.labelRecuperoPassword.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Sfondo.raise_()
        self.labelTitolo.raise_()
        self.pushButtonAccedi.raise_()
        self.lineEditEmail.raise_()
        self.lineEditPassword.raise_()
        self.labelEmail.raise_()
        self.labelPassword.raise_()
        self.pushButtonRecuperoPassword.raise_()
        self.labelIndietroButton.raise_()
        self.labelErroreEmail.raise_()
        self.labelErrorePassword.raise_()
        self.labelRecuperoPassword.raise_()

        self.retranslateUi(VistaLoginAmministratore)

        QMetaObject.connectSlotsByName(VistaLoginAmministratore)
    # setupUi

    def retranslateUi(self, VistaLoginAmministratore):
        VistaLoginAmministratore.setWindowTitle(QCoreApplication.translate("VistaLoginAmministratore", u"Login Amministratore - CineMax", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaLoginAmministratore", u"Login Amministratore", None))
        self.pushButtonAccedi.setText(QCoreApplication.translate("VistaLoginAmministratore", u"Accedi", None))
        self.lineEditEmail.setText("")
        self.lineEditPassword.setText("")
        self.labelEmail.setText(QCoreApplication.translate("VistaLoginAmministratore", u"Email:", None))
        self.labelPassword.setText(QCoreApplication.translate("VistaLoginAmministratore", u"Password:", None))
        self.pushButtonRecuperoPassword.setText(QCoreApplication.translate("VistaLoginAmministratore", u"Recupero Password", None))
        self.Sfondo.setText("")
        self.labelIndietroButton.setText("")
        self.labelErroreEmail.setText("")
        self.labelErrorePassword.setText("")
        self.labelRecuperoPassword.setText("")
    # retranslateUi

