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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHeaderView,
    QLabel, QSizePolicy, QTableView, QWidget)

from Viste.clickablelabel import ClickableLabel

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
"        stop: 0 #210A00,\n"
"        stop: 1 #7D2100\n"
"    );\n"
"}")
        self.labelProfilo = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelProfilo.setObjectName(u"labelProfilo")
        self.labelProfilo.setGeometry(QRect(30, 30, 121, 121))
        self.labelProfilo.setPixmap(QPixmap(u"Viste/Immagini/ProfiloButtonAmministratore.png"))
        self.labelProfilo.setScaledContents(True)
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
"    color: #D7320C;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelHomeButton = ClickableLabel(VistaVisualizzaClienteAmministratore)
        self.labelHomeButton.setObjectName(u"labelHomeButton")
        self.labelHomeButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButton.setPixmap(QPixmap(u"Viste/Immagini/HomeButtonAmministratore.png"))
        self.labelHomeButton.setScaledContents(True)
        self.labelCognome = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelNomeCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelNomeCliente.setObjectName(u"labelNomeCliente")
        self.labelNomeCliente.setGeometry(QRect(180, 130, 131, 20))
        self.labelNomeCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelCognomeCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelCognomeCliente.setObjectName(u"labelCognomeCliente")
        self.labelCognomeCliente.setGeometry(QRect(330, 130, 171, 20))
        self.labelCognomeCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelCodiceFiscale = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelCodiceFiscale.setObjectName(u"labelCodiceFiscale")
        self.labelCodiceFiscale.setGeometry(QRect(30, 180, 111, 20))
        self.labelCodiceFiscale.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCodiceFiscale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCodiceFiscaleCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelCodiceFiscaleCliente.setObjectName(u"labelCodiceFiscaleCliente")
        self.labelCodiceFiscaleCliente.setGeometry(QRect(30, 210, 131, 20))
        self.labelCodiceFiscaleCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelEmail = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(30, 250, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmailCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelEmailCliente.setObjectName(u"labelEmailCliente")
        self.labelEmailCliente.setGeometry(QRect(30, 280, 191, 20))
        self.labelEmailCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelTelefono = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(30, 320, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefonoCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelTelefonoCliente.setObjectName(u"labelTelefonoCliente")
        self.labelTelefonoCliente.setGeometry(QRect(30, 350, 101, 20))
        self.labelTelefonoCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelPunti = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelPunti.setObjectName(u"labelPunti")
        self.labelPunti.setGeometry(QRect(30, 400, 81, 20))
        self.labelPunti.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPuntiCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelPuntiCliente.setObjectName(u"labelPuntiCliente")
        self.labelPuntiCliente.setGeometry(QRect(30, 430, 81, 20))
        self.labelPuntiCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaClienteAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelPagamenti = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelPagamenti.setObjectName(u"labelPagamenti")
        self.labelPagamenti.setGeometry(QRect(260, 180, 111, 20))
        self.labelPagamenti.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPagamenti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelRecensioni = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelRecensioni.setObjectName(u"labelRecensioni")
        self.labelRecensioni.setGeometry(QRect(260, 320, 111, 20))
        self.labelRecensioni.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelRecensioni.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataNascita = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelDataNascita.setObjectName(u"labelDataNascita")
        self.labelDataNascita.setGeometry(QRect(520, 100, 111, 20))
        self.labelDataNascita.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelDataNascita.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataNascitaCliente = QLabel(VistaVisualizzaClienteAmministratore)
        self.labelDataNascitaCliente.setObjectName(u"labelDataNascitaCliente")
        self.labelDataNascitaCliente.setGeometry(QRect(520, 130, 101, 20))
        self.labelDataNascitaCliente.setStyleSheet(u"QLabel {\n"
"    color: #962D00;\n"
"}")
        self.tableViewPagamentiCliente = QTableView(VistaVisualizzaClienteAmministratore)
        self.tableViewPagamentiCliente.setObjectName(u"tableViewPagamentiCliente")
        self.tableViewPagamentiCliente.setGeometry(QRect(260, 210, 501, 101))
        self.tableViewPagamentiCliente.setStyleSheet(u"QTableView {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"	font-size: 11px;\n"
"}\n"
"\n"
"QTableView:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #5A1A00;\n"
"    color: #C83C00;\n"
"    border: 1px solid #3B0E00;\n"
"	border-left: none;\n"
"    border-right: none;\n"
"	text-align: left;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"	border: 1px solid #190700;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"	border-bottom: none;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #C83200;\n"
"    color: #FF3C00;\n"
"}\n"
"\n"
"QTableView QScrollBar:vertical {\n"
"	background: #B43700;\n"
"	border: 2px solid #190700;\n"
"    border-radius: 4px;\n"
"    width: 21px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:vertical {\n"
"	background: #962D00;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTable"
                        "View QScrollBar::handle:vertical:hover {\n"
"    background: #C83200;\n"
"}\n"
"\n"
"QTableView QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"    border: none;\n"
"}")
        self.tableViewPagamentiCliente.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableViewPagamentiCliente.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableViewPagamentiCliente.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableViewPagamentiCliente.setTabKeyNavigation(False)
        self.tableViewPagamentiCliente.setProperty(u"showDropIndicator", False)
        self.tableViewPagamentiCliente.setDragDropOverwriteMode(False)
        self.tableViewPagamentiCliente.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableViewPagamentiCliente.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableViewPagamentiCliente.setShowGrid(False)
        self.tableViewPagamentiCliente.setCornerButtonEnabled(False)
        self.tableViewPagamentiCliente.horizontalHeader().setHighlightSections(False)
        self.tableViewPagamentiCliente.verticalHeader().setVisible(False)
        self.tableViewPagamentiCliente.verticalHeader().setMinimumSectionSize(25)
        self.tableViewPagamentiCliente.verticalHeader().setDefaultSectionSize(25)
        self.tableViewPagamentiCliente.verticalHeader().setHighlightSections(False)
        self.tableViewRecensioniCliente = QTableView(VistaVisualizzaClienteAmministratore)
        self.tableViewRecensioniCliente.setObjectName(u"tableViewRecensioniCliente")
        self.tableViewRecensioniCliente.setGeometry(QRect(260, 350, 501, 111))
        self.tableViewRecensioniCliente.setStyleSheet(u"QTableView {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"	font-size: 11px;\n"
"}\n"
"\n"
"QTableView:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #5A1A00;\n"
"    color: #C83C00;\n"
"    border: 1px solid #3B0E00;\n"
"	border-left: none;\n"
"    border-right: none;\n"
"	text-align: left;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"	border: 1px solid #190700;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"	border-bottom: none;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #C83200;\n"
"    color: #FF3C00;\n"
"}\n"
"\n"
"QTableView QScrollBar:vertical {\n"
"	background: #B43700;\n"
"	border: 2px solid #190700;\n"
"    border-radius: 4px;\n"
"    width: 21px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:vertical {\n"
"	background: #962D00;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTable"
                        "View QScrollBar::handle:vertical:hover {\n"
"    background: #C83200;\n"
"}\n"
"\n"
"QTableView QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"    border: none;\n"
"}")
        self.tableViewRecensioniCliente.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableViewRecensioniCliente.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableViewRecensioniCliente.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableViewRecensioniCliente.setTabKeyNavigation(False)
        self.tableViewRecensioniCliente.setProperty(u"showDropIndicator", False)
        self.tableViewRecensioniCliente.setDragDropOverwriteMode(False)
        self.tableViewRecensioniCliente.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableViewRecensioniCliente.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableViewRecensioniCliente.setShowGrid(False)
        self.tableViewRecensioniCliente.setCornerButtonEnabled(False)
        self.tableViewRecensioniCliente.horizontalHeader().setHighlightSections(False)
        self.tableViewRecensioniCliente.verticalHeader().setVisible(False)
        self.tableViewRecensioniCliente.verticalHeader().setMinimumSectionSize(25)
        self.tableViewRecensioniCliente.verticalHeader().setDefaultSectionSize(25)
        self.tableViewRecensioniCliente.verticalHeader().setHighlightSections(False)

        self.retranslateUi(VistaVisualizzaClienteAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaClienteAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaClienteAmministratore):
        VistaVisualizzaClienteAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Cliente - CineMax", None))
        self.Sfondo.setText("")
        self.labelProfilo.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Profilo Cliente", None))
        self.labelHomeButton.setText("")
        self.labelCognome.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Cognome:", None))
        self.labelNomeCliente.setText("")
        self.labelCognomeCliente.setText("")
        self.labelCodiceFiscale.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Codice Fiscale:", None))
        self.labelCodiceFiscaleCliente.setText("")
        self.labelEmail.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Email:", None))
        self.labelEmailCliente.setText("")
        self.labelTelefono.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Telefono:", None))
        self.labelTelefonoCliente.setText("")
        self.labelPunti.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Punti:", None))
        self.labelPuntiCliente.setText("")
        self.labelIndietroButton.setText("")
        self.labelPagamenti.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Pagamenti:", None))
        self.labelRecensioni.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Recensioni:", None))
        self.labelDataNascita.setText(QCoreApplication.translate("VistaVisualizzaClienteAmministratore", u"Data di Nascita:", None))
        self.labelDataNascitaCliente.setText("")
    # retranslateUi

