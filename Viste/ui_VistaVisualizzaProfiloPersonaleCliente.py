# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaProfiloPersonaleCliente.ui'
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

class Ui_VistaVisualizzaProfiloPersonaleCliente(object):
    def setupUi(self, VistaVisualizzaProfiloPersonaleCliente):
        if not VistaVisualizzaProfiloPersonaleCliente.objectName():
            VistaVisualizzaProfiloPersonaleCliente.setObjectName(u"VistaVisualizzaProfiloPersonaleCliente")
        VistaVisualizzaProfiloPersonaleCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
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
        self.labelProfiloCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelProfiloCliente.setObjectName(u"labelProfiloCliente")
        self.labelProfiloCliente.setGeometry(QRect(40, 30, 121, 121))
        self.labelProfiloCliente.setPixmap(QPixmap(u"Immagini/profiloButtonCliente.png"))
        self.labelProfiloCliente.setScaledContents(True)
        self.labelNome = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 291, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C8B400;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIndietroButtonCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelIndietroButtonCliente.setObjectName(u"labelIndietroButtonCliente")
        self.labelIndietroButtonCliente.setGeometry(QRect(700, 20, 63, 61))
        self.labelIndietroButtonCliente.setPixmap(QPixmap(u"Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButtonCliente.setScaledContents(True)
        self.labelCognome = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelNomeCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelNomeCliente.setObjectName(u"labelNomeCliente")
        self.labelNomeCliente.setGeometry(QRect(180, 120, 131, 20))
        self.labelNomeCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelCognomeCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelCognomeCliente.setObjectName(u"labelCognomeCliente")
        self.labelCognomeCliente.setGeometry(QRect(330, 120, 131, 20))
        self.labelCognomeCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelCodiceFiscale = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelCodiceFiscale.setObjectName(u"labelCodiceFiscale")
        self.labelCodiceFiscale.setGeometry(QRect(40, 180, 111, 20))
        self.labelCodiceFiscale.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelCodiceFiscale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCodiceFiscaleCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelCodiceFiscaleCliente.setObjectName(u"labelCodiceFiscaleCliente")
        self.labelCodiceFiscaleCliente.setGeometry(QRect(40, 200, 131, 20))
        self.labelCodiceFiscaleCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelEmail = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(40, 240, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmailCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelEmailCliente.setObjectName(u"labelEmailCliente")
        self.labelEmailCliente.setGeometry(QRect(40, 260, 251, 20))
        self.labelEmailCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelTelefono = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(40, 300, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefonoCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelTelefonoCliente.setObjectName(u"labelTelefonoCliente")
        self.labelTelefonoCliente.setGeometry(QRect(40, 320, 101, 20))
        self.labelTelefonoCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelPunti = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelPunti.setObjectName(u"labelPunti")
        self.labelPunti.setGeometry(QRect(40, 360, 81, 20))
        self.labelPunti.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPuntiCliente = QLabel(VistaVisualizzaProfiloPersonaleCliente)
        self.labelPuntiCliente.setObjectName(u"labelPuntiCliente")
        self.labelPuntiCliente.setGeometry(QRect(40, 380, 81, 20))
        self.labelPuntiCliente.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.pushButtonModifica = QPushButton(VistaVisualizzaProfiloPersonaleCliente)
        self.pushButtonModifica.setObjectName(u"pushButtonModifica")
        self.pushButtonModifica.setGeometry(QRect(670, 450, 91, 29))
        self.pushButtonModifica.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(VistaVisualizzaProfiloPersonaleCliente)

        QMetaObject.connectSlotsByName(VistaVisualizzaProfiloPersonaleCliente)
    # setupUi

    def retranslateUi(self, VistaVisualizzaProfiloPersonaleCliente):
        VistaVisualizzaProfiloPersonaleCliente.setWindowTitle(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Profilo Personale - CineMax", None))
        self.Sfondo.setText("")
        self.labelProfiloCliente.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Profilo Personale", None))
        self.labelIndietroButtonCliente.setText("")
        self.labelCognome.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Cognome:", None))
        self.labelNomeCliente.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Cliente", None))
        self.labelCognomeCliente.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Cliente", None))
        self.labelCodiceFiscale.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Codice Fiscale:", None))
        self.labelCodiceFiscaleCliente.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"00000000000000", None))
        self.labelEmail.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Email:", None))
        self.labelEmailCliente.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Cliente@gmail.com", None))
        self.labelTelefono.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Telefono:", None))
        self.labelTelefonoCliente.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"3333333333", None))
        self.labelPunti.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Punti:", None))
        self.labelPuntiCliente.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"000", None))
        self.pushButtonModifica.setText(QCoreApplication.translate("VistaVisualizzaProfiloPersonaleCliente", u"Modifica", None))
    # retranslateUi

