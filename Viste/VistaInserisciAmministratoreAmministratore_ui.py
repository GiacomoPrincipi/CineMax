# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaInserisciAmministratoreAmministratore.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_VistaInserisciAmministratoreAmministratore(object):
    def setupUi(self, VistaInserisciAmministratoreAmministratore):
        if not VistaInserisciAmministratoreAmministratore.objectName():
            VistaInserisciAmministratoreAmministratore.setObjectName(u"VistaInserisciAmministratoreAmministratore")
        VistaInserisciAmministratoreAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaInserisciAmministratoreAmministratore)
        self.Sfondo.setObjectName(u"Sfondo")
        self.Sfondo.setGeometry(QRect(0, 0, 791, 501))
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
        self.labelProfiloAmministratore = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelProfiloAmministratore.setObjectName(u"labelProfiloAmministratore")
        self.labelProfiloAmministratore.setGeometry(QRect(40, 30, 121, 121))
        self.labelProfiloAmministratore.setPixmap(QPixmap(u"Immagini/profiloButtonAmministratore.png"))
        self.labelProfiloAmministratore.setScaledContents(True)
        self.labelNome = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitolo = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 30, 431, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitolo.setFont(font1)
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelCognome = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelCognome.setObjectName(u"labelCognome")
        self.labelCognome.setGeometry(QRect(330, 100, 81, 20))
        self.labelCognome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelCognome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelMatricola = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelMatricola.setObjectName(u"labelMatricola")
        self.labelMatricola.setGeometry(QRect(40, 180, 81, 20))
        self.labelMatricola.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelMatricola.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelEmail = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(40, 240, 81, 20))
        self.labelEmail.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelEmail.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTelefono = QLabel(VistaInserisciAmministratoreAmministratore)
        self.labelTelefono.setObjectName(u"labelTelefono")
        self.labelTelefono.setGeometry(QRect(40, 300, 81, 20))
        self.labelTelefono.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditEmail = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setGeometry(QRect(40, 260, 231, 26))
        self.lineEditEmail.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditTelefono = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditTelefono.setObjectName(u"lineEditTelefono")
        self.lineEditTelefono.setGeometry(QRect(40, 330, 111, 26))
        self.lineEditTelefono.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditMatricola = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditMatricola.setObjectName(u"lineEditMatricola")
        self.lineEditMatricola.setGeometry(QRect(40, 200, 81, 26))
        self.lineEditMatricola.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditNome = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setGeometry(QRect(180, 120, 131, 26))
        self.lineEditNome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditCognome = QLineEdit(VistaInserisciAmministratoreAmministratore)
        self.lineEditCognome.setObjectName(u"lineEditCognome")
        self.lineEditCognome.setGeometry(QRect(330, 120, 191, 26))
        self.lineEditCognome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.pushButtonConferma = QPushButton(VistaInserisciAmministratoreAmministratore)
        self.pushButtonConferma.setObjectName(u"pushButtonConferma")
        self.pushButtonConferma.setGeometry(QRect(680, 450, 91, 29))
        self.pushButtonConferma.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.pushButtonAnnulla = QPushButton(VistaInserisciAmministratoreAmministratore)
        self.pushButtonAnnulla.setObjectName(u"pushButtonAnnulla")
        self.pushButtonAnnulla.setGeometry(QRect(570, 450, 91, 29))
        self.pushButtonAnnulla.setStyleSheet(u"QPushButton {\n"
"    background-color: #961E00;\n"
"    color: #FF3C00;\n"
"    border: 2px solid #501400;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #C83200;\n"
"}")

        self.retranslateUi(VistaInserisciAmministratoreAmministratore)

        QMetaObject.connectSlotsByName(VistaInserisciAmministratoreAmministratore)
    # setupUi

    def retranslateUi(self, VistaInserisciAmministratoreAmministratore):
        VistaInserisciAmministratoreAmministratore.setWindowTitle(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Inserisci Amministratore - CineMax", None))
        self.Sfondo.setText("")
        self.labelProfiloAmministratore.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Nome:", None))
        self.labelTitolo.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Inserisci Amministratore", None))
        self.labelCognome.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Cognome:", None))
        self.labelMatricola.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Matricola:", None))
        self.labelEmail.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Email:", None))
        self.labelTelefono.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Telefono:", None))
        self.lineEditEmail.setText("")
        self.lineEditTelefono.setText("")
        self.lineEditMatricola.setText("")
        self.lineEditNome.setText("")
        self.lineEditCognome.setText("")
        self.pushButtonConferma.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Conferma", None))
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaInserisciAmministratoreAmministratore", u"Annulla", None))
    # retranslateUi

