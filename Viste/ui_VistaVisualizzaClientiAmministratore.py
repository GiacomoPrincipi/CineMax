# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaClientiAmministratore.ui'
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

class Ui_VistaVisualizzaClientiAmministratore(object):
    def setupUi(self, VistaVisualizzaClientiAmministratore):
        if not VistaVisualizzaClientiAmministratore.objectName():
            VistaVisualizzaClientiAmministratore.setObjectName(u"VistaVisualizzaClientiAmministratore")
        VistaVisualizzaClientiAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaClientiAmministratore)
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
        self.labelTitolo = QLabel(VistaVisualizzaClientiAmministratore)
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
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaClientiAmministratore)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(700, 10, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelBarra = QLabel(VistaVisualizzaClientiAmministratore)
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
        self.tableViewClienti = QTableView(VistaVisualizzaClientiAmministratore)
        self.tableViewClienti.setObjectName(u"tableViewClienti")
        self.tableViewClienti.setGeometry(QRect(30, 120, 731, 351))
        self.tableViewClienti.setStyleSheet(u"QTableView {\n"
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
        self.tableViewClienti.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableViewClienti.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableViewClienti.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableViewClienti.setTabKeyNavigation(False)
        self.tableViewClienti.setProperty(u"showDropIndicator", False)
        self.tableViewClienti.setDragDropOverwriteMode(False)
        self.tableViewClienti.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableViewClienti.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableViewClienti.setShowGrid(False)
        self.tableViewClienti.setCornerButtonEnabled(False)
        self.tableViewClienti.horizontalHeader().setHighlightSections(False)
        self.tableViewClienti.verticalHeader().setVisible(False)
        self.tableViewClienti.verticalHeader().setMinimumSectionSize(25)
        self.tableViewClienti.verticalHeader().setDefaultSectionSize(25)
        self.tableViewClienti.verticalHeader().setHighlightSections(False)
        self.labelBarra.raise_()
        self.Sfondo.raise_()
        self.labelTitolo.raise_()
        self.labelIndietroButton.raise_()
        self.tableViewClienti.raise_()

        self.retranslateUi(VistaVisualizzaClientiAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaClientiAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaClientiAmministratore):
        VistaVisualizzaClientiAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaClientiAmministratore", u"Clienti - CineMax", None))
        self.Sfondo.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaClientiAmministratore", u"Clienti", None))
        self.labelIndietroButton.setText("")
        self.labelBarra.setText("")
    # retranslateUi

