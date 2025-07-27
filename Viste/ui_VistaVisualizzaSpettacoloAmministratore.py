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

from clickablelabel import ClickableLabel

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
        self.labelIconaFoto = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelIconaFoto.setObjectName(u"labelIconaFoto")
        self.labelIconaFoto.setGeometry(QRect(30, 30, 131, 131))
        self.labelIconaFoto.setPixmap(QPixmap(u"Immagini/IconaFotoAmministratore.png"))
        self.labelIconaFoto.setScaledContents(True)
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
        self.labelHomeButton = ClickableLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelHomeButton.setObjectName(u"labelHomeButton")
        self.labelHomeButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButton.setPixmap(QPixmap(u"Immagini/HomeButtonAmministratore.png"))
        self.labelHomeButton.setScaledContents(True)
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
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
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
        self.labelStato = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelStato.setObjectName(u"labelStato")
        self.labelStato.setGeometry(QRect(520, 100, 111, 20))
        self.labelStato.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelStato.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelStatoSpettacolo = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelStatoSpettacolo.setObjectName(u"labelStatoSpettacolo")
        self.labelStatoSpettacolo.setGeometry(QRect(520, 120, 101, 20))
        self.labelStatoSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelPrezzo = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelPrezzo.setObjectName(u"labelPrezzo")
        self.labelPrezzo.setGeometry(QRect(370, 220, 101, 20))
        self.labelPrezzo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPrezzo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzoPunti = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelPrezzoPunti.setObjectName(u"labelPrezzoPunti")
        self.labelPrezzoPunti.setGeometry(QRect(370, 290, 101, 20))
        self.labelPrezzoPunti.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPrezzoPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzoSpettacolo = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelPrezzoSpettacolo.setObjectName(u"labelPrezzoSpettacolo")
        self.labelPrezzoSpettacolo.setGeometry(QRect(370, 240, 131, 20))
        self.labelPrezzoSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelPrezzoSpettacolo_2 = QLabel(VistaVisualizzaSpettacoloAmministratore)
        self.labelPrezzoSpettacolo_2.setObjectName(u"labelPrezzoSpettacolo_2")
        self.labelPrezzoSpettacolo_2.setGeometry(QRect(370, 310, 131, 20))
        self.labelPrezzoSpettacolo_2.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")

        self.retranslateUi(VistaVisualizzaSpettacoloAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaSpettacoloAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaSpettacoloAmministratore):
        VistaVisualizzaSpettacoloAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Spettacolo - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFoto.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Titolo:", None))
        self.labelTitoloPrincipale.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Spettacolo", None))
        self.labelHomeButton.setText("")
        self.labelGenere.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Genere:", None))
        self.labelTitoloSpettacolo.setText("")
        self.labelGenereSpettacolo.setText("")
        self.labelOrarioInizio.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Orario Inizio:", None))
        self.labelOrarioInizioSpettacolo.setText("")
        self.labelSala.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Sala:", None))
        self.labelSalaSpettacolo.setText("")
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Data:", None))
        self.labelDataSpettacolo.setText("")
        self.labelIndietroButton.setText("")
        self.labelOrarioFine.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Orario Fine:", None))
        self.labelOrarioFineSpettacolo.setText("")
        self.labelDurata.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Durata:", None))
        self.labelDurataSpettacolo.setText("")
        self.pushButtonModifica.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Modifica", None))
        self.labelStato.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Stato:", None))
        self.labelStatoSpettacolo.setText("")
        self.labelPrezzo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u"Prezzo:", None))
        self.labelPrezzoPunti.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloAmministratore", u" Prezzo in punti:", None))
        self.labelPrezzoSpettacolo.setText("")
        self.labelPrezzoSpettacolo_2.setText("")
    # retranslateUi

