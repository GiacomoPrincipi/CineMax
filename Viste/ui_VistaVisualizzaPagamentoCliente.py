# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaPagamentoCliente.ui'
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

from clickablelabel import ClickableLabel

class Ui_VistaVisualizzaPagamentoCliente(object):
    def setupUi(self, VistaVisualizzaPagamentoCliente):
        if not VistaVisualizzaPagamentoCliente.objectName():
            VistaVisualizzaPagamentoCliente.setObjectName(u"VistaVisualizzaPagamentoCliente")
        VistaVisualizzaPagamentoCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaPagamentoCliente)
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
        self.labelIconaRicevuta = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelIconaRicevuta.setObjectName(u"labelIconaRicevuta")
        self.labelIconaRicevuta.setGeometry(QRect(20, 20, 151, 151))
        self.labelIconaRicevuta.setPixmap(QPixmap(u"Immagini/RicevutaIconCliente.png"))
        self.labelIconaRicevuta.setScaledContents(True)
        self.labelTitolo = QLabel(VistaVisualizzaPagamentoCliente)
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
        self.labelHomeButton = ClickableLabel(VistaVisualizzaPagamentoCliente)
        self.labelHomeButton.setObjectName(u"labelHomeButton")
        self.labelHomeButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButton.setPixmap(QPixmap(u"Immagini/HomeButtonCliente.png"))
        self.labelHomeButton.setScaledContents(True)
        self.labelNome = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 141, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelData = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(40, 180, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataPagamento = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelDataPagamento.setObjectName(u"labelDataPagamento")
        self.labelDataPagamento.setGeometry(QRect(40, 200, 91, 20))
        self.labelDataPagamento.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelTipo = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelTipo.setObjectName(u"labelTipo")
        self.labelTipo.setGeometry(QRect(40, 240, 81, 20))
        self.labelTipo.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTipo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTipoPagamento = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelTipoPagamento.setObjectName(u"labelTipoPagamento")
        self.labelTipoPagamento.setGeometry(QRect(40, 260, 111, 20))
        self.labelTipoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelImporto = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelImporto.setObjectName(u"labelImporto")
        self.labelImporto.setGeometry(QRect(40, 300, 81, 20))
        self.labelImporto.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelImporto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelImportoPagamento = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelImportoPagamento.setObjectName(u"labelImportoPagamento")
        self.labelImportoPagamento.setGeometry(QRect(40, 320, 91, 20))
        self.labelImportoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelOra = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelOra.setObjectName(u"labelOra")
        self.labelOra.setGeometry(QRect(180, 180, 81, 20))
        self.labelOra.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelOra.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOraPagamento = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelOraPagamento.setObjectName(u"labelOraPagamento")
        self.labelOraPagamento.setGeometry(QRect(180, 200, 51, 20))
        self.labelOraPagamento.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaPagamentoCliente)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelNomePagamento = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelNomePagamento.setObjectName(u"labelNomePagamento")
        self.labelNomePagamento.setGeometry(QRect(180, 120, 231, 20))
        self.labelNomePagamento.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")

        self.retranslateUi(VistaVisualizzaPagamentoCliente)

        QMetaObject.connectSlotsByName(VistaVisualizzaPagamentoCliente)
    # setupUi

    def retranslateUi(self, VistaVisualizzaPagamentoCliente):
        VistaVisualizzaPagamentoCliente.setWindowTitle(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Pagamento - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaRicevuta.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Pagamento", None))
        self.labelHomeButton.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Nome Articolo:", None))
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Data:", None))
        self.labelDataPagamento.setText("")
        self.labelTipo.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Tipo:", None))
        self.labelTipoPagamento.setText("")
        self.labelImporto.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Importo:", None))
        self.labelImportoPagamento.setText("")
        self.labelOra.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Ora:", None))
        self.labelOraPagamento.setText("")
        self.labelIndietroButton.setText("")
        self.labelNomePagamento.setText("")
    # retranslateUi

