# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaAcquistoBigliettoCliente.ui'
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

class Ui_VistaAcquistoBigliettoCliente(object):
    def setupUi(self, VistaAcquistoBigliettoCliente):
        if not VistaAcquistoBigliettoCliente.objectName():
            VistaAcquistoBigliettoCliente.setObjectName(u"VistaAcquistoBigliettoCliente")
        VistaAcquistoBigliettoCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaAcquistoBigliettoCliente)
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
        self.labelIconaFotoCliente = QLabel(VistaAcquistoBigliettoCliente)
        self.labelIconaFotoCliente.setObjectName(u"labelIconaFotoCliente")
        self.labelIconaFotoCliente.setGeometry(QRect(40, 30, 121, 121))
        self.labelIconaFotoCliente.setPixmap(QPixmap(u"Immagini/IconaFotoCliente.png"))
        self.labelIconaFotoCliente.setScaledContents(True)
        self.labelTitolo = QLabel(VistaAcquistoBigliettoCliente)
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
        self.labelPosto = QLabel(VistaAcquistoBigliettoCliente)
        self.labelPosto.setObjectName(u"labelPosto")
        self.labelPosto.setGeometry(QRect(40, 180, 111, 20))
        self.labelPosto.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPosto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTipo = QLabel(VistaAcquistoBigliettoCliente)
        self.labelTipo.setObjectName(u"labelTipo")
        self.labelTipo.setGeometry(QRect(40, 240, 81, 20))
        self.labelTipo.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTipo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTipoPagamento = QLabel(VistaAcquistoBigliettoCliente)
        self.labelTipoPagamento.setObjectName(u"labelTipoPagamento")
        self.labelTipoPagamento.setGeometry(QRect(40, 300, 171, 20))
        self.labelTipoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTipoPagamento.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzo = QLabel(VistaAcquistoBigliettoCliente)
        self.labelPrezzo.setObjectName(u"labelPrezzo")
        self.labelPrezzo.setGeometry(QRect(40, 360, 81, 20))
        self.labelPrezzo.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPrezzo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButtonAcquista = QPushButton(VistaAcquistoBigliettoCliente)
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
        self.pushButtonAnnulla = QPushButton(VistaAcquistoBigliettoCliente)
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
        self.labelPostoBiglietto = QLabel(VistaAcquistoBigliettoCliente)
        self.labelPostoBiglietto.setObjectName(u"labelPostoBiglietto")
        self.labelPostoBiglietto.setGeometry(QRect(40, 200, 51, 20))
        self.labelPostoBiglietto.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelPrezzoBiglietto = QLabel(VistaAcquistoBigliettoCliente)
        self.labelPrezzoBiglietto.setObjectName(u"labelPrezzoBiglietto")
        self.labelPrezzoBiglietto.setGeometry(QRect(40, 380, 71, 20))
        self.labelPrezzoBiglietto.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.comboBoxTipo = QComboBox(VistaAcquistoBigliettoCliente)
        self.comboBoxTipo.setObjectName(u"comboBoxTipo")
        self.comboBoxTipo.setGeometry(QRect(40, 260, 76, 26))
        self.comboBoxTipo.setStyleSheet(u"QComboBox {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #321E00;\n"
"	color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"	border-radius: 4px;\n"
"    selection-background-color: #C86400;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #C86400;\n"
"}")
        self.comboBoxTipoPagamento = QComboBox(VistaAcquistoBigliettoCliente)
        self.comboBoxTipoPagamento.setObjectName(u"comboBoxTipoPagamento")
        self.comboBoxTipoPagamento.setGeometry(QRect(40, 320, 76, 26))
        self.comboBoxTipoPagamento.setStyleSheet(u"QComboBox {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #321E00;\n"
"	color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"	border-radius: 4px;\n"
"    selection-background-color: #C86400;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #C86400;\n"
"}")
        self.labelPrezzoPunti = QLabel(VistaAcquistoBigliettoCliente)
        self.labelPrezzoPunti.setObjectName(u"labelPrezzoPunti")
        self.labelPrezzoPunti.setGeometry(QRect(180, 360, 121, 20))
        self.labelPrezzoPunti.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPrezzoPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzoPuntiBiglietto = QLabel(VistaAcquistoBigliettoCliente)
        self.labelPrezzoPuntiBiglietto.setObjectName(u"labelPrezzoPuntiBiglietto")
        self.labelPrezzoPuntiBiglietto.setGeometry(QRect(180, 380, 71, 20))
        self.labelPrezzoPuntiBiglietto.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelErroreTipo = QLabel(VistaAcquistoBigliettoCliente)
        self.labelErroreTipo.setObjectName(u"labelErroreTipo")
        self.labelErroreTipo.setGeometry(QRect(130, 260, 191, 20))
        self.labelErroreTipo.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelErroreTipo.setScaledContents(False)
        self.labelErroreTipoPagamento = QLabel(VistaAcquistoBigliettoCliente)
        self.labelErroreTipoPagamento.setObjectName(u"labelErroreTipoPagamento")
        self.labelErroreTipoPagamento.setGeometry(QRect(130, 320, 191, 20))
        self.labelErroreTipoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelErroreTipoPagamento.setScaledContents(False)
        self.labelPunti = QLabel(VistaAcquistoBigliettoCliente)
        self.labelPunti.setObjectName(u"labelPunti")
        self.labelPunti.setGeometry(QRect(40, 420, 81, 20))
        self.labelPunti.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPuntiCliente = QLabel(VistaAcquistoBigliettoCliente)
        self.labelPuntiCliente.setObjectName(u"labelPuntiCliente")
        self.labelPuntiCliente.setGeometry(QRect(40, 440, 71, 20))
        self.labelPuntiCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelErrorePuntiInsufficenti = QLabel(VistaAcquistoBigliettoCliente)
        self.labelErrorePuntiInsufficenti.setObjectName(u"labelErrorePuntiInsufficenti")
        self.labelErrorePuntiInsufficenti.setGeometry(QRect(190, 440, 191, 20))
        self.labelErrorePuntiInsufficenti.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelErrorePuntiInsufficenti.setScaledContents(False)

        self.retranslateUi(VistaAcquistoBigliettoCliente)

        QMetaObject.connectSlotsByName(VistaAcquistoBigliettoCliente)
    # setupUi

    def retranslateUi(self, VistaAcquistoBigliettoCliente):
        VistaAcquistoBigliettoCliente.setWindowTitle(QCoreApplication.translate("VistaAcquistoBigliettoCliente", u"Acquisto Biglietto - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFotoCliente.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaAcquistoBigliettoCliente", u"Acquisto Biglietto", None))
        self.labelPosto.setText(QCoreApplication.translate("VistaAcquistoBigliettoCliente", u"Posto:", None))
        self.labelTipo.setText(QCoreApplication.translate("VistaAcquistoBigliettoCliente", u"Tipo:", None))
        self.labelTipoPagamento.setText(QCoreApplication.translate("VistaAcquistoBigliettoCliente", u"Metodo di Pagamento:", None))
        self.labelPrezzo.setText(QCoreApplication.translate("VistaAcquistoBigliettoCliente", u"Prezzo:", None))
        self.pushButtonAcquista.setText(QCoreApplication.translate("VistaAcquistoBigliettoCliente", u"Acquista", None))
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaAcquistoBigliettoCliente", u"Annulla", None))
        self.labelPostoBiglietto.setText("")
        self.labelPrezzoBiglietto.setText("")
        self.labelPrezzoPunti.setText(QCoreApplication.translate("VistaAcquistoBigliettoCliente", u"Prezzo Punti:", None))
        self.labelPrezzoPuntiBiglietto.setText("")
        self.labelErroreTipo.setText("")
        self.labelErroreTipoPagamento.setText("")
        self.labelPunti.setText(QCoreApplication.translate("VistaAcquistoBigliettoCliente", u"Saldo Punti:", None))
        self.labelPuntiCliente.setText("")
        self.labelErrorePuntiInsufficenti.setText("")
    # retranslateUi

