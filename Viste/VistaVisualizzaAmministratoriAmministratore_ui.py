# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaAmministratoriAmministratore.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QPushButton,
    QScrollBar, QSizePolicy, QWidget)

class Ui_VistaVisualizzaAmministratoriAmministratore(object):
    def setupUi(self, VistaVisualizzaAmministratoriAmministratore):
        if not VistaVisualizzaAmministratoriAmministratore.objectName():
            VistaVisualizzaAmministratoriAmministratore.setObjectName(u"VistaVisualizzaAmministratoriAmministratore")
        VistaVisualizzaAmministratoriAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaAmministratoriAmministratore)
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
        self.labelTitolo = QLabel(VistaVisualizzaAmministratoriAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(30, 10, 321, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #501400;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIndietroButtonAmministratore = QLabel(VistaVisualizzaAmministratoriAmministratore)
        self.labelIndietroButtonAmministratore.setObjectName(u"labelIndietroButtonAmministratore")
        self.labelIndietroButtonAmministratore.setGeometry(QRect(700, 10, 63, 61))
        self.labelIndietroButtonAmministratore.setPixmap(QPixmap(u"Immagini/IndietroButtonAmministratore.png"))
        self.labelIndietroButtonAmministratore.setScaledContents(True)
        self.listViewAmministratori = QListView(VistaVisualizzaAmministratoriAmministratore)
        self.listViewAmministratori.setObjectName(u"listViewAmministratori")
        self.listViewAmministratori.setGeometry(QRect(30, 120, 731, 351))
        self.listViewAmministratori.setStyleSheet(u"QListView {\n"
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
        self.verticalScrollBarAmministratori = QScrollBar(VistaVisualizzaAmministratoriAmministratore)
        self.verticalScrollBarAmministratori.setObjectName(u"verticalScrollBarAmministratori")
        self.verticalScrollBarAmministratori.setGeometry(QRect(740, 120, 21, 351))
        self.verticalScrollBarAmministratori.setStyleSheet(u"QScrollBar:vertical {\n"
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
        self.verticalScrollBarAmministratori.setOrientation(Qt.Orientation.Vertical)
        self.labelBarra = QLabel(VistaVisualizzaAmministratoriAmministratore)
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
        self.pushButtonInserisci = QPushButton(VistaVisualizzaAmministratoriAmministratore)
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
        self.labelBarra.raise_()
        self.Sfondo.raise_()
        self.labelTitolo.raise_()
        self.labelIndietroButtonAmministratore.raise_()
        self.listViewAmministratori.raise_()
        self.verticalScrollBarAmministratori.raise_()
        self.pushButtonInserisci.raise_()

        self.retranslateUi(VistaVisualizzaAmministratoriAmministratore)

        QMetaObject.connectSlotsByName(VistaVisualizzaAmministratoriAmministratore)
    # setupUi

    def retranslateUi(self, VistaVisualizzaAmministratoriAmministratore):
        VistaVisualizzaAmministratoriAmministratore.setWindowTitle(QCoreApplication.translate("VistaVisualizzaAmministratoriAmministratore", u"Amministratori - CineMax", None))
        self.Sfondo.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaAmministratoriAmministratore", u"Amministratori", None))
        self.labelIndietroButtonAmministratore.setText("")
        self.labelBarra.setText("")
        self.pushButtonInserisci.setText(QCoreApplication.translate("VistaVisualizzaAmministratoriAmministratore", u"Inserisci", None))
    # retranslateUi

