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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

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
        self.labelIconaFotoCliente = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelIconaFotoCliente.setObjectName(u"labelIconaFotoCliente")
        self.labelIconaFotoCliente.setGeometry(QRect(30, 30, 131, 131))
        self.labelIconaFotoCliente.setPixmap(QPixmap(u"Immagini/IconaFotoCliente.png"))
        self.labelIconaFotoCliente.setScaledContents(True)
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
        self.labelHomeButtonCliente = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelHomeButtonCliente.setObjectName(u"labelHomeButtonCliente")
        self.labelHomeButtonCliente.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButtonCliente.setPixmap(QPixmap(u"Immagini/HomeButtonCliente.png"))
        self.labelHomeButtonCliente.setScaledContents(True)
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
        self.labelDisponibile = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelDisponibile.setObjectName(u"labelDisponibile")
        self.labelDisponibile.setGeometry(QRect(40, 360, 101, 20))
        self.labelDisponibile.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelDisponibile.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDisponibileProdotto = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelDisponibileProdotto.setObjectName(u"labelDisponibileProdotto")
        self.labelDisponibileProdotto.setGeometry(QRect(40, 380, 31, 20))
        self.labelDisponibileProdotto.setStyleSheet(u"QLabel {\n"
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
        self.labelIndietroButtonCliente = QLabel(VistaVisualizzaProdottoCliente__)
        self.labelIndietroButtonCliente.setObjectName(u"labelIndietroButtonCliente")
        self.labelIndietroButtonCliente.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButtonCliente.setPixmap(QPixmap(u"Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButtonCliente.setScaledContents(True)

        self.retranslateUi(VistaVisualizzaProdottoCliente__)

        QMetaObject.connectSlotsByName(VistaVisualizzaProdottoCliente__)
    # setupUi

    def retranslateUi(self, VistaVisualizzaProdottoCliente__):
        VistaVisualizzaProdottoCliente__.setWindowTitle(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Prodotto - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFotoCliente.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Nome:", None))
        self.labelTitoloPrincipale.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Prodotto", None))
        self.labelHomeButtonCliente.setText("")
        self.labelIngredienti.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Ingredienti:", None))
        self.labelNomeProdotto.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Prodotto", None))
        self.labelIngredientiProdotto.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Ingrediente1, Ingradiente2", None))
        self.labelDisponibile.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Disponibilit\u00e0:", None))
        self.labelDisponibileProdotto.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"si", None))
        self.labelAllergeni.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Allergeni:", None))
        self.labelAllergeniProdotto.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Allergene1, Allergene2, Allergene3", None))
        self.labelPrezzo.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"Prezzo:", None))
        self.labelPrezzoProdotto.setText(QCoreApplication.translate("VistaVisualizzaProdottoCliente  ", u"00,00 $", None))
        self.labelIndietroButtonCliente.setText("")
    # retranslateUi

