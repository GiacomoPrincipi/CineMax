# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaSpettacoloAmministratore.ui'
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

class Ui_VistaVisualizzaSpettacoloAmministratore(object):
    def setupUi(self, VistaVisualizzaSpettacoloAmministratore):
        if not VistaVisualizzaSpettacoloAmministratore.objectName():
            VistaVisualizzaSpettacoloAmministratore.setObjectName(u"VistaVisualizzaSpettacoloAmministratore")
        VistaVisualizzaSpettacoloAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaSpettacoloAmministratore)
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
        self.labelIconaFotoAmministratore = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelIconaFotoAmministratore.setObjectName(u"labelIconaFotoAmministratore")
        self.labelIconaFotoAmministratore.setGeometry(QRect(30, 30, 131, 131))
        self.labelIconaFotoAmministratore.setPixmap(QPixmap(u"Immagini/IconaFotoAmministratore.png"))
        self.labelIconaFotoAmministratore.setScaledContents(True)
        self.labelTitolo = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 100, 63, 20))
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitoloPrincipale = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelTitoloPrincipale.setObjectName(u"labelTitoloPrincipale")
        self.labelTitoloPrincipale.setGeometry(QRect(180, 30, 291, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitoloPrincipale.setFont(font1)
        self.labelTitoloPrincipale.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTitoloPrincipale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelHomeButtonAmministratore = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelHomeButtonAmministratore.setObjectName(u"labelHomeButtonAmministratore")
        self.labelHomeButtonAmministratore.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButtonAmministratore.setPixmap(QPixmap(u"Immagini/HomeButtonAmministratore.png"))
        self.labelHomeButtonAmministratore.setScaledContents(True)
        self.labelGenere = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelGenere.setObjectName(u"labelGenere")
        self.labelGenere.setGeometry(QRect(40, 180, 81, 20))
        self.labelGenere.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelGenere.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitoloSpettacolo = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelTitoloSpettacolo.setObjectName(u"labelTitoloSpettacolo")
        self.labelTitoloSpettacolo.setGeometry(QRect(180, 120, 301, 20))
        self.labelTitoloSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelGenereSpettacolo = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelGenereSpettacolo.setObjectName(u"labelGenereSpettacolo")
        self.labelGenereSpettacolo.setGeometry(QRect(40, 200, 131, 20))
        self.labelGenereSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelOrarioInizio = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelOrarioInizio.setObjectName(u"labelOrarioInizio")
        self.labelOrarioInizio.setGeometry(QRect(40, 360, 101, 20))
        self.labelOrarioInizio.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelOrarioInizio.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOrarioInizioSpettacolo = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelOrarioInizioSpettacolo.setObjectName(u"labelOrarioInizioSpettacolo")
        self.labelOrarioInizioSpettacolo.setGeometry(QRect(40, 380, 41, 20))
        self.labelOrarioInizioSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelSala = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelSala.setObjectName(u"labelSala")
        self.labelSala.setGeometry(QRect(40, 240, 81, 20))
        self.labelSala.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelSala.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelSalaSpettacolo = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelSalaSpettacolo.setObjectName(u"labelSalaSpettacolo")
        self.labelSalaSpettacolo.setGeometry(QRect(40, 260, 31, 20))
        self.labelSalaSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelData = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(40, 300, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataSpettacolo = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelDataSpettacolo.setObjectName(u"labelDataSpettacolo")
        self.labelDataSpettacolo.setGeometry(QRect(40, 320, 81, 20))
        self.labelDataSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIndietroButtonAmministratore = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelIndietroButtonAmministratore.setObjectName(u"labelIndietroButtonAmministratore")
        self.labelIndietroButtonAmministratore.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButtonAmministratore.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButtonAmministratore.setScaledContents(True)
        self.labelOrarioFine = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelOrarioFine.setObjectName(u"labelOrarioFine")
        self.labelOrarioFine.setGeometry(QRect(170, 360, 101, 20))
        self.labelOrarioFine.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelOrarioFine.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOrarioFineSpettacolo = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelOrarioFineSpettacolo.setObjectName(u"labelOrarioFineSpettacolo")
        self.labelOrarioFineSpettacolo.setGeometry(QRect(170, 380, 51, 20))
        self.labelOrarioFineSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelDurata = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelDurata.setObjectName(u"labelDurata")
        self.labelDurata.setGeometry(QRect(40, 420, 101, 20))
        self.labelDurata.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelDurata.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDurataSpettacolo = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelDurataSpettacolo.setObjectName(u"labelDurataSpettacolo")
        self.labelDurataSpettacolo.setGeometry(QRect(40, 440, 91, 20))
        self.labelDurataSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.pushButtonModifica = QPushButton(VistaVisualizzaSpettacoloAmministratore)
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

        self.retranslateUi(VistaVisualizzaSpettacoloAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaSpettacoloAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaSpettacoloAmministratore):
        VistaVisualizzaSpettacoloAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Spettacolo - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFotoAmministratore.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Titolo:", None))
        self.labelTitoloPrincipale.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Spettacolo", None))
        self.labelHomeButtonAmministratore.setText("")
        self.labelGenere.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Genere:", None))
        self.labelTitoloSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Film", None))
        self.labelGenereSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Fantasia", None))
        self.labelOrarioInizio.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Orario Inizio:", None))
        self.labelOrarioInizioSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"00:00", None))
        self.labelSala.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Sala:", None))
        self.labelSalaSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"1", None))
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Data:", None))
        self.labelDataSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"13/07/2025", None))
        self.labelIndietroButtonAmministratore.setText("")
        self.labelOrarioFine.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Orario Fine:", None))
        self.labelOrarioFineSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"02:00", None))
        self.labelDurata.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Durata:", None))
        self.labelDurataSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"120 miuti", None))
        self.pushButtonModifica.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Modifica", None))
    # retranslateUi

