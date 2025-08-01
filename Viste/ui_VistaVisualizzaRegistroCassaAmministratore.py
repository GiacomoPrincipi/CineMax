# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaRegistroCassaAmministratore.ui'
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

class Ui_VistaVisualizzaRegistroCassaAmministratore(object):
    def setupUi(self, VistaVisualizzaRegistroCassaAmministratore):
        if not VistaVisualizzaRegistroCassaAmministratore.objectName():
            VistaVisualizzaRegistroCassaAmministratore.setObjectName(u"VistaVisualizzaRegistroCassaAmministratore")
        VistaVisualizzaRegistroCassaAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaRegistroCassaAmministratore)
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
        self.labelTitolo = QLabel(VistaVisualizzaRegistroCassaAmministratore)
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
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaRegistroCassaAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(700, 10, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelBarra = QLabel(VistaVisualizzaRegistroCassaAmministratore)
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
        self.tableViewPagamenti = QTableView(VistaVisualizzaRegistroCassaAmministratore)
        self.tableViewPagamenti.setObjectName(u"tableViewPagamenti")
        self.tableViewPagamenti.setGeometry(QRect(30, 120, 731, 351))
        self.tableViewPagamenti.setStyleSheet(u"QTableView {\n"
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
        self.tableViewPagamenti.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableViewPagamenti.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableViewPagamenti.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableViewPagamenti.setTabKeyNavigation(False)
        self.tableViewPagamenti.setProperty(u"showDropIndicator", False)
        self.tableViewPagamenti.setDragDropOverwriteMode(False)
        self.tableViewPagamenti.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableViewPagamenti.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableViewPagamenti.setShowGrid(False)
        self.tableViewPagamenti.setCornerButtonEnabled(False)
        self.tableViewPagamenti.horizontalHeader().setHighlightSections(False)
        self.tableViewPagamenti.verticalHeader().setVisible(False)
        self.tableViewPagamenti.verticalHeader().setMinimumSectionSize(25)
        self.tableViewPagamenti.verticalHeader().setDefaultSectionSize(25)
        self.tableViewPagamenti.verticalHeader().setHighlightSections(False)
        self.Sfondo.raise_()
        self.labelBarra.raise_()
        self.labelTitolo.raise_()
        self.labelIndietroButton.raise_()
        self.tableViewPagamenti.raise_()

        self.retranslateUi(VistaVisualizzaRegistroCassaAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaRegistroCassaAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaRegistroCassaAmministratore):
        VistaVisualizzaRegistroCassaAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaRegistroCassaAmministratore", u"Registro Cassa - CineMax", None))
        self.Sfondo.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaRegistroCassaAmministratore", u"RegistroCassa", None))
        self.labelIndietroButton.setText("")
        self.labelBarra.setText("")
    # retranslateUi

