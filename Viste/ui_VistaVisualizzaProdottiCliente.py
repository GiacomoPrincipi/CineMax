# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaProdottiCliente.ui'
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

class Ui_VistaVisualizzaProdottiCliente(object):
    def setupUi(self, VistaVisualizzaProdottiCliente):
        if not VistaVisualizzaProdottiCliente.objectName():
            VistaVisualizzaProdottiCliente.setObjectName(u"VistaVisualizzaProdottiCliente")
        VistaVisualizzaProdottiCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaProdottiCliente)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 90, 791, 411))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"		stop: 0 #211400,\n"
"        stop: 1 #7D4B00\n"
"    );\n"
"}")
        self.labelTitolo = QLabel(VistaVisualizzaProdottiCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(30, 10, 201, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #D7AA0C;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaProdottiCliente)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(700, 10, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelBarra = QLabel(VistaVisualizzaProdottiCliente)
        self.labelBarra.setObjectName(u"labelBarra")
        self.labelBarra.setGeometry(QRect(0, 0, 791, 91))
        self.labelBarra.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #965A00,\n"
"        stop: 1 #B46E00\n"
"    );\n"
"    border: 1px solid #AF8C0A;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"}")
        self.tableViewProdotti = QTableView(VistaVisualizzaProdottiCliente)
        self.tableViewProdotti.setObjectName(u"tableViewProdotti")
        self.tableViewProdotti.setGeometry(QRect(30, 120, 731, 351))
        self.tableViewProdotti.setStyleSheet(u"QTableView {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QTableView:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #5A3400;\n"
"    color: #C87800;\n"
"    border: 1px solid #3B1C00;\n"
"	border-left: none;\n"
"    border-right: none;\n"
"	text-align: left;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"	border: 1px solid #190E00;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"	border-bottom: none;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #C86400;\n"
"    color: #FF7800;\n"
"}\n"
"\n"
"QTableView QScrollBar:vertical {\n"
"        background: #B46E00;\n"
"        border: 2px solid #190E00;\n"
"        border-radius: 4px;\n"
"        width: 21px;\n"
"        margin: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:vertical {\n"
"	background: #965A00;\n"
"    min-height: 20px;\n"
"    border-radiu"
                        "s: 4px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:vertical:hover {\n"
"     background: #C86400;\n"
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
        self.Sfondo.raise_()
        self.labelBarra.raise_()
        self.labelTitolo.raise_()
        self.labelIndietroButton.raise_()
        self.tableViewProdotti.raise_()

        self.retranslateUi(VistaVisualizzaProdottiCliente)

        QMetaObject.connectSlotsByName(VistaVisualizzaProdottiCliente)
    # setupUi

    def retranslateUi(self, VistaVisualizzaProdottiCliente):
        VistaVisualizzaProdottiCliente.setWindowTitle(QCoreApplication.translate("VistaVisualizzaProdottiCliente", u"Prodotti - CineMax", None))
        self.Sfondo.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaProdottiCliente", u"Prodotti", None))
        self.labelIndietroButton.setText("")
        self.labelBarra.setText("")
    # retranslateUi

