# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaSpettacoloCliente.ui'
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

class Ui_VistaVisualizzaSpettacoloCliente(object):
    def setupUi(self, VistaVisualizzaSpettacoloCliente):
        if not VistaVisualizzaSpettacoloCliente.objectName():
            VistaVisualizzaSpettacoloCliente.setObjectName(u"VistaVisualizzaSpettacoloCliente")
        VistaVisualizzaSpettacoloCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaSpettacoloCliente)
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
        self.labelIconaFotoCliente = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelIconaFotoCliente.setObjectName(u"labelIconaFotoCliente")
        self.labelIconaFotoCliente.setGeometry(QRect(30, 30, 131, 131))
        self.labelIconaFotoCliente.setPixmap(QPixmap(u"Immagini/IconaFotoCliente.png"))
        self.labelIconaFotoCliente.setScaledContents(True)
        self.labelTitolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 100, 63, 20))
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitoloPrincipale = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelTitoloPrincipale.setObjectName(u"labelTitoloPrincipale")
        self.labelTitoloPrincipale.setGeometry(QRect(180, 30, 291, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitoloPrincipale.setFont(font1)
        self.labelTitoloPrincipale.setStyleSheet(u"QLabel {\n"
"    color: #C8B400;\n"
"}")
        self.labelTitoloPrincipale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelHomeButtonCliente = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelHomeButtonCliente.setObjectName(u"labelHomeButtonCliente")
        self.labelHomeButtonCliente.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButtonCliente.setPixmap(QPixmap(u"Immagini/HomeButtonCliente.png"))
        self.labelHomeButtonCliente.setScaledContents(True)
        self.labelGenere = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelGenere.setObjectName(u"labelGenere")
        self.labelGenere.setGeometry(QRect(40, 180, 81, 20))
        self.labelGenere.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelGenere.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitoloSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelTitoloSpettacolo.setObjectName(u"labelTitoloSpettacolo")
        self.labelTitoloSpettacolo.setGeometry(QRect(180, 120, 301, 20))
        self.labelTitoloSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelGenereSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelGenereSpettacolo.setObjectName(u"labelGenereSpettacolo")
        self.labelGenereSpettacolo.setGeometry(QRect(40, 200, 131, 20))
        self.labelGenereSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelOrarioInizio = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelOrarioInizio.setObjectName(u"labelOrarioInizio")
        self.labelOrarioInizio.setGeometry(QRect(40, 360, 101, 20))
        self.labelOrarioInizio.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelOrarioInizio.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOrarioInizioSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelOrarioInizioSpettacolo.setObjectName(u"labelOrarioInizioSpettacolo")
        self.labelOrarioInizioSpettacolo.setGeometry(QRect(40, 380, 41, 20))
        self.labelOrarioInizioSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelSala = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelSala.setObjectName(u"labelSala")
        self.labelSala.setGeometry(QRect(40, 240, 81, 20))
        self.labelSala.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelSala.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelSalaSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelSalaSpettacolo.setObjectName(u"labelSalaSpettacolo")
        self.labelSalaSpettacolo.setGeometry(QRect(40, 260, 31, 20))
        self.labelSalaSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelData = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(40, 300, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelDataSpettacolo.setObjectName(u"labelDataSpettacolo")
        self.labelDataSpettacolo.setGeometry(QRect(40, 320, 81, 20))
        self.labelDataSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelIndietroButtonCliente = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelIndietroButtonCliente.setObjectName(u"labelIndietroButtonCliente")
        self.labelIndietroButtonCliente.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButtonCliente.setPixmap(QPixmap(u"Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButtonCliente.setScaledContents(True)
        self.labelOrarioFine = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelOrarioFine.setObjectName(u"labelOrarioFine")
        self.labelOrarioFine.setGeometry(QRect(170, 360, 101, 20))
        self.labelOrarioFine.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelOrarioFine.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOrarioFineSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelOrarioFineSpettacolo.setObjectName(u"labelOrarioFineSpettacolo")
        self.labelOrarioFineSpettacolo.setGeometry(QRect(170, 380, 51, 20))
        self.labelOrarioFineSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelDurata = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelDurata.setObjectName(u"labelDurata")
        self.labelDurata.setGeometry(QRect(40, 420, 101, 20))
        self.labelDurata.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelDurata.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDurataSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelDurataSpettacolo.setObjectName(u"labelDurataSpettacolo")
        self.labelDurataSpettacolo.setGeometry(QRect(40, 440, 91, 20))
        self.labelDurataSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")

        self.retranslateUi(VistaVisualizzaSpettacoloCliente)

        QMetaObject.connectSlotsByName(VistaVisualizzaSpettacoloCliente)
    # setupUi

    def retranslateUi(self, VistaVisualizzaSpettacoloCliente):
        VistaVisualizzaSpettacoloCliente.setWindowTitle(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Spettacolo - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFotoCliente.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Titolo:", None))
        self.labelTitoloPrincipale.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Spettacolo", None))
        self.labelHomeButtonCliente.setText("")
        self.labelGenere.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Genere:", None))
        self.labelTitoloSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Film", None))
        self.labelGenereSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Fantasia", None))
        self.labelOrarioInizio.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Orario Inizio:", None))
        self.labelOrarioInizioSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"00:00", None))
        self.labelSala.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Sala:", None))
        self.labelSalaSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"1", None))
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Data:", None))
        self.labelDataSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"13/07/2025", None))
        self.labelIndietroButtonCliente.setText("")
        self.labelOrarioFine.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Orario Fine:", None))
        self.labelOrarioFineSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"02:00", None))
        self.labelDurata.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Durata:", None))
        self.labelDurataSpettacolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"120 miuti", None))
    # retranslateUi

