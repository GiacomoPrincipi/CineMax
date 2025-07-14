# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaSpettacoliCliente.ui'
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

class Ui_VistaVisualizzaSpettacoliCliente(object):
    def setupUi(self, VistaVisualizzaSpettacoliCliente):
        if not VistaVisualizzaSpettacoliCliente.objectName():
            VistaVisualizzaSpettacoliCliente.setObjectName(u"VistaVisualizzaSpettacoliCliente")
        VistaVisualizzaSpettacoliCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaSpettacoliCliente)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 90, 791, 411))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"		stop: 0 #321E00,\n"
"        stop: 1 #643C00\n"
"    );\n"
"}")
        self.labelTitolo = QLabel(VistaVisualizzaSpettacoliCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(30, 10, 201, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #502800;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIndietroButtonCliente = QLabel(VistaVisualizzaSpettacoliCliente)
        self.labelIndietroButtonCliente.setObjectName(u"labelIndietroButtonCliente")
        self.labelIndietroButtonCliente.setGeometry(QRect(700, 10, 63, 61))
        self.labelIndietroButtonCliente.setPixmap(QPixmap(u"Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButtonCliente.setScaledContents(True)
        self.listViewSpettacoli = QListView(VistaVisualizzaSpettacoliCliente)
        self.listViewSpettacoli.setObjectName(u"listViewSpettacoli")
        self.listViewSpettacoli.setGeometry(QRect(30, 120, 731, 351))
        self.listViewSpettacoli.setStyleSheet(u"QListView {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background-color: #C86400;\n"
"    color: #FF7800;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #C86400;\n"
"}")
        self.verticalScrollBarSpettacoli = QScrollBar(VistaVisualizzaSpettacoliCliente)
        self.verticalScrollBarSpettacoli.setObjectName(u"verticalScrollBarSpettacoli")
        self.verticalScrollBarSpettacoli.setGeometry(QRect(740, 120, 21, 351))
        self.verticalScrollBarSpettacoli.setStyleSheet(u"QScrollBar:vertical {\n"
"        background: #B46E00;\n"
"        border: 2px solid #190E00;\n"
"    border-radius: 4px;\n"
"        width: 15px;\n"
"        margin: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"        background: #965A00;\n"
"        min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"        background: #C86400;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        background: none;\n"
"        border: none;\n"
"            }")
        self.verticalScrollBarSpettacoli.setOrientation(Qt.Orientation.Vertical)
        self.labelBarra = QLabel(VistaVisualizzaSpettacoliCliente)
        self.labelBarra.setObjectName(u"labelBarra")
        self.labelBarra.setGeometry(QRect(0, 0, 791, 91))
        self.labelBarra.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #965A00,\n"
"        stop: 1 #B46E00\n"
"    );\n"
"}")
        self.labelBarra.raise_()
        self.Sfondo.raise_()
        self.labelTitolo.raise_()
        self.labelIndietroButtonCliente.raise_()
        self.listViewSpettacoli.raise_()
        self.verticalScrollBarSpettacoli.raise_()

        self.retranslateUi(VistaVisualizzaSpettacoliCliente)

        QMetaObject.connectSlotsByName(VistaVisualizzaSpettacoliCliente)
    # setupUi

    def retranslateUi(self, VistaVisualizzaSpettacoliCliente):
        VistaVisualizzaSpettacoliCliente.setWindowTitle(QCoreApplication.translate("VistaVisualizzaSpettacoliCliente", u"Spettacoli - CineMax", None))
        self.Sfondo.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoliCliente", u"Spettacoli", None))
        self.labelIndietroButtonCliente.setText("")
        self.labelBarra.setText("")
    # retranslateUi

