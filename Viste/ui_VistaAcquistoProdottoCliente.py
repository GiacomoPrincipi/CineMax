# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaAcquistoProdottoCliente.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_VistaAcquistoProdottoCliente(object):
    def setupUi(self, VistaAcquistoProdottoCliente):
        if not VistaAcquistoProdottoCliente.objectName():
            VistaAcquistoProdottoCliente.setObjectName(u"VistaAcquistoProdottoCliente")
        VistaAcquistoProdottoCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaAcquistoProdottoCliente)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"                stop: 0 #321E00,\n"
"        stop: 1 #643C00\n"
"    );\n"
"}")
        self.labelIconaFotoCliente = QLabel(VistaAcquistoProdottoCliente)
        self.labelIconaFotoCliente.setObjectName(u"labelIconaFotoCliente")
        self.labelIconaFotoCliente.setGeometry(QRect(40, 30, 121, 121))
        self.labelIconaFotoCliente.setPixmap(QPixmap(u"Immagini/IconaFotoCliente.png"))
        self.labelIconaFotoCliente.setScaledContents(True)
        self.labelTitolo = QLabel(VistaAcquistoProdottoCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 371, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C8B400;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPosto = QLabel(VistaAcquistoProdottoCliente)
        self.labelPosto.setObjectName(u"labelPosto")
        self.labelPosto.setGeometry(QRect(40, 180, 111, 20))
        self.labelPosto.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPosto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTipoPagamento = QLabel(VistaAcquistoProdottoCliente)
        self.labelTipoPagamento.setObjectName(u"labelTipoPagamento")
        self.labelTipoPagamento.setGeometry(QRect(40, 180, 171, 20))
        self.labelTipoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTipoPagamento.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzo = QLabel(VistaAcquistoProdottoCliente)
        self.labelPrezzo.setObjectName(u"labelPrezzo")
        self.labelPrezzo.setGeometry(QRect(40, 240, 81, 20))
        self.labelPrezzo.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPrezzo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButtonAcquista = QPushButton(VistaAcquistoProdottoCliente)
        self.pushButtonAcquista.setObjectName(u"pushButtonAcquista")
        self.pushButtonAcquista.setGeometry(QRect(670, 450, 91, 29))
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
        self.pushButtonAnnulla = QPushButton(VistaAcquistoProdottoCliente)
        self.pushButtonAnnulla.setObjectName(u"pushButtonAnnulla")
        self.pushButtonAnnulla.setGeometry(QRect(560, 450, 91, 29))
        self.pushButtonAnnulla.setStyleSheet(u"QPushButton {\n"
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
        self.labelPrezzoProdotto = QLabel(VistaAcquistoProdottoCliente)
        self.labelPrezzoProdotto.setObjectName(u"labelPrezzoProdotto")
        self.labelPrezzoProdotto.setGeometry(QRect(40, 260, 71, 20))
        self.labelPrezzoProdotto.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.comboBoxTipoPagamento = QComboBox(VistaAcquistoProdottoCliente)
        self.comboBoxTipoPagamento.setObjectName(u"comboBoxTipoPagamento")
        self.comboBoxTipoPagamento.setGeometry(QRect(40, 200, 76, 26))
        self.comboBoxTipoPagamento.setStyleSheet(u"QComboBox {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #321E00;\n"
"        color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"        border-radius: 4px;\n"
"    selection-background-color: #C86400;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #C86400;\n"
"}")
        self.labelErroreTipoPagamento = QLabel(VistaAcquistoProdottoCliente)
        self.labelErroreTipoPagamento.setObjectName(u"labelErroreTipoPagamento")
        self.labelErroreTipoPagamento.setGeometry(QRect(130, 200, 191, 20))
        self.labelErroreTipoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelErroreTipoPagamento.setScaledContents(False)
        self.labelPrezzoPunti = QLabel(VistaAcquistoProdottoCliente)
        self.labelPrezzoPunti.setObjectName(u"labelPrezzoPunti")
        self.labelPrezzoPunti.setGeometry(QRect(190, 240, 91, 20))
        self.labelPrezzoPunti.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPrezzoPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzoPuntiProdotto = QLabel(VistaAcquistoProdottoCliente)
        self.labelPrezzoPuntiProdotto.setObjectName(u"labelPrezzoPuntiProdotto")
        self.labelPrezzoPuntiProdotto.setGeometry(QRect(190, 260, 71, 20))
        self.labelPrezzoPuntiProdotto.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelErrorePuntiInsufficenti = QLabel(VistaAcquistoProdottoCliente)
        self.labelErrorePuntiInsufficenti.setObjectName(u"labelErrorePuntiInsufficenti")
        self.labelErrorePuntiInsufficenti.setGeometry(QRect(200, 320, 191, 20))
        self.labelErrorePuntiInsufficenti.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelErrorePuntiInsufficenti.setScaledContents(False)
        self.labelPunti = QLabel(VistaAcquistoProdottoCliente)
        self.labelPunti.setObjectName(u"labelPunti")
        self.labelPunti.setGeometry(QRect(40, 290, 81, 20))
        self.labelPunti.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPuntiCliente = QLabel(VistaAcquistoProdottoCliente)
        self.labelPuntiCliente.setObjectName(u"labelPuntiCliente")
        self.labelPuntiCliente.setGeometry(QRect(40, 310, 71, 20))
        self.labelPuntiCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")

        self.retranslateUi(VistaAcquistoProdottoCliente)

        QMetaObject.connectSlotsByName(VistaAcquistoProdottoCliente)
    # setupUi

    def retranslateUi(self, VistaAcquistoProdottoCliente):
        VistaAcquistoProdottoCliente.setWindowTitle(QCoreApplication.translate("VistaAcquistoProdottoCliente", u"Acquisto Prodottoo - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFotoCliente.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaAcquistoProdottoCliente", u"Acquisto Prodotto", None))
        self.labelPosto.setText("")
        self.labelTipoPagamento.setText(QCoreApplication.translate("VistaAcquistoProdottoCliente", u"Metodo di Pagamento:", None))
        self.labelPrezzo.setText(QCoreApplication.translate("VistaAcquistoProdottoCliente", u"Prezzo:", None))
        self.pushButtonAcquista.setText(QCoreApplication.translate("VistaAcquistoProdottoCliente", u"Acquista", None))
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaAcquistoProdottoCliente", u"Annulla", None))
        self.labelPrezzoProdotto.setText("")
        self.labelErroreTipoPagamento.setText("")
        self.labelPrezzoPunti.setText(QCoreApplication.translate("VistaAcquistoProdottoCliente", u"Prezzo Punti:", None))
        self.labelPrezzoPuntiProdotto.setText("")
        self.labelErrorePuntiInsufficenti.setText("")
        self.labelPunti.setText(QCoreApplication.translate("VistaAcquistoProdottoCliente", u"Saldo Punti:", None))
        self.labelPuntiCliente.setText("")
    # retranslateUi

