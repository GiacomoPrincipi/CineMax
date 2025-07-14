# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaInserisciModificaSpettacoloAmministratore.ui'
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

class Ui_VistaInserisciModificaSpettacoloAmministratore(object):
    def setupUi(self, VistaInserisciModificaSpettacoloAmministratore):
        if not VistaInserisciModificaSpettacoloAmministratore.objectName():
            VistaInserisciModificaSpettacoloAmministratore.setObjectName(u"VistaInserisciModificaSpettacoloAmministratore")
        VistaInserisciModificaSpettacoloAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaInserisciModificaSpettacoloAmministratore)
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
        self.labelIconaFotoAmministratore = QLabel(VistaInserisciModificaSpettacoloAmministratore)
        self.labelIconaFotoAmministratore.setObjectName(u"labelIconaFotoAmministratore")
        self.labelIconaFotoAmministratore.setGeometry(QRect(30, 30, 131, 131))
        self.labelIconaFotoAmministratore.setPixmap(QPixmap(u"Immagini/IconaFotoAmministratore.png"))
        self.labelIconaFotoAmministratore.setScaledContents(True)
        self.labelTitolo = QLabel(VistaInserisciModificaSpettacoloAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 100, 63, 20))
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitoloPrincipale = QLabel(VistaInserisciModificaSpettacoloAmministratore)
        self.labelTitoloPrincipale.setObjectName(u"labelTitoloPrincipale")
        self.labelTitoloPrincipale.setGeometry(QRect(180, 30, 411, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitoloPrincipale.setFont(font1)
        self.labelTitoloPrincipale.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTitoloPrincipale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelGenere = QLabel(VistaInserisciModificaSpettacoloAmministratore)
        self.labelGenere.setObjectName(u"labelGenere")
        self.labelGenere.setGeometry(QRect(40, 180, 81, 20))
        self.labelGenere.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelGenere.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOrarioInizio = QLabel(VistaInserisciModificaSpettacoloAmministratore)
        self.labelOrarioInizio.setObjectName(u"labelOrarioInizio")
        self.labelOrarioInizio.setGeometry(QRect(40, 360, 101, 20))
        self.labelOrarioInizio.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelOrarioInizio.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelSala = QLabel(VistaInserisciModificaSpettacoloAmministratore)
        self.labelSala.setObjectName(u"labelSala")
        self.labelSala.setGeometry(QRect(40, 240, 81, 20))
        self.labelSala.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelSala.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelData = QLabel(VistaInserisciModificaSpettacoloAmministratore)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(40, 300, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOrarioFine = QLabel(VistaInserisciModificaSpettacoloAmministratore)
        self.labelOrarioFine.setObjectName(u"labelOrarioFine")
        self.labelOrarioFine.setGeometry(QRect(170, 360, 101, 20))
        self.labelOrarioFine.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelOrarioFine.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDurata = QLabel(VistaInserisciModificaSpettacoloAmministratore)
        self.labelDurata.setObjectName(u"labelDurata")
        self.labelDurata.setGeometry(QRect(40, 420, 101, 20))
        self.labelDurata.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelDurata.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditTitolo = QLineEdit(VistaInserisciModificaSpettacoloAmministratore)
        self.lineEditTitolo.setObjectName(u"lineEditTitolo")
        self.lineEditTitolo.setGeometry(QRect(180, 120, 291, 26))
        self.lineEditTitolo.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditGenere = QLineEdit(VistaInserisciModificaSpettacoloAmministratore)
        self.lineEditGenere.setObjectName(u"lineEditGenere")
        self.lineEditGenere.setGeometry(QRect(40, 200, 111, 26))
        self.lineEditGenere.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditSala = QLineEdit(VistaInserisciModificaSpettacoloAmministratore)
        self.lineEditSala.setObjectName(u"lineEditSala")
        self.lineEditSala.setGeometry(QRect(40, 260, 41, 26))
        self.lineEditSala.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditData = QLineEdit(VistaInserisciModificaSpettacoloAmministratore)
        self.lineEditData.setObjectName(u"lineEditData")
        self.lineEditData.setGeometry(QRect(40, 320, 81, 26))
        self.lineEditData.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditOrarioInizio = QLineEdit(VistaInserisciModificaSpettacoloAmministratore)
        self.lineEditOrarioInizio.setObjectName(u"lineEditOrarioInizio")
        self.lineEditOrarioInizio.setGeometry(QRect(40, 380, 51, 26))
        self.lineEditOrarioInizio.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditOrarioFine = QLineEdit(VistaInserisciModificaSpettacoloAmministratore)
        self.lineEditOrarioFine.setObjectName(u"lineEditOrarioFine")
        self.lineEditOrarioFine.setGeometry(QRect(170, 380, 51, 26))
        self.lineEditOrarioFine.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditDurata = QLineEdit(VistaInserisciModificaSpettacoloAmministratore)
        self.lineEditDurata.setObjectName(u"lineEditDurata")
        self.lineEditDurata.setGeometry(QRect(40, 440, 31, 26))
        self.lineEditDurata.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.pushButtonConferma = QPushButton(VistaInserisciModificaSpettacoloAmministratore)
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
        self.pushButtonAnnulla = QPushButton(VistaInserisciModificaSpettacoloAmministratore)
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

        self.retranslateUi(VistaInserisciModificaSpettacoloAmministratore)

        QMetaObject.connectSlotsByName(VistaInserisciModificaSpettacoloAmministratore)
    # setupUi

    def retranslateUi(self, VistaInserisciModificaSpettacoloAmministratore):
        VistaInserisciModificaSpettacoloAmministratore.setWindowTitle(QCoreApplication.translate("VistaInserisciModificaSpettacoloAmministratore", u"Inserisci/Modifica Spettacolo - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFotoAmministratore.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaInserisciModificaSpettacoloAmministratore", u"Titolo:", None))
        self.labelTitoloPrincipale.setText(QCoreApplication.translate("VistaInserisciModificaSpettacoloAmministratore", u"\"Azione\" + Spettacolo", None))
        self.labelGenere.setText(QCoreApplication.translate("VistaInserisciModificaSpettacoloAmministratore", u"Genere:", None))
        self.labelOrarioInizio.setText(QCoreApplication.translate("VistaInserisciModificaSpettacoloAmministratore", u"Orario Inizio:", None))
        self.labelSala.setText(QCoreApplication.translate("VistaInserisciModificaSpettacoloAmministratore", u"Sala:", None))
        self.labelData.setText(QCoreApplication.translate("VistaInserisciModificaSpettacoloAmministratore", u"Data:", None))
        self.labelOrarioFine.setText(QCoreApplication.translate("VistaInserisciModificaSpettacoloAmministratore", u"Orario Fine:", None))
        self.labelDurata.setText(QCoreApplication.translate("VistaInserisciModificaSpettacoloAmministratore", u"Durata:", None))
        self.lineEditTitolo.setText("")
        self.lineEditGenere.setText("")
        self.lineEditSala.setText("")
        self.lineEditData.setText("")
        self.lineEditOrarioInizio.setText("")
        self.lineEditOrarioFine.setText("")
        self.lineEditDurata.setText("")
        self.pushButtonConferma.setText(QCoreApplication.translate("VistaInserisciModificaSpettacoloAmministratore", u"Conferma", None))
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaInserisciModificaSpettacoloAmministratore", u"Annulla", None))
    # retranslateUi

