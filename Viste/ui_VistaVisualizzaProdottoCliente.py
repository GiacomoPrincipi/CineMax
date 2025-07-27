# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaProdottoCliente.ui'
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

class Ui_VistaVisualizzaProdottoCliente  (object):
    def setupUi(self, VistaVisualizzaProdottoCliente__):
        if not VistaVisualizzaProdottoCliente__.objectName():
            VistaVisualizzaProdottoCliente__.setObjectName(u"VistaVisualizzaProdottoCliente__")
        VistaVisualizzaProdottoCliente__.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaProdottoCliente__)
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
        self.labelIconaFoto = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelIconaFoto.setObjectName(u"labelIconaFoto")
        self.labelIconaFoto.setGeometry(QRect(30, 30, 131, 131))
        self.labelIconaFoto.setPixmap(QPixmap(u"Immagini/IconaFotoCliente.png"))
        self.labelIconaFoto.setScaledContents(True)
        self.labelNome = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitoloPrincipale = QLabel(VistaVisualizzaProdottoCliente__)
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
        self.labelHomeButton = ClickableLabel(VistaVisualizzaProdottoCliente__)
        self.labelHomeButton.setObjectName(u"labelHomeButton")
        self.labelHomeButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButton.setPixmap(QPixmap(u"Immagini/HomeButtonCliente.png"))
        self.labelHomeButton.setScaledContents(True)
        self.labelIngredienti = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelIngredienti.setObjectName(u"labelIngredienti")
        self.labelIngredienti.setGeometry(QRect(40, 180, 81, 20))
        self.labelIngredienti.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelIngredienti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelNomeProdotto = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelNomeProdotto.setObjectName(u"labelNomeProdotto")
        self.labelNomeProdotto.setGeometry(QRect(180, 120, 221, 20))
        self.labelNomeProdotto.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelIngredientiProdotto = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelIngredientiProdotto.setObjectName(u"labelIngredientiProdotto")
        self.labelIngredientiProdotto.setGeometry(QRect(40, 200, 511, 20))
        self.labelIngredientiProdotto.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelAllergeni = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelAllergeni.setObjectName(u"labelAllergeni")
        self.labelAllergeni.setGeometry(QRect(40, 240, 81, 20))
        self.labelAllergeni.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelAllergeni.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelAllergeniProdotto = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelAllergeniProdotto.setObjectName(u"labelAllergeniProdotto")
        self.labelAllergeniProdotto.setGeometry(QRect(40, 260, 401, 20))
        self.labelAllergeniProdotto.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelPrezzo = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelPrezzo.setObjectName(u"labelPrezzo")
        self.labelPrezzo.setGeometry(QRect(40, 300, 81, 20))
        self.labelPrezzo.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPrezzo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzoProdotto = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelPrezzoProdotto.setObjectName(u"labelPrezzoProdotto")
        self.labelPrezzoProdotto.setGeometry(QRect(40, 320, 81, 20))
        self.labelPrezzoProdotto.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaProdottoCliente__)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelPrezzoPunti = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelPrezzoPunti.setObjectName(u"labelPrezzoPunti")
        self.labelPrezzoPunti.setGeometry(QRect(210, 300, 111, 20))
        self.labelPrezzoPunti.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPrezzoPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzoPuntiProdotto = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelPrezzoPuntiProdotto.setObjectName(u"labelPrezzoPuntiProdotto")
        self.labelPrezzoPuntiProdotto.setGeometry(QRect(210, 320, 111, 20))
        self.labelPrezzoPuntiProdotto.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.pushButtonAcquista = QPushButton(VistaVisualizzaProdottoCliente__)
        self.pushButtonAcquista.setObjectName(u"pushButtonAcquista")
        self.pushButtonAcquista.setGeometry(QRect(670, 440, 91, 29))
        self.pushButtonAcquista.setStyleSheet(u"QPushButton {\n"
"    background-color: #963C00;\n"
"    color: #FF7800;\n"
"    border: 2px solid #502800;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C86400;\n"
"}\n"
"")

        self.retranslateUi(VistaVisualizzaProdottoCliente__)

        QMetaObject.connectSlotsByName(VistaVisualizzaProdottoCliente__)
    # setupUi

    def retranslateUi(self, VistaVisualizzaProdottoCliente__):
        VistaVisualizzaProdottoCliente__.setWindowTitle(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Prodotto - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFoto.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Nome:", None))
        self.labelTitoloPrincipale.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Prodotto", None))
        self.labelHomeButton.setText("")
        self.labelIngredienti.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Ingredienti:", None))
        self.labelNomeProdotto.setText("")
        self.labelIngredientiProdotto.setText("")
        self.labelAllergeni.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Allergeni:", None))
        self.labelAllergeniProdotto.setText("")
        self.labelPrezzo.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Prezzo:", None))
        self.labelPrezzoProdotto.setText("")
        self.labelIndietroButton.setText("")
        self.labelPrezzoPunti.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Prezzo in Punti:", None))
        self.labelPrezzoPuntiProdotto.setText("")
        self.pushButtonAcquista.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Acquista", None))
    # retranslateUi

