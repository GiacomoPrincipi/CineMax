# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaClienteAmministratore.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QScrollBar,
    QSizePolicy, QWidget)

class Ui_VistaVisualizzaClienteAmministratore(object):
    def setupUi(self, VistaVisualizzaClienteAmministratore):
        if not VistaVisualizzaClienteAmministratore.objectName():
            VistaVisualizzaClienteAmministratore.setObjectName(u"VistaVisualizzaClienteAmministratore")
        VistaVisualizzaClienteAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaClienteAmministratore)
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
        self.labelProfiloAmministratore = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelProfiloAmministratore.setObjectName(u"labelProfiloAmministratore")
        self.labelProfiloAmministratore.setGeometry(QRect(40, 30, 121, 121))
        self.labelProfiloAmministratore.setPixmap(QPixmap(u"Immagini/profiloButtonAmministratore.png"))
        self.labelProfiloAmministratore.setScaledContents(True)
        self.labelNome = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaVisualizzaClienteAmministratore)
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
        self.labelHomeButtonAmministratore = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelHomeButtonAmministratore.setObjectName(u"labelHomeButtonAmministratore")
        self.labelHomeButtonAmministratore.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButtonAmministratore.setPixmap(QPixmap(u"Immagini/HomeButtonAmministratore.png"))
        self.labelHomeButtonAmministratore.setScaledContents(True)
        self.labelCognome = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelNomeCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelNomeCliente.setObjectName(u"labelNomeCliente")
        self.labelNomeCliente.setGeometry(QRect(180, 120, 131, 20))
        self.labelNomeCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelCognomeCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelCognomeCliente.setObjectName(u"labelCognomeCliente")
        self.labelCognomeCliente.setGeometry(QRect(330, 120, 131, 20))
        self.labelCognomeCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelCodiceFiscale = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelCodiceFiscale.setObjectName(u"labelCodiceFiscale")
        self.labelCodiceFiscale.setGeometry(QRect(40, 180, 111, 20))
        self.labelCodiceFiscale.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCodiceFiscale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCodiceFiscasleAmministratore = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelCodiceFiscasleAmministratore.setObjectName(u"labelCodiceFiscasleAmministratore")
        self.labelCodiceFiscasleAmministratore.setGeometry(QRect(40, 200, 131, 20))
        self.labelCodiceFiscasleAmministratore.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelEmail = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(40, 240, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmailCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelEmailCliente.setObjectName(u"labelEmailCliente")
        self.labelEmailCliente.setGeometry(QRect(40, 260, 251, 20))
        self.labelEmailCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelTelefono = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(40, 300, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefonoCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelTelefonoCliente.setObjectName(u"labelTelefonoCliente")
        self.labelTelefonoCliente.setGeometry(QRect(40, 320, 101, 20))
        self.labelTelefonoCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelPunti = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelPunti.setObjectName(u"labelPunti")
        self.labelPunti.setGeometry(QRect(40, 360, 81, 20))
        self.labelPunti.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPuntiCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelPuntiCliente.setObjectName(u"labelPuntiCliente")
        self.labelPuntiCliente.setGeometry(QRect(30, 380, 101, 20))
        self.labelPuntiCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIndietroButtonAmministratore = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelIndietroButtonAmministratore.setObjectName(u"labelIndietroButtonAmministratore")
        self.labelIndietroButtonAmministratore.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButtonAmministratore.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButtonAmministratore.setScaledContents(True)
        self.listViewPagamenti = QListView(VistaVisualizzaClienteAmministratore)
        self.listViewPagamenti.setObjectName(u"listViewPagamenti")
        self.listViewPagamenti.setGeometry(QRect(260, 200, 461, 111))
        self.listViewPagamenti.setStyleSheet(u"QListView {\n"
"        background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"        font-size: 11px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background-color: #C83200;\n"
"    color: #FF3C00;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.listViewRecensioni = QListView(VistaVisualizzaClienteAmministratore)
        self.listViewRecensioni.setObjectName(u"listViewRecensioni")
        self.listViewRecensioni.setGeometry(QRect(260, 350, 461, 111))
        self.listViewRecensioni.setStyleSheet(u"QListView {\n"
"        background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"        font-size: 11px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background-color: #C83200;\n"
"    color: #FF3C00;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.labelPagamenti = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelPagamenti.setObjectName(u"labelPagamenti")
        self.labelPagamenti.setGeometry(QRect(260, 180, 111, 20))
        self.labelPagamenti.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPagamenti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelRecensioni = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelRecensioni.setObjectName(u"labelRecensioni")
        self.labelRecensioni.setGeometry(QRect(260, 330, 111, 20))
        self.labelRecensioni.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelRecensioni.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.verticalScrollBarPagamenti = QScrollBar(VistaVisualizzaClienteAmministratore)
        self.verticalScrollBarPagamenti.setObjectName(u"verticalScrollBarPagamenti")
        self.verticalScrollBarPagamenti.setGeometry(QRect(700, 200, 21, 111))
        self.verticalScrollBarPagamenti.setStyleSheet(u"QScrollBar:vertical {\n"
"        background: #B43700;\n"
"        border: 2px solid #190700;\n"
"    border-radius: 4px;\n"
"        width: 15px;\n"
"        margin: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"        background: #962D00;\n"
"        min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"        background: #C83200;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        background: none;\n"
"        border: none;\n"
"            }")
        self.verticalScrollBarPagamenti.setOrientation(Qt.Orientation.Vertical)
        self.verticalScrollBarRecensioni = QScrollBar(VistaVisualizzaClienteAmministratore)
        self.verticalScrollBarRecensioni.setObjectName(u"verticalScrollBarRecensioni")
        self.verticalScrollBarRecensioni.setGeometry(QRect(700, 350, 21, 111))
        self.verticalScrollBarRecensioni.setStyleSheet(u"QScrollBar:vertical {\n"
"        background: #B43700;\n"
"        border: 2px solid #190700;\n"
"    border-radius: 4px;\n"
"        width: 15px;\n"
"        margin: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"        background: #962D00;\n"
"        min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"        background: #C83200;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        background: none;\n"
"        border: none;\n"
"            }")
        self.verticalScrollBarRecensioni.setOrientation(Qt.Orientation.Vertical)

        self.retranslateUi(VistaVisualizzaClienteAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaClienteAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaClienteAmministratore):
        VistaVisualizzaClienteAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Cliente - CineMax", None))
        self.Sfondo.setText("")
        self.labelProfiloAmministratore.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Profilo Cliente", None))
        self.labelHomeButtonAmministratore.setText("")
        self.labelCognome.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Cognome:", None))
        self.labelNomeCliente.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Cliente", None))
        self.labelCognomeCliente.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Cliente", None))
        self.labelCodiceFiscale.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Codice Fiscale:", None))
        self.labelCodiceFiscasleAmministratore.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"00000000000000", None))
        self.labelEmail.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Email:", None))
        self.labelEmailCliente.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Cliente@gmail.com", None))
        self.labelTelefono.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Telefono:", None))
        self.labelTelefonoCliente.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"3333333333", None))
        self.labelPunti.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Punti:", None))
        self.labelPuntiCliente.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"000", None))
        self.labelIndietroButtonAmministratore.setText("")
        self.labelPagamenti.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Pagamenti:", None))
        self.labelRecensioni.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Recensioni:", None))
    # retranslateUi

