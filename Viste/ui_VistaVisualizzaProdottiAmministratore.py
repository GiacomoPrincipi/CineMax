# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaProdottiAmministratore.ui'
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
    QLabel, QPushButton, QSizePolicy, QTableView,
    QWidget)

from clickablelabel import ClickableLabel

class Ui_VistaVisualizzaProdottiAmministratore(object):
    def setupUi(self, VistaVisualizzaProdottiAmministratore):
        if not VistaVisualizzaProdottiAmministratore.objectName():
            VistaVisualizzaProdottiAmministratore.setObjectName(u"VistaVisualizzaProdottiAmministratore")
        VistaVisualizzaProdottiAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaProdottiAmministratore)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 90, 791, 411))
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
        self.labelTitolo = QLabel(VistaVisualizzaProdottiAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(30, 10, 201, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #501400;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaProdottiAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(700, 10, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelBarra = QLabel(VistaVisualizzaProdottiAmministratore)
        self.labelBarra.setObjectName(u"labelBarra")
        self.labelBarra.setGeometry(QRect(0, 0, 791, 91))
        self.labelBarra.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #962D00,\n"
"        stop: 1 #B43700\n"
"    );\n"
"}")
        self.pushButtonInserisci = QPushButton(VistaVisualizzaProdottiAmministratore)
        self.pushButtonInserisci.setObjectName(u"pushButtonInserisci")
        self.pushButtonInserisci.setGeometry(QRect(630, 420, 91, 29))
        self.pushButtonInserisci.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.tableViewProdotti = QTableView(VistaVisualizzaProdottiAmministratore)
        self.tableViewProdotti.setObjectName(u"tableViewProdotti")
        self.tableViewProdotti.setGeometry(QRect(30, 120, 731, 351))
        self.tableViewProdotti.setStyleSheet(u"QTableView {\n"
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
        self.tableViewProdotti.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableViewProdotti.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableViewProdotti.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableViewProdotti.setTabKeyNavigation(False)
        self.tableViewProdotti.setProperty(u"showDropIndicator", False)
        self.tableViewProdotti.setDragDropOverwriteMode(False)
        self.tableViewProdotti.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableViewProdotti.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableViewProdotti.setShowGrid(False)
        self.tableViewProdotti.setCornerButtonEnabled(False)
        self.tableViewProdotti.horizontalHeader().setHighlightSections(False)
        self.tableViewProdotti.verticalHeader().setVisible(False)
        self.tableViewProdotti.verticalHeader().setMinimumSectionSize(25)
        self.tableViewProdotti.verticalHeader().setDefaultSectionSize(25)
        self.tableViewProdotti.verticalHeader().setHighlightSections(False)
        self.labelBarra.raise_()
        self.Sfondo.raise_()
        self.labelTitolo.raise_()
        self.labelIndietroButton.raise_()
        self.tableViewProdotti.raise_()
        self.pushButtonInserisci.raise_()

        self.retranslateUi(VistaVisualizzaProdottiAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaProdottiAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaProdottiAmministratore):
        VistaVisualizzaProdottiAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaProdottiAmministratore", u"Prodotti - CineMax", None))
        self.Sfondo.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaProdottiAmministratore", u"Prodotti", None))
        self.labelIndietroButton.setText("")
        self.labelBarra.setText("")
        self.pushButtonInserisci.setText(QCoreApplication.translate("VistaVisualizzaProdottiAmministratore", u"Inserisci", None))
    # retranslateUi

