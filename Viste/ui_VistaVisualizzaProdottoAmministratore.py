# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaProdottoAmministratore.ui'
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

class Ui_VistaVisualizzaProdottoAmministratore(object):
    def setupUi(self, VistaVisualizzaProdottoAmministratore):
        if not VistaVisualizzaProdottoAmministratore.objectName():
            VistaVisualizzaProdottoAmministratore.setObjectName(u"VistaVisualizzaProdottoAmministratore")
        VistaVisualizzaProdottoAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaProdottoAmministratore)
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
        self.labelIconaFoto = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelIconaFoto.setObjectName(u"labelIconaFoto")
        self.labelIconaFoto.setGeometry(QRect(30, 30, 131, 131))
        self.labelIconaFoto.setPixmap(QPixmap(u"Immagini/IconaFotoAmministratore.png"))
        self.labelIconaFoto.setScaledContents(True)
        self.labelNome = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 291, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelHomeButton = ClickableLabel(VistaVisualizzaProdottoAmministratore)
        self.labelHomeButton.setObjectName(u"labelHomeButton")
        self.labelHomeButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButton.setPixmap(QPixmap(u"Immagini/HomeButtonAmministratore.png"))
        self.labelHomeButton.setScaledContents(True)
        self.labelIngredienti = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelIngredienti.setObjectName(u"labelIngredienti")
        self.labelIngredienti.setGeometry(QRect(40, 180, 81, 20))
        self.labelIngredienti.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelIngredienti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelNomeProdotto = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelNomeProdotto.setObjectName(u"labelNomeProdotto")
        self.labelNomeProdotto.setGeometry(QRect(180, 120, 221, 20))
        self.labelNomeProdotto.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIngredientiProdotto = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelIngredientiProdotto.setObjectName(u"labelIngredientiProdotto")
        self.labelIngredientiProdotto.setGeometry(QRect(40, 200, 511, 20))
        self.labelIngredientiProdotto.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelDisponibile = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelDisponibile.setObjectName(u"labelDisponibile")
        self.labelDisponibile.setGeometry(QRect(40, 360, 101, 20))
        self.labelDisponibile.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelDisponibile.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDisponibileProdotto = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelDisponibileProdotto.setObjectName(u"labelDisponibileProdotto")
        self.labelDisponibileProdotto.setGeometry(QRect(40, 380, 31, 20))
        self.labelDisponibileProdotto.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelAllergeni = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelAllergeni.setObjectName(u"labelAllergeni")
        self.labelAllergeni.setGeometry(QRect(40, 240, 81, 20))
        self.labelAllergeni.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelAllergeni.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelAllergeniProdotto = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelAllergeniProdotto.setObjectName(u"labelAllergeniProdotto")
        self.labelAllergeniProdotto.setGeometry(QRect(40, 260, 401, 20))
        self.labelAllergeniProdotto.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelPrezzo = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelPrezzo.setObjectName(u"labelPrezzo")
        self.labelPrezzo.setGeometry(QRect(40, 300, 81, 20))
        self.labelPrezzo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPrezzo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzoProdotto = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelPrezzoProdotto.setObjectName(u"labelPrezzoProdotto")
        self.labelPrezzoProdotto.setGeometry(QRect(40, 320, 81, 20))
        self.labelPrezzoProdotto.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaProdottoAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.pushButtonModifica = QPushButton(VistaVisualizzaProdottoAmministratore)
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
        self.labelPrezzoPunti = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelPrezzoPunti.setObjectName(u"labelPrezzoPunti")
        self.labelPrezzoPunti.setGeometry(QRect(190, 300, 121, 20))
        self.labelPrezzoPunti.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPrezzoPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzoPuntiProdotto = QLabel(VistaVisualizzaProdottoAmministratore)
        self.labelPrezzoPuntiProdotto.setObjectName(u"labelPrezzoPuntiProdotto")
        self.labelPrezzoPuntiProdotto.setGeometry(QRect(190, 320, 81, 20))
        self.labelPrezzoPuntiProdotto.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")

        self.retranslateUi(VistaVisualizzaProdottoAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaProdottoAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaProdottoAmministratore):
        VistaVisualizzaProdottoAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaProdottoAmministratore", u"Prodotto - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFoto.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaVisualizzaProdottoAmministratore", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaProdottoAmministratore", u"Prodotto", None))
        self.labelHomeButton.setText("")
        self.labelIngredienti.setText(QCoreApplication.translate("VistaVisualizzaProdottoAmministratore", u"Ingredienti:", None))
        self.labelNomeProdotto.setText("")
        self.labelIngredientiProdotto.setText("")
        self.labelDisponibile.setText(QCoreApplication.translate("VistaVisualizzaProdottoAmministratore", u"Disponibilit\u00e0:", None))
        self.labelDisponibileProdotto.setText("")
        self.labelAllergeni.setText(QCoreApplication.translate("VistaVisualizzaProdottoAmministratore", u"Allergeni:", None))
        self.labelAllergeniProdotto.setText("")
        self.labelPrezzo.setText(QCoreApplication.translate("VistaVisualizzaProdottoAmministratore", u"Prezzo:", None))
        self.labelPrezzoProdotto.setText("")
        self.labelIndietroButton.setText("")
        self.pushButtonModifica.setText(QCoreApplication.translate("VistaVisualizzaProdottoAmministratore", u"Modifica", None))
        self.labelPrezzoPunti.setText(QCoreApplication.translate("VistaVisualizzaProdottoAmministratore", u"Prezzo in Punti:", None))
        self.labelPrezzoPuntiProdotto.setText("")
    # retranslateUi

