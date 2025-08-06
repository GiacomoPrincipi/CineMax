# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaBigliettoAmministratore.ui'
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

class Ui_VistaVisualizzaBigliettoAmministratore(object):
    def setupUi(self, VistaVisualizzaBigliettoAmministratore):
        if not VistaVisualizzaBigliettoAmministratore.objectName():
            VistaVisualizzaBigliettoAmministratore.setObjectName(u"VistaVisualizzaBigliettoAmministratore")
        VistaVisualizzaBigliettoAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaBigliettoAmministratore)
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
        self.labelIconaFoto = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelIconaFoto.setObjectName(u"labelIconaFoto")
        self.labelIconaFoto.setGeometry(QRect(30, 30, 131, 131))
        self.labelIconaFoto.setPixmap(QPixmap(u"Viste/Immagini/IconaFotoAmministratore.png"))
        self.labelIconaFoto.setScaledContents(True)
        self.labelTitolo = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 100, 63, 20))
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitoloPrincipale = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelTitoloPrincipale.setObjectName(u"labelTitoloPrincipale")
        self.labelTitoloPrincipale.setGeometry(QRect(180, 30, 291, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitoloPrincipale.setFont(font1)
        self.labelTitoloPrincipale.setStyleSheet(u"QLabel {\n"
"    color: #D7320C;\n"
"}")
        self.labelTitoloPrincipale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelHomeButton = ClickableLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelHomeButton.setObjectName(u"labelHomeButton")
        self.labelHomeButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButton.setPixmap(QPixmap(u"Viste/Immagini/HomeButtonAmministratore.png"))
        self.labelHomeButton.setScaledContents(True)
        self.labelPostoBiglietto = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelPostoBiglietto.setObjectName(u"labelPostoBiglietto")
        self.labelPostoBiglietto.setGeometry(QRect(180, 130, 51, 20))
        self.labelPostoBiglietto.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelCliente = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelCliente.setObjectName(u"labelCliente")
        self.labelCliente.setGeometry(QRect(310, 100, 61, 20))
        self.labelCliente.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCliente.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelClienteBiglietto = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelClienteBiglietto.setObjectName(u"labelClienteBiglietto")
        self.labelClienteBiglietto.setGeometry(QRect(310, 130, 121, 20))
        self.labelClienteBiglietto.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelId = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelId.setObjectName(u"labelId")
        self.labelId.setGeometry(QRect(470, 100, 101, 20))
        self.labelId.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelId.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDisponibile = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelDisponibile.setObjectName(u"labelDisponibile")
        self.labelDisponibile.setGeometry(QRect(30, 260, 101, 20))
        self.labelDisponibile.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelDisponibile.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDisponibileBiglietto = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelDisponibileBiglietto.setObjectName(u"labelDisponibileBiglietto")
        self.labelDisponibileBiglietto.setGeometry(QRect(30, 290, 101, 20))
        self.labelDisponibileBiglietto.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelTipo = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelTipo.setObjectName(u"labelTipo")
        self.labelTipo.setGeometry(QRect(30, 190, 61, 20))
        self.labelTipo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTipo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTipoBiglietto = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelTipoBiglietto.setObjectName(u"labelTipoBiglietto")
        self.labelTipoBiglietto.setGeometry(QRect(30, 220, 131, 20))
        self.labelTipoBiglietto.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIdBiglietto = QLabel(VistaVisualizzaBigliettoAmministratore)
        self.labelIdBiglietto.setObjectName(u"labelIdBiglietto")
        self.labelIdBiglietto.setGeometry(QRect(470, 130, 111, 20))
        self.labelIdBiglietto.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")

        self.retranslateUi(VistaVisualizzaBigliettoAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaBigliettoAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaBigliettoAmministratore):
        VistaVisualizzaBigliettoAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaBigliettoAmministratore", u"Biglietto - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFoto.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaBigliettoAmministratore", u"Posto:", None))
        self.labelTitoloPrincipale.setText(QCoreApplication.translate("VistaVisualizzaBigliettoAmministratore", u"Biglietto", None))
        self.labelHomeButton.setText("")
        self.labelPostoBiglietto.setText("")
        self.labelCliente.setText(QCoreApplication.translate("VistaVisualizzaBigliettoAmministratore", u"Cliente:", None))
        self.labelClienteBiglietto.setText("")
        self.labelIndietroButton.setText("")
        self.labelId.setText(QCoreApplication.translate("VistaVisualizzaBigliettoAmministratore", u"Identificativo:", None))
        self.labelDisponibile.setText(QCoreApplication.translate("VistaVisualizzaBigliettoAmministratore", u"Disponibilit\u00e0:", None))
        self.labelDisponibileBiglietto.setText("")
        self.labelTipo.setText(QCoreApplication.translate("VistaVisualizzaBigliettoAmministratore", u"Tipo:", None))
        self.labelTipoBiglietto.setText("")
        self.labelIdBiglietto.setText("")
    # retranslateUi

