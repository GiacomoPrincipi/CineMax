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

class Ui_VistaLoginAmministratore(object):
    def setupUi(self, VistaLoginAmministratore):
        if not VistaLoginAmministratore.objectName():
            VistaLoginAmministratore.setObjectName(u"VistaLoginAmministratore")
        VistaLoginAmministratore.resize(790, 499)
        self.label = QLabel(VistaLoginAmministratore)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 371, 71))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
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
        self.pushButtonRecuperoCredenziali = QPushButton(VistaLoginAmministratore)
        self.pushButtonRecuperoCredenziali.setObjectName(u"pushButtonRecuperoCredenziali")
        self.pushButtonRecuperoCredenziali.setGeometry(QRect(610, 450, 161, 29))
        self.pushButtonRecuperoCredenziali.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
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
"        stop: 0 #320F00,\n"
"        stop: 1 #641E00\n"
"    );\n"
"}")
        self.labelIndietroButtonAmministratore = QLabel(VistaLoginAmministratore)
        self.labelIndietroButtonAmministratore.setObjectName(u"labelIndietroButtonAmministratore")
        self.labelIndietroButtonAmministratore.setGeometry(QRect(700, 20, 63, 61))
        self.labelIndietroButtonAmministratore.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButtonAmministratore.setScaledContents(True)
        self.Sfondo.raise_()
        self.label.raise_()
        self.pushButtonAccedi.raise_()
        self.lineEditEmail.raise_()
        self.lineEditPassword.raise_()
        self.labelEmail.raise_()
        self.labelPassword.raise_()
        self.pushButtonRecuperoCredenziali.raise_()
        self.labelIndietroButtonAmministratore.raise_()

        self.retranslateUi(VistaLoginAmministratore)

        QMetaObject.connectSlotsByName(VistaLoginAmministratore)
    # setupUi

    def retranslateUi(self, VistaLoginAmministratore):
        VistaLoginAmministratore.setWindowTitle(QCoreApplication.translate("VistaLoginAmministratore", u"Login Amministratore - CineMax", None))
        self.label.setText(QCoreApplication.translate("VistaLoginAmministratore", u"Login Amministratore", None))
        self.pushButtonAccedi.setText(QCoreApplication.translate("VistaLoginAmministratore", u"Accedi", None))
        self.lineEditEmail.setText("")
        self.lineEditPassword.setText("")
        self.labelEmail.setText(QCoreApplication.translate("VistaLoginAmministratore", u"Email", None))
        self.labelPassword.setText(QCoreApplication.translate("VistaLoginAmministratore", u"Password", None))
        self.pushButtonRecuperoCredenziali.setText(QCoreApplication.translate("VistaLoginAmministratore", u"Recupero Password", None))
        self.Sfondo.setText("")
        self.labelIndietroButtonAmministratore.setText("")
    # retranslateUi

