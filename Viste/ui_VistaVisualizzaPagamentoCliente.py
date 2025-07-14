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
        self.labelRicevutaIconCliente = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelRicevutaIconCliente.setObjectName(u"labelRicevutaIconCliente")
        self.labelRicevutaIconCliente.setGeometry(QRect(20, 20, 151, 151))
        self.labelRicevutaIconCliente.setPixmap(QPixmap(u"Immagini/RicevutaIconCliente.png"))
        self.labelRicevutaIconCliente.setScaledContents(True)
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
        self.labelHomeButtonCliente = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelHomeButtonCliente.setObjectName(u"labelHomeButtonCliente")
        self.labelHomeButtonCliente.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButtonCliente.setPixmap(QPixmap(u"Immagini/HomeButtonCliente.png"))
        self.labelHomeButtonCliente.setScaledContents(True)
        self.labelArticolo = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelArticolo.setObjectName(u"labelArticolo")
        self.labelArticolo.setGeometry(QRect(180, 100, 81, 20))
        self.labelArticolo.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelArticolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
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
        self.labelIndietroButtonCliente = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelIndietroButtonCliente.setObjectName(u"labelIndietroButtonCliente")
        self.labelIndietroButtonCliente.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButtonCliente.setPixmap(QPixmap(u"Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButtonCliente.setScaledContents(True)
        self.labelButtonArticolo = QLabel(VistaVisualizzaPagamentoCliente)
        self.labelButtonArticolo.setObjectName(u"labelButtonArticolo")
        self.labelButtonArticolo.setGeometry(QRect(180, 120, 51, 51))
        self.labelButtonArticolo.setPixmap(QPixmap(u"Immagini/IconaFotoCliente.png"))
        self.labelButtonArticolo.setScaledContents(True)

        self.retranslateUi(VistaVisualizzaPagamentoCliente)

        QMetaObject.connectSlotsByName(VistaVisualizzaPagamentoCliente)
    # setupUi

    def retranslateUi(self, VistaVisualizzaPagamentoCliente):
        VistaVisualizzaPagamentoCliente.setWindowTitle(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Pagamento - CineMax", None))
        self.Sfondo.setText("")
        self.labelRicevutaIconCliente.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Pagamento", None))
        self.labelHomeButtonCliente.setText("")
        self.labelArticolo.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Articolo:", None))
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Data:", None))
        self.labelDataPagamento.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"14/07/2025", None))
        self.labelTipo.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Tipo:", None))
        self.labelTipoPagamento.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Punti", None))
        self.labelImporto.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Importo:", None))
        self.labelImportoPagamento.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"00,00 $", None))
        self.labelOra.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"Ora:", None))
        self.labelOraPagamento.setText(QCoreApplication.translate("VistaVisualizzaPagamentoCliente", u"00:00", None))
        self.labelIndietroButtonCliente.setText("")
        self.labelButtonArticolo.setText("")
    # retranslateUi

