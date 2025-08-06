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

from Viste.clickablelabel import ClickableLabel

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
"        stop: 0 #210A00,\n"
"        stop: 1 #7D2100\n"
"    );\n"
"}")
        self.labelRicevutaIcon = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelRicevutaIcon.setObjectName(u"labelRicevutaIcon")
        self.labelRicevutaIcon.setGeometry(QRect(10, 10, 171, 171))
        self.labelRicevutaIcon.setPixmap(QPixmap(u"Viste/Immagini/RicevutaIconAmministratore.png"))
        self.labelRicevutaIcon.setScaledContents(True)
        self.labelCliente = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelCliente.setObjectName(u"labelCliente")
        self.labelCliente.setGeometry(QRect(320, 100, 161, 20))
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
"    color: #D7320C;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelHomeButton = ClickableLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelHomeButton.setObjectName(u"labelHomeButton")
        self.labelHomeButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButton.setPixmap(QPixmap(u"Viste/Immagini/HomeButtonAmministratore.png"))
        self.labelHomeButton.setScaledContents(True)
        self.labelArticolo = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelArticolo.setObjectName(u"labelArticolo")
        self.labelArticolo.setGeometry(QRect(520, 100, 171, 20))
        self.labelArticolo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelArticolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelData = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(30, 190, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataPagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelDataPagamento.setObjectName(u"labelDataPagamento")
        self.labelDataPagamento.setGeometry(QRect(30, 220, 91, 20))
        self.labelDataPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelTipo = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelTipo.setObjectName(u"labelTipo")
        self.labelTipo.setGeometry(QRect(30, 260, 81, 20))
        self.labelTipo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTipo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTipoPagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelTipoPagamento.setObjectName(u"labelTipoPagamento")
        self.labelTipoPagamento.setGeometry(QRect(30, 290, 111, 20))
        self.labelTipoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelImporto = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelImporto.setObjectName(u"labelImporto")
        self.labelImporto.setGeometry(QRect(30, 330, 81, 20))
        self.labelImporto.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelImporto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelImportoPagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelImportoPagamento.setObjectName(u"labelImportoPagamento")
        self.labelImportoPagamento.setGeometry(QRect(30, 360, 91, 20))
        self.labelImportoPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelOra = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelOra.setObjectName(u"labelOra")
        self.labelOra.setGeometry(QRect(180, 190, 81, 20))
        self.labelOra.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelOra.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOraPagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelOraPagamento.setObjectName(u"labelOraPagamento")
        self.labelOraPagamento.setGeometry(QRect(180, 220, 51, 20))
        self.labelOraPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelCodiceFiscalePagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelCodiceFiscalePagamento.setObjectName(u"labelCodiceFiscalePagamento")
        self.labelCodiceFiscalePagamento.setGeometry(QRect(320, 130, 151, 20))
        self.labelCodiceFiscalePagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIdArticoloPagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelIdArticoloPagamento.setObjectName(u"labelIdArticoloPagamento")
        self.labelIdArticoloPagamento.setGeometry(QRect(520, 130, 181, 20))
        self.labelIdArticoloPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelImportoPunti = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelImportoPunti.setObjectName(u"labelImportoPunti")
        self.labelImportoPunti.setGeometry(QRect(180, 330, 131, 20))
        self.labelImportoPunti.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelImportoPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelImportoPuntiPagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelImportoPuntiPagamento.setObjectName(u"labelImportoPuntiPagamento")
        self.labelImportoPuntiPagamento.setGeometry(QRect(180, 360, 91, 20))
        self.labelImportoPuntiPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelId = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelId.setObjectName(u"labelId")
        self.labelId.setGeometry(QRect(180, 100, 161, 20))
        self.labelId.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelId.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIdPagamento = QLabel(VistaVisualizzaPagamentoAmministratore)
        self.labelIdPagamento.setObjectName(u"labelIdPagamento")
        self.labelIdPagamento.setGeometry(QRect(180, 130, 111, 20))
        self.labelIdPagamento.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")

        self.retranslateUi(VistaVisualizzaPagamentoAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaPagamentoAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaPagamentoAmministratore):
        VistaVisualizzaPagamentoAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Pagamento - CineMax", None))
        self.Sfondo.setText("")
        self.labelRicevutaIcon.setText("")
        self.labelCliente.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Cliente:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Pagamento", None))
        self.labelHomeButton.setText("")
        self.labelArticolo.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Articolo:", None))
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Data:", None))
        self.labelDataPagamento.setText("")
        self.labelTipo.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Tipo:", None))
        self.labelTipoPagamento.setText("")
        self.labelImporto.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Importo:", None))
        self.labelImportoPagamento.setText("")
        self.labelOra.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Ora:", None))
        self.labelOraPagamento.setText("")
        self.labelIndietroButton.setText("")
        self.labelCodiceFiscalePagamento.setText("")
        self.labelIdArticoloPagamento.setText("")
        self.labelImportoPunti.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Importo in Punti:", None))
        self.labelImportoPuntiPagamento.setText("")
        self.labelId.setText(QCoreApplication.translate("VistaVisualizzaPagamentoAmministratore", u"Identificativo:", None))
        self.labelIdPagamento.setText("")
    # retranslateUi

