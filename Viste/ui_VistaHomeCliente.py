# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaHomeCliente.ui'
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

from Viste.clickablelabel import ClickableLabel

class Ui_VistaHomeCliente(object):
    def setupUi(self, VistaHomeCliente):
        if not VistaHomeCliente.objectName():
            VistaHomeCliente.setObjectName(u"VistaHomeCliente")
        VistaHomeCliente.resize(790, 499)
        self.pushButtonSpettacoli = QPushButton(VistaHomeCliente)
        self.pushButtonSpettacoli.setObjectName(u"pushButtonSpettacoli")
        self.pushButtonSpettacoli.setGeometry(QRect(180, 160, 201, 101))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButtonSpettacoli.setFont(font)
        self.pushButtonSpettacoli.setStyleSheet(u"QPushButton {\n"
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
        self.Sfondo = QLabel(VistaHomeCliente)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 90, 791, 411))
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
        self.labelBarra = QLabel(VistaHomeCliente)
        self.labelBarra.setObjectName(u"labelBarra")
        self.labelBarra.setGeometry(QRect(0, 0, 791, 91))
        self.labelBarra.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #965A00,\n"
"        stop: 1 #B46E00\n"
"    );\n"
"    border: 1px solid #AF8C0A;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"}")
        self.labelProfiloButton = ClickableLabel(VistaHomeCliente)
        self.labelProfiloButton.setObjectName(u"labelProfiloButton")
        self.labelProfiloButton.setGeometry(QRect(700, 10, 63, 61))
        self.labelProfiloButton.setPixmap(QPixmap(u"Viste/Immagini/ProfiloButtonCliente.png"))
        self.labelProfiloButton.setScaledContents(True)
        self.labelProfilo = QLabel(VistaHomeCliente)
        self.labelProfilo.setObjectName(u"labelProfilo")
        self.labelProfilo.setGeometry(QRect(700, 70, 63, 20))
        self.labelProfilo.setStyleSheet(u"QLabel {\n"
"    color: #D7AA0C;\n"
"}")
        self.labelProfilo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLogout = QLabel(VistaHomeCliente)
        self.labelLogout.setObjectName(u"labelLogout")
        self.labelLogout.setGeometry(QRect(20, 70, 63, 20))
        self.labelLogout.setStyleSheet(u"QLabel {\n"
"    color: #D7AA0C;\n"
"}")
        self.labelLogout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLogoutButton = ClickableLabel(VistaHomeCliente)
        self.labelLogoutButton.setObjectName(u"labelLogoutButton")
        self.labelLogoutButton.setGeometry(QRect(20, 10, 63, 61))
        self.labelLogoutButton.setPixmap(QPixmap(u"Viste/Immagini/LogoutButtonCliente.png"))
        self.labelLogoutButton.setScaledContents(True)
        self.pushButtonProdotti = QPushButton(VistaHomeCliente)
        self.pushButtonProdotti.setObjectName(u"pushButtonProdotti")
        self.pushButtonProdotti.setGeometry(QRect(410, 160, 201, 101))
        self.pushButtonProdotti.setFont(font)
        self.pushButtonProdotti.setStyleSheet(u"QPushButton {\n"
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
        self.pushButtonPagamenti = QPushButton(VistaHomeCliente)
        self.pushButtonPagamenti.setObjectName(u"pushButtonPagamenti")
        self.pushButtonPagamenti.setGeometry(QRect(180, 290, 201, 101))
        self.pushButtonPagamenti.setFont(font)
        self.pushButtonPagamenti.setStyleSheet(u"QPushButton {\n"
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
        self.pushButtonRecensioni = QPushButton(VistaHomeCliente)
        self.pushButtonRecensioni.setObjectName(u"pushButtonRecensioni")
        self.pushButtonRecensioni.setGeometry(QRect(410, 290, 201, 101))
        self.pushButtonRecensioni.setFont(font)
        self.pushButtonRecensioni.setStyleSheet(u"QPushButton {\n"
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
        self.labelTitolo = QLabel(VistaHomeCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(140, 10, 511, 71))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.labelTitolo.setFont(font2)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #D7AA0C;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Sfondo.raise_()
        self.pushButtonSpettacoli.raise_()
        self.labelBarra.raise_()
        self.labelProfilo.raise_()
        self.labelLogout.raise_()
        self.labelLogoutButton.raise_()
        self.pushButtonProdotti.raise_()
        self.pushButtonPagamenti.raise_()
        self.pushButtonRecensioni.raise_()
        self.labelTitolo.raise_()
        self.labelProfiloButton.raise_()

        self.retranslateUi(VistaHomeCliente)

        QMetaObject.connectSlotsByName(VistaHomeCliente)
    # setupUi

    def retranslateUi(self, VistaHomeCliente):
        VistaHomeCliente.setWindowTitle(QCoreApplication.translate("VistaHomeCliente", u"Area Riservata Cliente - CineMax", None))
        self.pushButtonSpettacoli.setText(QCoreApplication.translate("VistaHomeCliente", u"Spettacoli", None))
        self.Sfondo.setText("")
        self.labelBarra.setText("")
        self.labelProfiloButton.setText("")
        self.labelProfilo.setText(QCoreApplication.translate("VistaHomeCliente", u"Profilo", None))
        self.labelLogout.setText(QCoreApplication.translate("VistaHomeCliente", u"Logout", None))
        self.labelLogoutButton.setText("")
        self.pushButtonProdotti.setText(QCoreApplication.translate("VistaHomeCliente", u"Prodotti", None))
        self.pushButtonPagamenti.setText(QCoreApplication.translate("VistaHomeCliente", u"Pagamenti", None))
        self.pushButtonRecensioni.setText(QCoreApplication.translate("VistaHomeCliente", u"Recensioni", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaHomeCliente", u"Area Riservata Cliente", None))
    # retranslateUi

