# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaRecensioneAmministratore.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTextBrowser,
    QWidget)

from Viste.clickablelabel import ClickableLabel

class Ui_VistaVisualizzaRecensioneAmministratore(object):
    def setupUi(self, VistaVisualizzaRecensioneAmministratore):
        if not VistaVisualizzaRecensioneAmministratore.objectName():
            VistaVisualizzaRecensioneAmministratore.setObjectName(u"VistaVisualizzaRecensioneAmministratore")
        VistaVisualizzaRecensioneAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaRecensioneAmministratore)
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
        self.labelId = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelId.setObjectName(u"labelId")
        self.labelId.setGeometry(QRect(180, 100, 161, 20))
        self.labelId.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelId.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaVisualizzaRecensioneAmministratore)
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
        self.labelHomeButton = ClickableLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelHomeButton.setObjectName(u"labelHomeButton")
        self.labelHomeButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButton.setPixmap(QPixmap(u"Viste/Immagini/HomeButtonAmministratore.png"))
        self.labelHomeButton.setScaledContents(True)
        self.labelData = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(30, 190, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataRecensione = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelDataRecensione.setObjectName(u"labelDataRecensione")
        self.labelDataRecensione.setGeometry(QRect(30, 220, 91, 20))
        self.labelDataRecensione.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelStelle = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelStelle.setObjectName(u"labelStelle")
        self.labelStelle.setGeometry(QRect(30, 260, 81, 20))
        self.labelStelle.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelStelle.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelStelleRecensione = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelStelleRecensione.setObjectName(u"labelStelleRecensione")
        self.labelStelleRecensione.setGeometry(QRect(30, 290, 51, 20))
        self.labelStelleRecensione.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelOra = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelOra.setObjectName(u"labelOra")
        self.labelOra.setGeometry(QRect(180, 190, 81, 20))
        self.labelOra.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelOra.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOraRecensione = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelOraRecensione.setObjectName(u"labelOraRecensione")
        self.labelOraRecensione.setGeometry(QRect(180, 220, 91, 20))
        self.labelOraRecensione.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelRecensioneIcon = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelRecensioneIcon.setObjectName(u"labelRecensioneIcon")
        self.labelRecensioneIcon.setGeometry(QRect(40, 40, 121, 121))
        self.labelRecensioneIcon.setPixmap(QPixmap(u"Viste/Immagini/RecensioneIconAmministratore.png"))
        self.labelRecensioneIcon.setScaledContents(True)
        self.labelTesto = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelTesto.setObjectName(u"labelTesto")
        self.labelTesto.setGeometry(QRect(290, 190, 81, 20))
        self.labelTesto.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTesto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIdRecensione = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelIdRecensione.setObjectName(u"labelIdRecensione")
        self.labelIdRecensione.setGeometry(QRect(180, 130, 131, 20))
        self.labelIdRecensione.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.textBrowserTesto = QTextBrowser(VistaVisualizzaRecensioneAmministratore)
        self.textBrowserTesto.setObjectName(u"textBrowserTesto")
        self.textBrowserTesto.setGeometry(QRect(290, 220, 401, 192))
        self.textBrowserTesto.setStyleSheet(u"QTextBrowser {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar:vertical {\n"
"	background: #B43700;\n"
"	border: 2px solid #190700;\n"
"    border-radius: 4px;\n"
"    width: 21px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::handle:vertical {\n"
"	background: #962D00;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::handle:vertical:hover {\n"
"    background: #C83200;\n"
"}\n"
"\n"
"QTextBrowser QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"    border: none;\n"
"}")
        self.labelCodiceFiscale = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelCodiceFiscale.setObjectName(u"labelCodiceFiscale")
        self.labelCodiceFiscale.setGeometry(QRect(390, 100, 161, 20))
        self.labelCodiceFiscale.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCodiceFiscale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCodiceFiscaleRecensione = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelCodiceFiscaleRecensione.setObjectName(u"labelCodiceFiscaleRecensione")
        self.labelCodiceFiscaleRecensione.setGeometry(QRect(390, 130, 131, 20))
        self.labelCodiceFiscaleRecensione.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")

        self.retranslateUi(VistaVisualizzaRecensioneAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaRecensioneAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaRecensioneAmministratore):
        VistaVisualizzaRecensioneAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Recensione - CineMax", None))
        self.Sfondo.setText("")
        self.labelId.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Identificativo:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Recensione", None))
        self.labelHomeButton.setText("")
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Data:", None))
        self.labelDataRecensione.setText("")
        self.labelStelle.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Stelle:", None))
        self.labelStelleRecensione.setText("")
        self.labelOra.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Ora:", None))
        self.labelOraRecensione.setText("")
        self.labelIndietroButton.setText("")
        self.labelRecensioneIcon.setText("")
        self.labelTesto.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Testo:", None))
        self.labelIdRecensione.setText("")
        self.labelCodiceFiscale.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Cliente:", None))
        self.labelCodiceFiscaleRecensione.setText("")
    # retranslateUi

