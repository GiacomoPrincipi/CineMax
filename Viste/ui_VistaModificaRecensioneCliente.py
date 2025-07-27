# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaModificaRecensioneCliente.ui'
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

class Ui_VistaModificaRecensioneCliente(object):
    def setupUi(self, VistaModificaRecensioneCliente):
        if not VistaModificaRecensioneCliente.objectName():
            VistaModificaRecensioneCliente.setObjectName(u"VistaModificaRecensioneCliente")
        VistaModificaRecensioneCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaModificaRecensioneCliente)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"                stop: 0 #321E00,\n"
"        stop: 1 #643C00\n"
"    );\n"
"}")
        self.labelTitolo = QLabel(VistaModificaRecensioneCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 391, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C8B400;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTipo = QLabel(VistaModificaRecensioneCliente)
        self.labelTipo.setObjectName(u"labelTipo")
        self.labelTipo.setGeometry(QRect(40, 190, 81, 20))
        self.labelTipo.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTipo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelProfiloCliente = QLabel(VistaModificaRecensioneCliente)
        self.labelProfiloCliente.setObjectName(u"labelProfiloCliente")
        self.labelProfiloCliente.setGeometry(QRect(40, 50, 121, 121))
        self.labelProfiloCliente.setPixmap(QPixmap(u"Immagini/RecensioneIconCliente.png"))
        self.labelProfiloCliente.setScaledContents(True)
        self.labelTesto = QLabel(VistaModificaRecensioneCliente)
        self.labelTesto.setObjectName(u"labelTesto")
        self.labelTesto.setGeometry(QRect(260, 190, 81, 20))
        self.labelTesto.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTesto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pushButtonConferma = QPushButton(VistaModificaRecensioneCliente)
        self.pushButtonConferma.setObjectName(u"pushButtonConferma")
        self.pushButtonConferma.setGeometry(QRect(670, 450, 91, 29))
        self.pushButtonConferma.setStyleSheet(u"QPushButton {\n"
"    background-color: #963C00;\n"
"    color: #FF7800;\n"
"    border: 2px solid #502800;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C86400;\n"
"}\n"
"")
        self.pushButtonAnnulla = QPushButton(VistaModificaRecensioneCliente)
        self.pushButtonAnnulla.setObjectName(u"pushButtonAnnulla")
        self.pushButtonAnnulla.setGeometry(QRect(560, 450, 91, 29))
        self.pushButtonAnnulla.setStyleSheet(u"QPushButton {\n"
"    background-color: #963C00;\n"
"    color: #FF7800;\n"
"    border: 2px solid #502800;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C86400;\n"
"}\n"
"")
        self.comboBoxStelle = QComboBox(VistaModificaRecensioneCliente)
        self.comboBoxStelle.setObjectName(u"comboBoxStelle")
        self.comboBoxStelle.setGeometry(QRect(40, 210, 76, 26))
        self.comboBoxStelle.setStyleSheet(u"QComboBox {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #321E00;\n"
"        color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"        border-radius: 4px;\n"
"    selection-background-color: #C86400;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #C86400;\n"
"}")
        self.textEditTesto = QTextEdit(VistaModificaRecensioneCliente)
        self.textEditTesto.setObjectName(u"textEditTesto")
        self.textEditTesto.setGeometry(QRect(260, 210, 401, 201))
        self.textEditTesto.setStyleSheet(u"QTextEdit {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"}")
        self.labelErroreStelle = QLabel(VistaModificaRecensioneCliente)
        self.labelErroreStelle.setObjectName(u"labelErroreStelle")
        self.labelErroreStelle.setGeometry(QRect(40, 240, 141, 20))
        self.labelErroreStelle.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelErroreStelle.setScaledContents(False)
        self.labelErroreTesto = QLabel(VistaModificaRecensioneCliente)
        self.labelErroreTesto.setObjectName(u"labelErroreTesto")
        self.labelErroreTesto.setGeometry(QRect(330, 190, 191, 20))
        self.labelErroreTesto.setStyleSheet(u"QLabel {\n"
"    color: #FFFF00;\n"
"}")
        self.labelErroreTesto.setScaledContents(False)

        self.retranslateUi(VistaModificaRecensioneCliente)

        QMetaObject.connectSlotsByName(VistaModificaRecensioneCliente)
    # setupUi

    def retranslateUi(self, VistaModificaRecensioneCliente):
        VistaModificaRecensioneCliente.setWindowTitle(QCoreApplication.translate("VistaModificaRecensioneCliente", u"Modifica Recensione - CineMax", None))
        self.Sfondo.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaModificaRecensioneCliente", u"Modifica Recensione", None))
        self.labelTipo.setText(QCoreApplication.translate("VistaModificaRecensioneCliente", u"Stelle:", None))
        self.labelProfiloCliente.setText("")
        self.labelTesto.setText(QCoreApplication.translate("VistaModificaRecensioneCliente", u"Testo:", None))
        self.pushButtonConferma.setText(QCoreApplication.translate("VistaModificaRecensioneCliente", u"Conferma", None))
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaModificaRecensioneCliente", u"Annulla", None))
        self.labelErroreStelle.setText("")
        self.labelErroreTesto.setText("")
    # retranslateUi

