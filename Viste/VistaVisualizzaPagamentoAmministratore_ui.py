# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaPagamentoAmministratore.ui'
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

class Ui_VistaVisualizzaPagamentoAmministratore(object):
    def setupUi(self, VistaVisualizzaPagamentoAmministratore):
        if not VistaVisualizzaPagamentoAmministratore.objectName():
            VistaVisualizzaPagamentoAmministratore.setObjectName(u"VistaVisualizzaPagamentoAmministratore")
        VistaVisualizzaPagamentoAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaPagamentoAmministratore)
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
        self.labelRicevutaIconAmministratore = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelRicevutaIconAmministratore.setObjectName(u"labelRicevutaIconAmministratore")
        self.labelRicevutaIconAmministratore.setGeometry(QRect(20, 20, 151, 151))
        self.labelRicevutaIconAmministratore.setPixmap(QPixmap(u"Immagini/RicevutaIconAmministratore.png"))
        self.labelRicevutaIconAmministratore.setScaledContents(True)
        self.labelCliente = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelCliente.setObjectName(u"labelCliente")
        self.labelCliente.setGeometry(QRect(180, 100, 63, 20))
        self.labelCliente.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCliente.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaVisualizzaPagamentoAmministratore)
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
        self.labelHomeButtonAmministratore = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelHomeButtonAmministratore.setObjectName(u"labelHomeButtonAmministratore")
        self.labelHomeButtonAmministratore.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButtonAmministratore.setPixmap(QPixmap(u"Immagini/HomeButtonAmministratore.png"))
        self.labelHomeButtonAmministratore.setScaledContents(True)
        self.labelArticolo = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelArticolo.setObjectName(u"labelArticolo")
        self.labelArticolo.setGeometry(QRect(330, 100, 81, 20))
        self.labelArticolo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelArticolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelData = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(40, 180, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataPagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelDataPagamento.setObjectName(u"labelDataPagamento")
        self.labelDataPagamento.setGeometry(QRect(40, 200, 91, 20))
        self.labelDataPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelTipo = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelTipo.setObjectName(u"labelTipo")
        self.labelTipo.setGeometry(QRect(40, 240, 81, 20))
        self.labelTipo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTipo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTipoPagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelTipoPagamento.setObjectName(u"labelTipoPagamento")
        self.labelTipoPagamento.setGeometry(QRect(40, 260, 111, 20))
        self.labelTipoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelImporto = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelImporto.setObjectName(u"labelImporto")
        self.labelImporto.setGeometry(QRect(40, 300, 81, 20))
        self.labelImporto.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelImporto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelImportoPagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelImportoPagamento.setObjectName(u"labelImportoPagamento")
        self.labelImportoPagamento.setGeometry(QRect(40, 320, 91, 20))
        self.labelImportoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelOra = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelOra.setObjectName(u"labelOra")
        self.labelOra.setGeometry(QRect(180, 180, 81, 20))
        self.labelOra.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelOra.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOraPagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelOraPagamento.setObjectName(u"labelOraPagamento")
        self.labelOraPagamento.setGeometry(QRect(180, 200, 51, 20))
        self.labelOraPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIndietroButtonAmministratore = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelIndietroButtonAmministratore.setObjectName(u"labelIndietroButtonAmministratore")
        self.labelIndietroButtonAmministratore.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButtonAmministratore.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButtonAmministratore.setScaledContents(True)
        self.labelButtonCliente = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelButtonCliente.setObjectName(u"labelButtonCliente")
        self.labelButtonCliente.setGeometry(QRect(180, 120, 51, 51))
        self.labelButtonCliente.setPixmap(QPixmap(u"Immagini/profiloButtonAmministratore.png"))
        self.labelButtonCliente.setScaledContents(True)
        self.labelButtonArticolo = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelButtonArticolo.setObjectName(u"labelButtonArticolo")
        self.labelButtonArticolo.setGeometry(QRect(330, 120, 51, 51))
        self.labelButtonArticolo.setPixmap(QPixmap(u"Immagini/IconaFotoAmministratore.png"))
        self.labelButtonArticolo.setScaledContents(True)

        self.retranslateUi(VistaVisualizzaPagamentoAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaPagamentoAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaPagamentoAmministratore):
        VistaVisualizzaPagamentoAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Pagamento - CineMax", None))
        self.Sfondo.setText("")
        self.labelRicevutaIconAmministratore.setText("")
        self.labelCliente.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Cliente:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Pagamento", None))
        self.labelHomeButtonAmministratore.setText("")
        self.labelArticolo.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Articolo:", None))
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Data:", None))
        self.labelDataPagamento.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"14/07/2025", None))
        self.labelTipo.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Tipo:", None))
        self.labelTipoPagamento.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Punti", None))
        self.labelImporto.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Importo:", None))
        self.labelImportoPagamento.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"00,00 $", None))
        self.labelOra.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Ora:", None))
        self.labelOraPagamento.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"00:00", None))
        self.labelIndietroButtonAmministratore.setText("")
        self.labelButtonCliente.setText("")
        self.labelButtonArticolo.setText("")
    # retranslateUi

