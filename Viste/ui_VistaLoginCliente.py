# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaLoginCliente.ui'
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

from clickablelabel import ClickableLabel

class Ui_VistaLoginCliente(object):
    def setupUi(self, VistaLoginCliente):
        if not VistaLoginCliente.objectName():
            VistaLoginCliente.setObjectName(u"VistaLoginCliente")
        VistaLoginCliente.resize(790, 499)
        self.labelTitolo = QLabel(VistaLoginCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(30, 20, 241, 71))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable"])
        font.setPointSize(20)
        font.setBold(True)
        self.labelTitolo.setFont(font)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #D7AA0C;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButtonAccedi = QPushButton(VistaLoginCliente)
        self.pushButtonAccedi.setObjectName(u"pushButtonAccedi")
        self.pushButtonAccedi.setGeometry(QRect(420, 310, 91, 29))
        self.pushButtonAccedi.setStyleSheet(u"QPushButton {\n"
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
        self.pushButtonRegistrati = QPushButton(VistaLoginCliente)
        self.pushButtonRegistrati.setObjectName(u"pushButtonRegistrati")
        self.pushButtonRegistrati.setGeometry(QRect(280, 310, 93, 31))
        self.pushButtonRegistrati.setStyleSheet(u"QPushButton {\n"
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
        self.lineEditEmail = QLineEdit(VistaLoginCliente)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setGeometry(QRect(280, 200, 231, 26))
        self.lineEditEmail.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditPassword = QLineEdit(VistaLoginCliente)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(280, 270, 231, 26))
        self.lineEditPassword.setStyleSheet(u"QLineEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.labelEmail = QLabel(VistaLoginCliente)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(280, 170, 63, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPassword = QLabel(VistaLoginCliente)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(280, 240, 71, 20))
        self.labelPassword.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.pushButtonRecuperoPassword = QPushButton(VistaLoginCliente)
        self.pushButtonRecuperoPassword.setObjectName(u"pushButtonRecuperoPassword")
        self.pushButtonRecuperoPassword.setGeometry(QRect(610, 450, 161, 29))
        self.pushButtonRecuperoPassword.setStyleSheet(u"QPushButton {\n"
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
        self.Sfondo = QLabel(VistaLoginCliente)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font1)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"		stop: 0 #211400,\n"
"        stop: 1 #7D4B00\n"
"    );\n"
"}")
        self.Sfondo.setScaledContents(False)
        self.labelIndietroButton = ClickableLabel(VistaLoginCliente)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelErroreEmail = QLabel(VistaLoginCliente)
        self.labelErroreEmail.setObjectName(u"labelErroreEmail")
        self.labelErroreEmail.setGeometry(QRect(520, 200, 191, 20))
        self.labelErroreEmail.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelErroreEmail.setScaledContents(False)
        self.labelErrorePassword = QLabel(VistaLoginCliente)
        self.labelErrorePassword.setObjectName(u"labelErrorePassword")
        self.labelErrorePassword.setGeometry(QRect(520, 270, 151, 20))
        self.labelErrorePassword.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelRecuperoPassword = QLabel(VistaLoginCliente)
        self.labelRecuperoPassword.setObjectName(u"labelRecuperoPassword")
        self.labelRecuperoPassword.setGeometry(QRect(390, 450, 211, 31))
        self.labelRecuperoPassword.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelRecuperoPassword.setScaledContents(False)
        self.labelRecuperoPassword.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Sfondo.raise_()
        self.labelTitolo.raise_()
        self.pushButtonAccedi.raise_()
        self.pushButtonRegistrati.raise_()
        self.lineEditEmail.raise_()
        self.lineEditPassword.raise_()
        self.labelEmail.raise_()
        self.labelPassword.raise_()
        self.pushButtonRecuperoPassword.raise_()
        self.labelIndietroButton.raise_()
        self.labelErroreEmail.raise_()
        self.labelErrorePassword.raise_()
        self.labelRecuperoPassword.raise_()

        self.retranslateUi(VistaLoginCliente)

        QMetaObject.connectSlotsByName(VistaLoginCliente)
    # setupUi

    def retranslateUi(self, VistaLoginCliente):
        VistaLoginCliente.setWindowTitle(QCoreApplication.translate("VistaLoginCliente", u"Login Cliente - CineMax", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaLoginCliente", u"Login Cliente", None))
        self.pushButtonAccedi.setText(QCoreApplication.translate("VistaLoginCliente", u"Accedi", None))
        self.pushButtonRegistrati.setText(QCoreApplication.translate("VistaLoginCliente", u"Registrati", None))
        self.lineEditEmail.setText("")
        self.lineEditPassword.setText("")
        self.labelEmail.setText(QCoreApplication.translate("VistaLoginCliente", u"Email:", None))
        self.labelPassword.setText(QCoreApplication.translate("VistaLoginCliente", u"Password:", None))
        self.pushButtonRecuperoPassword.setText(QCoreApplication.translate("VistaLoginCliente", u"Recupero Password", None))
        self.Sfondo.setText("")
        self.labelIndietroButton.setText("")
        self.labelErroreEmail.setText("")
        self.labelErrorePassword.setText("")
        self.labelRecuperoPassword.setText("")
    # retranslateUi

