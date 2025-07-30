# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaRecensioniAmministratore.ui'
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

from clickablelabel import ClickableLabel

class Ui_VistaVisualizzaRecensioniAmministratore(object):
    def setupUi(self, VistaVisualizzaRecensioniAmministratore):
        if not VistaVisualizzaRecensioniAmministratore.objectName():
            VistaVisualizzaRecensioniAmministratore.setObjectName(u"VistaVisualizzaRecensioniAmministratore")
        VistaVisualizzaRecensioniAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaRecensioniAmministratore)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 90, 791, 411))
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
        self.labelTitolo = QLabel(VistaVisualizzaRecensioniAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(30, 10, 261, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #D7320C;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaRecensioniAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(700, 10, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelBarra = QLabel(VistaVisualizzaRecensioniAmministratore)
        self.labelBarra.setObjectName(u"labelBarra")
        self.labelBarra.setGeometry(QRect(0, 0, 791, 91))
        self.labelBarra.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #961E00,\n"
"        stop: 1 #B42100\n"
"    );\n"
"    border: 1px solid #D7320C;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"}")
        self.tableViewRecensioni = QTableView(VistaVisualizzaRecensioniAmministratore)
        self.tableViewRecensioni.setObjectName(u"tableViewRecensioni")
        self.tableViewRecensioni.setGeometry(QRect(30, 120, 731, 351))
        self.tableViewRecensioni.setStyleSheet(u"QTableView {\n"
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
        self.tableViewRecensioni.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableViewRecensioni.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableViewRecensioni.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableViewRecensioni.setTabKeyNavigation(False)
        self.tableViewRecensioni.setProperty(u"showDropIndicator", False)
        self.tableViewRecensioni.setDragDropOverwriteMode(False)
        self.tableViewRecensioni.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableViewRecensioni.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableViewRecensioni.setShowGrid(False)
        self.tableViewRecensioni.setCornerButtonEnabled(False)
        self.tableViewRecensioni.horizontalHeader().setHighlightSections(False)
        self.tableViewRecensioni.verticalHeader().setVisible(False)
        self.tableViewRecensioni.verticalHeader().setMinimumSectionSize(25)
        self.tableViewRecensioni.verticalHeader().setDefaultSectionSize(25)
        self.tableViewRecensioni.verticalHeader().setHighlightSections(False)
        self.Sfondo.raise_()
        self.labelBarra.raise_()
        self.labelTitolo.raise_()
        self.labelIndietroButton.raise_()
        self.tableViewRecensioni.raise_()

        self.retranslateUi(VistaVisualizzaRecensioniAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaRecensioniAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaRecensioniAmministratore):
        VistaVisualizzaRecensioniAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaRecensioniAmministratore", u"Recensioni - CineMax", None))
        self.Sfondo.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaRecensioniAmministratore", u"Recensioni", None))
        self.labelIndietroButton.setText("")
        self.labelBarra.setText("")
    # retranslateUi

