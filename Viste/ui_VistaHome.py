# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaHome.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_VistaHome(object):
    def setupUi(self, VistaHome):
        if not VistaHome.objectName():
            VistaHome.setObjectName(u"VistaHome")
        VistaHome.resize(790, 499)
        self.labelTitolo = QLabel(VistaHome)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(210, 70, 371, 71))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable"])
        font.setPointSize(26)
        font.setBold(True)
        self.labelTitolo.setFont(font)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C8C8C8;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelSottotitolo = QLabel(VistaHome)
        self.labelSottotitolo.setObjectName(u"labelSottotitolo")
        self.labelSottotitolo.setGeometry(QRect(280, 130, 231, 20))
        font1 = QFont()
        font1.setPointSize(11)
        self.labelSottotitolo.setFont(font1)
        self.labelSottotitolo.setStyleSheet(u"QLabel {\n"
"    color: #AFAFAF;\n"
"}")
        self.labelSottotitolo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButtonAmministratore = QPushButton(VistaHome)
        self.pushButtonAmministratore.setObjectName(u"pushButtonAmministratore")
        self.pushButtonAmministratore.setGeometry(QRect(320, 240, 161, 41))
        self.pushButtonAmministratore.setStyleSheet(u"QPushButton {\n"
"    background-color: #969696;\n"
"    color: #EEEEEE;\n"
"    border: 2px solid #555555;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C8C8C8;\n"
"}")
        self.Sfondo = QLabel(VistaHome)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, -1, 791, 501))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        self.Sfondo.setFont(font2)
        self.Sfondo.setStyleSheet(u"QLabel {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #191919,\n"
"        stop: 1 #646464\n"
"    );\n"
"}")
        self.pushButtonCliente = QPushButton(VistaHome)
        self.pushButtonCliente.setObjectName(u"pushButtonCliente")
        self.pushButtonCliente.setGeometry(QRect(320, 320, 161, 41))
        self.pushButtonCliente.setStyleSheet(u"QPushButton {\n"
"    background-color: #969696;\n"
"    color: #EEEEEE;\n"
"    border: 2px solid #555555;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C8C8C8;\n"
"}")
        self.Sfondo.raise_()
        self.labelTitolo.raise_()
        self.labelSottotitolo.raise_()
        self.pushButtonAmministratore.raise_()
        self.pushButtonCliente.raise_()

        self.retranslateUi(VistaHome)

        QMetaObject.connectSlotsByName(VistaHome)
    # setupUi

    def retranslateUi(self, VistaHome):
        VistaHome.setWindowTitle(QCoreApplication.translate("VistaHome", u"Home - CineMax", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaHome", u"CINEMAX", None))
        self.labelSottotitolo.setText(QCoreApplication.translate("VistaHome", u"Benvenuto", None))
        self.pushButtonAmministratore.setText(QCoreApplication.translate("VistaHome", u"Amministratore", None))
        self.Sfondo.setText("")
        self.pushButtonCliente.setText(QCoreApplication.translate("VistaHome", u"Cliente", None))
    # retranslateUi

