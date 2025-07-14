# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaRecensioneCliente.ui'
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

class Ui_VistaVisualizzaRecensioneCliente(object):
    def setupUi(self, VistaVisualizzaRecensioneCliente):
        if not VistaVisualizzaRecensioneCliente.objectName():
            VistaVisualizzaRecensioneCliente.setObjectName(u"VistaVisualizzaRecensioneCliente")
        VistaVisualizzaRecensioneCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaRecensioneCliente)
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
        self.labelTitolo = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 291, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C8B400;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelHomeButtonCliente = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelHomeButtonCliente.setObjectName(u"labelHomeButtonCliente")
        self.labelHomeButtonCliente.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButtonCliente.setPixmap(QPixmap(u"Immagini/HomeButtonCliente.png"))
        self.labelHomeButtonCliente.setScaledContents(True)
        self.labelData = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(40, 180, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataPagamento = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelDataPagamento.setObjectName(u"labelDataPagamento")
        self.labelDataPagamento.setGeometry(QRect(40, 200, 91, 20))
        self.labelDataPagamento.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelTipo = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelTipo.setObjectName(u"labelTipo")
        self.labelTipo.setGeometry(QRect(40, 240, 81, 20))
        self.labelTipo.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTipo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTipoPagamento = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelTipoPagamento.setObjectName(u"labelTipoPagamento")
        self.labelTipoPagamento.setGeometry(QRect(40, 260, 41, 20))
        self.labelTipoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelOra = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelOra.setObjectName(u"labelOra")
        self.labelOra.setGeometry(QRect(180, 180, 81, 20))
        self.labelOra.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelOra.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOraPagamento = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelOraPagamento.setObjectName(u"labelOraPagamento")
        self.labelOraPagamento.setGeometry(QRect(180, 200, 51, 20))
        self.labelOraPagamento.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelIndietroButtonCliente = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelIndietroButtonCliente.setObjectName(u"labelIndietroButtonCliente")
        self.labelIndietroButtonCliente.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButtonCliente.setPixmap(QPixmap(u"Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButtonCliente.setScaledContents(True)
        self.labelProfiloCliente = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelProfiloCliente.setObjectName(u"labelProfiloCliente")
        self.labelProfiloCliente.setGeometry(QRect(40, 50, 121, 121))
        self.labelProfiloCliente.setPixmap(QPixmap(u"Immagini/RecensioneIconCliente.png"))
        self.labelProfiloCliente.setScaledContents(True)
        self.labelTesto = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelTesto.setObjectName(u"labelTesto")
        self.labelTesto.setGeometry(QRect(290, 180, 81, 20))
        self.labelTesto.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTesto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTestoPagamento = QLabel(VistaVisualizzaRecensioneCliente)
        self.labelTestoPagamento.setObjectName(u"labelTestoPagamento")
        self.labelTestoPagamento.setGeometry(QRect(290, 200, 401, 201))
        self.labelTestoPagamento.setStyleSheet(u"QLabel {\n"
"	background-color: #EBF064;\n"
"	color: #965A00;\n"
"	border: 1px solid #8C8C3C;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.labelTestoPagamento.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelTestoPagamento.setWordWrap(True)

        self.retranslateUi(VistaVisualizzaRecensioneCliente)

        QMetaObject.connectSlotsByName(VistaVisualizzaRecensioneCliente)
    # setupUi

    def retranslateUi(self, VistaVisualizzaRecensioneCliente):
        VistaVisualizzaRecensioneCliente.setWindowTitle(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Recensione - CineMax", None))
        self.Sfondo.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Recensione", None))
        self.labelHomeButtonCliente.setText("")
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Data:", None))
        self.labelDataPagamento.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"14/07/2025", None))
        self.labelTipo.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Stelle:", None))
        self.labelTipoPagamento.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"n/5", None))
        self.labelOra.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Ora:", None))
        self.labelOraPagamento.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"00:00", None))
        self.labelIndietroButtonCliente.setText("")
        self.labelProfiloCliente.setText("")
        self.labelTesto.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Testo:", None))
        self.labelTestoPagamento.setText(QCoreApplication.translate("VistaVisualizzaRecensioneCliente", u"Siete Fantastici", None))
    # retranslateUi

