# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaInserisciRecensioneCliente.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_VistaInserisciRecensioneCliente(object):
    def setupUi(self, VistaInserisciRecensioneCliente):
        if not VistaInserisciRecensioneCliente.objectName():
            VistaInserisciRecensioneCliente.setObjectName(u"VistaInserisciRecensioneCliente")
        VistaInserisciRecensioneCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaInserisciRecensioneCliente)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
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
        self.labelTitolo = QLabel(VistaInserisciRecensioneCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 391, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #D7AA0C;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTipo = QLabel(VistaInserisciRecensioneCliente)
        self.labelTipo.setObjectName(u"labelTipo")
        self.labelTipo.setGeometry(QRect(30, 190, 81, 20))
        self.labelTipo.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTipo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelProfilo = QLabel(VistaInserisciRecensioneCliente)
        self.labelProfilo.setObjectName(u"labelProfilo")
        self.labelProfilo.setGeometry(QRect(40, 40, 121, 121))
        self.labelProfilo.setPixmap(QPixmap(u"Viste/Immagini/RecensioneIconCliente.png"))
        self.labelProfilo.setScaledContents(True)
        self.labelTesto = QLabel(VistaInserisciRecensioneCliente)
        self.labelTesto.setObjectName(u"labelTesto")
        self.labelTesto.setGeometry(QRect(290, 190, 81, 20))
        self.labelTesto.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTesto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButtonConferma = QPushButton(VistaInserisciRecensioneCliente)
        self.pushButtonConferma.setObjectName(u"pushButtonConferma")
        self.pushButtonConferma.setGeometry(QRect(670, 440, 91, 29))
        self.pushButtonConferma.setStyleSheet(u"QPushButton {\n"
"    background-color: #963C00;\n"
"    color: #FF7800;\n"
"    border: 2px solid #502800;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C86400;\n"
"}\n"
"")
        self.pushButtonAnnulla = QPushButton(VistaInserisciRecensioneCliente)
        self.pushButtonAnnulla.setObjectName(u"pushButtonAnnulla")
        self.pushButtonAnnulla.setGeometry(QRect(560, 440, 91, 29))
        self.pushButtonAnnulla.setStyleSheet(u"QPushButton {\n"
"    background-color: #963C00;\n"
"    color: #FF7800;\n"
"    border: 2px solid #502800;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C86400;\n"
"}\n"
"")
        self.comboBoxStelle = QComboBox(VistaInserisciRecensioneCliente)
        self.comboBoxStelle.setObjectName(u"comboBoxStelle")
        self.comboBoxStelle.setGeometry(QRect(30, 220, 76, 26))
        self.comboBoxStelle.setStyleSheet(u"QComboBox {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #321E00;\n"
"	color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"	border-radius: 4px;\n"
"    selection-background-color: #C86400;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #C86400;\n"
"}")
        self.textEditTesto = QTextEdit(VistaInserisciRecensioneCliente)
        self.textEditTesto.setObjectName(u"textEditTesto")
        self.textEditTesto.setGeometry(QRect(290, 220, 401, 191))
        self.textEditTesto.setStyleSheet(u"QTextEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTextEdit QScrollBar:vertical {\n"
"        background: #B46E00;\n"
"        border: 2px solid #190E00;\n"
"        border-radius: 4px;\n"
"        width: 21px;\n"
"        margin: 5px;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical {\n"
"	background: #965A00;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical:hover {\n"
"     background: #C86400;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"    border: none;\n"
"}")
        self.labelErroreStelle = QLabel(VistaInserisciRecensioneCliente)
        self.labelErroreStelle.setObjectName(u"labelErroreStelle")
        self.labelErroreStelle.setGeometry(QRect(30, 250, 141, 20))
        self.labelErroreStelle.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelErroreStelle.setScaledContents(False)
        self.labelErroreTesto = QLabel(VistaInserisciRecensioneCliente)
        self.labelErroreTesto.setObjectName(u"labelErroreTesto")
        self.labelErroreTesto.setGeometry(QRect(290, 410, 191, 20))
        self.labelErroreTesto.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelErroreTesto.setScaledContents(False)

        self.retranslateUi(VistaInserisciRecensioneCliente)

        QMetaObject.connectSlotsByName(VistaInserisciRecensioneCliente)
    # setupUi

    def retranslateUi(self, VistaInserisciRecensioneCliente):
        VistaInserisciRecensioneCliente.setWindowTitle(QCoreApplication.translate("VistaInserisciRecensioneCliente", u"Inserisci Recensione - CineMax", None))
        self.Sfondo.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaInserisciRecensioneCliente", u"Inserisci Recensione", None))
        self.labelTipo.setText(QCoreApplication.translate("VistaInserisciRecensioneCliente", u"Stelle:", None))
        self.labelProfilo.setText("")
        self.labelTesto.setText(QCoreApplication.translate("VistaInserisciRecensioneCliente", u"Testo:", None))
        self.pushButtonConferma.setText(QCoreApplication.translate("VistaInserisciRecensioneCliente", u"Conferma", None))
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaInserisciRecensioneCliente", u"Annulla", None))
        self.labelErroreStelle.setText("")
        self.labelErroreTesto.setText("")
    # retranslateUi

