# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaRecensioneCliente.ui'
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

class Ui_VistaVisualizzaRecensioneCliente(object):
    def setupUi(self, VistaVisualizzaRecensioneCliente):
        if not VistaVisualizzaRecensioneCliente.objectName():
            VistaVisualizzaRecensioneCliente.setObjectName(u"VistaVisualizzaRecensioneCliente")
        VistaVisualizzaRecensioneCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaRecensioneCliente)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"		stop: 0 #321E00,\n"
"        stop: 1 #643C00\n"
"    );\n"
"}")
        self.labelTitolo = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 291, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C8B400;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelHomeButton = ClickableLabel(VistaVisualizzaRecensioneCliente)
        self.labelHomeButton.setObjectName(u"labelHomeButton")
        self.labelHomeButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButton.setPixmap(QPixmap(u"Immagini/HomeButtonCliente.png"))
        self.labelHomeButton.setScaledContents(True)
        self.labelData = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(40, 180, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataRecensione = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelDataRecensione.setObjectName(u"labelDataRecensione")
        self.labelDataRecensione.setGeometry(QRect(40, 200, 91, 20))
        self.labelDataRecensione.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelStelle = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelStelle.setObjectName(u"labelStelle")
        self.labelStelle.setGeometry(QRect(40, 240, 81, 20))
        self.labelStelle.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelStelle.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelStelleRecensione = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelStelleRecensione.setObjectName(u"labelStelleRecensione")
        self.labelStelleRecensione.setGeometry(QRect(40, 260, 41, 20))
        self.labelStelleRecensione.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelOra = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelOra.setObjectName(u"labelOra")
        self.labelOra.setGeometry(QRect(180, 180, 81, 20))
        self.labelOra.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelOra.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOraRecensione = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelOraRecensione.setObjectName(u"labelOraRecensione")
        self.labelOraRecensione.setGeometry(QRect(180, 200, 51, 20))
        self.labelOraRecensione.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaRecensioneCliente)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelIconaProfilo = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelIconaProfilo.setObjectName(u"labelIconaProfilo")
        self.labelIconaProfilo.setGeometry(QRect(40, 50, 121, 121))
        self.labelIconaProfilo.setPixmap(QPixmap(u"Immagini/RecensioneIconCliente.png"))
        self.labelIconaProfilo.setScaledContents(True)
        self.labelTesto = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelTesto.setObjectName(u"labelTesto")
        self.labelTesto.setGeometry(QRect(290, 180, 81, 20))
        self.labelTesto.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTesto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTestoRecensione = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelTestoRecensione.setObjectName(u"labelTestoRecensione")
        self.labelTestoRecensione.setGeometry(QRect(290, 200, 401, 201))
        self.labelTestoRecensione.setStyleSheet(u"QLabel {\n"
"	background-color: #EBF064;\n"
"	color: #965A00;\n"
"	border: 1px solid #8C8C3C;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.labelTestoRecensione.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelTestoRecensione.setWordWrap(True)
        self.pushButtonModifica = QPushButton(VistaVisualizzaRecensioneCliente)
        self.pushButtonModifica.setObjectName(u"pushButtonModifica")
        self.pushButtonModifica.setGeometry(QRect(670, 450, 91, 29))
        self.pushButtonModifica.setStyleSheet(u"QPushButton {\n"
"    background-color: #963C00;\n"
"    color: #FF7800;\n"
"    border: 2px solid #502800;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C86400;\n"
"}")

        self.retranslateUi(VistaVisualizzaRecensioneCliente)

        QMetaObject.connectSlotsByName(VistaVisualizzaRecensioneCliente)
    # setupUi

    def retranslateUi(self, VistaVisualizzaRecensioneCliente):
        VistaVisualizzaRecensioneCliente.setWindowTitle(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Recensione - CineMax", None))
        self.Sfondo.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Recensione", None))
        self.labelHomeButton.setText("")
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Data:", None))
        self.labelDataRecensione.setText("")
        self.labelStelle.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Stelle:", None))
        self.labelStelleRecensione.setText("")
        self.labelOra.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Ora:", None))
        self.labelOraRecensione.setText("")
        self.labelIndietroButton.setText("")
        self.labelIconaProfilo.setText("")
        self.labelTesto.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Testo:", None))
        self.labelTestoRecensione.setText("")
        self.pushButtonModifica.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Modifica", None))
    # retranslateUi

