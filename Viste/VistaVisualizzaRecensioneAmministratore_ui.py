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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

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
"        stop: 0 #320F00,\n"
"        stop: 1 #641E00\n"
"    );\n"
"}")
        self.labelCliente = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelCliente.setObjectName(u"labelCliente")
        self.labelCliente.setGeometry(QRect(180, 100, 63, 20))
        self.labelCliente.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCliente.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaVisualizzaRecensioneAmministratore)
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
        self.labelHomeButtonAmministratore = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelHomeButtonAmministratore.setObjectName(u"labelHomeButtonAmministratore")
        self.labelHomeButtonAmministratore.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButtonAmministratore.setPixmap(QPixmap(u"Immagini/HomeButtonAmministratore.png"))
        self.labelHomeButtonAmministratore.setScaledContents(True)
        self.labelData = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(40, 180, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataPagamento = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelDataPagamento.setObjectName(u"labelDataPagamento")
        self.labelDataPagamento.setGeometry(QRect(40, 200, 91, 20))
        self.labelDataPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelTipo = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelTipo.setObjectName(u"labelTipo")
        self.labelTipo.setGeometry(QRect(40, 240, 81, 20))
        self.labelTipo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTipo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTipoPagamento = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelTipoPagamento.setObjectName(u"labelTipoPagamento")
        self.labelTipoPagamento.setGeometry(QRect(40, 260, 41, 20))
        self.labelTipoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelOra = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelOra.setObjectName(u"labelOra")
        self.labelOra.setGeometry(QRect(180, 180, 81, 20))
        self.labelOra.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelOra.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOraPagamento = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelOraPagamento.setObjectName(u"labelOraPagamento")
        self.labelOraPagamento.setGeometry(QRect(180, 200, 51, 20))
        self.labelOraPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIndietroButtonAmministratore = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelIndietroButtonAmministratore.setObjectName(u"labelIndietroButtonAmministratore")
        self.labelIndietroButtonAmministratore.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButtonAmministratore.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButtonAmministratore.setScaledContents(True)
        self.labelButtonCliente = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelButtonCliente.setObjectName(u"labelButtonCliente")
        self.labelButtonCliente.setGeometry(QRect(180, 120, 51, 51))
        self.labelButtonCliente.setPixmap(QPixmap(u"Immagini/profiloButtonAmministratore.png"))
        self.labelButtonCliente.setScaledContents(True)
        self.labelProfiloAmministratore = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelProfiloAmministratore.setObjectName(u"labelProfiloAmministratore")
        self.labelProfiloAmministratore.setGeometry(QRect(40, 50, 121, 121))
        self.labelProfiloAmministratore.setPixmap(QPixmap(u"Immagini/RecensioneIconAmministratore.png"))
        self.labelProfiloAmministratore.setScaledContents(True)
        self.labelTesto = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelTesto.setObjectName(u"labelTesto")
        self.labelTesto.setGeometry(QRect(290, 180, 81, 20))
        self.labelTesto.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTesto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTestoPagamento = QLabel(VistaVisualizzaRecensioneAmministratore)
        self.labelTestoPagamento.setObjectName(u"labelTestoPagamento")
        self.labelTestoPagamento.setGeometry(QRect(290, 200, 401, 201))
        self.labelTestoPagamento.setStyleSheet(u"QLabel {\n"
"	background-color: #EB7864;\n"
"    color: #962D00;\n"
"	border: 1px solid #8C463C;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.labelTestoPagamento.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelTestoPagamento.setWordWrap(True)

        self.retranslateUi(VistaVisualizzaRecensioneAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaRecensioneAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaRecensioneAmministratore):
        VistaVisualizzaRecensioneAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Recensione - CineMax", None))
        self.Sfondo.setText("")
        self.labelCliente.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Cliente:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Recensione", None))
        self.labelHomeButtonAmministratore.setText("")
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Data:", None))
        self.labelDataPagamento.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"14/07/2025", None))
        self.labelTipo.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Stelle:", None))
        self.labelTipoPagamento.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"n/5", None))
        self.labelOra.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Ora:", None))
        self.labelOraPagamento.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"00:00", None))
        self.labelIndietroButtonAmministratore.setText("")
        self.labelButtonCliente.setText("")
        self.labelProfiloAmministratore.setText("")
        self.labelTesto.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"Testo:", None))
        self.labelTestoPagamento.setText(QCoreApplication.translate("VistaVisualizzaRecensioneAmministratore", u"ciao io sono claudio e volevo dire che siete fantastici top top top", None))
    # retranslateUi

