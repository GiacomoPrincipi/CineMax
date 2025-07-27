# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaInserisciSpettacoloAmministratore.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTimeEdit,
    QWidget)

class Ui_VistaInserisciSpettacoloAmministratore(object):
    def setupUi(self, VistaInserisciSpettacoloAmministratore):
        if not VistaInserisciSpettacoloAmministratore.objectName():
            VistaInserisciSpettacoloAmministratore.setObjectName(u"VistaInserisciSpettacoloAmministratore")
        VistaInserisciSpettacoloAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaInserisciSpettacoloAmministratore)
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
        self.labelIconaFotoAmministratore = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelIconaFotoAmministratore.setObjectName(u"labelIconaFotoAmministratore")
        self.labelIconaFotoAmministratore.setGeometry(QRect(30, 30, 131, 131))
        self.labelIconaFotoAmministratore.setPixmap(QPixmap(u"Immagini/IconaFotoAmministratore.png"))
        self.labelIconaFotoAmministratore.setScaledContents(True)
        self.labelTitolo = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 100, 63, 20))
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitoloPrincipale = QLabel(VistaInserisciSpettacoloAmministratore)
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
        self.labelGenere = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelGenere.setObjectName(u"labelGenere")
        self.labelGenere.setGeometry(QRect(40, 180, 81, 20))
        self.labelGenere.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelGenere.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOrarioInizio = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelOrarioInizio.setObjectName(u"labelOrarioInizio")
        self.labelOrarioInizio.setGeometry(QRect(40, 360, 101, 20))
        self.labelOrarioInizio.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelOrarioInizio.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelSala = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelSala.setObjectName(u"labelSala")
        self.labelSala.setGeometry(QRect(40, 240, 81, 20))
        self.labelSala.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelSala.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelData = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(40, 300, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOrarioFine = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelOrarioFine.setObjectName(u"labelOrarioFine")
        self.labelOrarioFine.setGeometry(QRect(340, 350, 101, 20))
        self.labelOrarioFine.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelOrarioFine.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDurata = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelDurata.setObjectName(u"labelDurata")
        self.labelDurata.setGeometry(QRect(40, 420, 101, 20))
        self.labelDurata.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelDurata.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditTitolo = QLineEdit(VistaInserisciSpettacoloAmministratore)
        self.lineEditTitolo.setObjectName(u"lineEditTitolo")
        self.lineEditTitolo.setGeometry(QRect(180, 120, 291, 26))
        self.lineEditTitolo.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditGenere = QLineEdit(VistaInserisciSpettacoloAmministratore)
        self.lineEditGenere.setObjectName(u"lineEditGenere")
        self.lineEditGenere.setGeometry(QRect(40, 200, 111, 26))
        self.lineEditGenere.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditDurata = QLineEdit(VistaInserisciSpettacoloAmministratore)
        self.lineEditDurata.setObjectName(u"lineEditDurata")
        self.lineEditDurata.setGeometry(QRect(40, 440, 51, 26))
        self.lineEditDurata.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.pushButtonConferma = QPushButton(VistaInserisciSpettacoloAmministratore)
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
        self.pushButtonAnnulla = QPushButton(VistaInserisciSpettacoloAmministratore)
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
        self.comboBoxSala = QComboBox(VistaInserisciSpettacoloAmministratore)
        self.comboBoxSala.setObjectName(u"comboBoxSala")
        self.comboBoxSala.setGeometry(QRect(40, 260, 76, 26))
        self.comboBoxSala.setStyleSheet(u"QComboBox {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #320F00;\n"
"	color: #962D00;\n"
"    border: 1px solid #190700;\n"
"	border-radius: 4px;\n"
"    selection-background-color: #C83200;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #C83200;\n"
"}")
        self.dateEditData = QDateEdit(VistaInserisciSpettacoloAmministratore)
        self.dateEditData.setObjectName(u"dateEditData")
        self.dateEditData.setGeometry(QRect(40, 320, 110, 26))
        self.dateEditData.setStyleSheet(u"QDateEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"	transition: border-color 1.5s ease;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"	border-color:#FF3C00;\n"
"	transition: border-color 1.5s ease;\n"
"}\n"
"\n"
"")
        self.dateEditData.setDateTime(QDateTime(QDate(1950, 1, 1), QTime(22, 0, 0)))
        self.dateEditData.setTime(QTime(22, 0, 0))
        self.dateEditData.setMaximumDateTime(QDateTime(QDate(2050, 12, 12), QTime(14, 59, 59)))
        self.dateEditData.setMinimumDateTime(QDateTime(QDate(1949, 12, 31), QTime(17, 0, 0)))
        self.timeEditOrarioInizio = QTimeEdit(VistaInserisciSpettacoloAmministratore)
        self.timeEditOrarioInizio.setObjectName(u"timeEditOrarioInizio")
        self.timeEditOrarioInizio.setGeometry(QRect(40, 380, 118, 26))
        self.timeEditOrarioInizio.setStyleSheet(u"QTimeEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"	transition: border-color 1.5s ease;\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"	border-color:#FF3C00;\n"
"	transition: border-color 1.5s ease;\n"
"}\n"
"\n"
"")
        self.timeEditOrarioFine = QTimeEdit(VistaInserisciSpettacoloAmministratore)
        self.timeEditOrarioFine.setObjectName(u"timeEditOrarioFine")
        self.timeEditOrarioFine.setGeometry(QRect(340, 380, 118, 26))
        self.timeEditOrarioFine.setStyleSheet(u"QTimeEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"	transition: border-color 1.5s ease;\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"	border-color:#FF3C00;\n"
"	transition: border-color 1.5s ease;\n"
"}\n"
"\n"
"")
        self.labelErroreTitolo = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelErroreTitolo.setObjectName(u"labelErroreTitolo")
        self.labelErroreTitolo.setGeometry(QRect(490, 120, 121, 20))
        self.labelErroreTitolo.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreGenere = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelErroreGenere.setObjectName(u"labelErroreGenere")
        self.labelErroreGenere.setGeometry(QRect(170, 200, 121, 20))
        self.labelErroreGenere.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreGenere.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreSala = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelErroreSala.setObjectName(u"labelErroreSala")
        self.labelErroreSala.setGeometry(QRect(130, 260, 121, 20))
        self.labelErroreSala.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreSala.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreData = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelErroreData.setObjectName(u"labelErroreData")
        self.labelErroreData.setGeometry(QRect(160, 320, 121, 20))
        self.labelErroreData.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreOrarioInizio = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelErroreOrarioInizio.setObjectName(u"labelErroreOrarioInizio")
        self.labelErroreOrarioInizio.setGeometry(QRect(170, 380, 121, 20))
        self.labelErroreOrarioInizio.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreOrarioInizio.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreOrarioFine = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelErroreOrarioFine.setObjectName(u"labelErroreOrarioFine")
        self.labelErroreOrarioFine.setGeometry(QRect(460, 380, 121, 20))
        self.labelErroreOrarioFine.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreOrarioFine.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreDurata = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelErroreDurata.setObjectName(u"labelErroreDurata")
        self.labelErroreDurata.setGeometry(QRect(110, 440, 121, 20))
        self.labelErroreDurata.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreDurata.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzo = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelPrezzo.setObjectName(u"labelPrezzo")
        self.labelPrezzo.setGeometry(QRect(390, 210, 101, 20))
        self.labelPrezzo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPrezzo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditPrezzo = QLineEdit(VistaInserisciSpettacoloAmministratore)
        self.lineEditPrezzo.setObjectName(u"lineEditPrezzo")
        self.lineEditPrezzo.setGeometry(QRect(390, 230, 111, 26))
        self.lineEditPrezzo.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.labelPrezzoPunti = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelPrezzoPunti.setObjectName(u"labelPrezzoPunti")
        self.labelPrezzoPunti.setGeometry(QRect(390, 270, 101, 20))
        self.labelPrezzoPunti.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPrezzoPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditPrezzoPunti = QLineEdit(VistaInserisciSpettacoloAmministratore)
        self.lineEditPrezzoPunti.setObjectName(u"lineEditPrezzoPunti")
        self.lineEditPrezzoPunti.setGeometry(QRect(390, 290, 111, 26))
        self.lineEditPrezzoPunti.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.labelErrorePrezzo = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelErrorePrezzo.setObjectName(u"labelErrorePrezzo")
        self.labelErrorePrezzo.setGeometry(QRect(510, 230, 121, 20))
        self.labelErrorePrezzo.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErrorePrezzo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErrorePrezzoPunti = QLabel(VistaInserisciSpettacoloAmministratore)
        self.labelErrorePrezzoPunti.setObjectName(u"labelErrorePrezzoPunti")
        self.labelErrorePrezzoPunti.setGeometry(QRect(510, 290, 121, 20))
        self.labelErrorePrezzoPunti.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErrorePrezzoPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(VistaInserisciSpettacoloAmministratore)

        QMetaObject.connectSlotsByName(VistaInserisciSpettacoloAmministratore)
    # setupUi

    def retranslateUi(self, VistaInserisciSpettacoloAmministratore):
        VistaInserisciSpettacoloAmministratore.setWindowTitle(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Inserisci Spettacolo - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFotoAmministratore.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Titolo:", None))
        self.labelTitoloPrincipale.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Inserisci Spettacolo", None))
        self.labelGenere.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Genere:", None))
        self.labelOrarioInizio.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Orario Inizio:", None))
        self.labelSala.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Sala:", None))
        self.labelData.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Data:", None))
        self.labelOrarioFine.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Orario Fine:", None))
        self.labelDurata.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Durata:", None))
        self.lineEditTitolo.setText("")
        self.lineEditGenere.setText("")
        self.lineEditDurata.setText("")
        self.pushButtonConferma.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Conferma", None))
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Annulla", None))
        self.labelErroreTitolo.setText("")
        self.labelErroreGenere.setText("")
        self.labelErroreSala.setText("")
        self.labelErroreData.setText("")
        self.labelErroreOrarioInizio.setText("")
        self.labelErroreOrarioFine.setText("")
        self.labelErroreDurata.setText("")
        self.labelPrezzo.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u"Prezzo:", None))
        self.lineEditPrezzo.setText("")
        self.labelPrezzoPunti.setText(QCoreApplication.translate("VistaInserisciSpettacoloAmministratore", u" Prezzo in punti:", None))
        self.lineEditPrezzoPunti.setText("")
        self.labelErrorePrezzo.setText("")
        self.labelErrorePrezzoPunti.setText("")
    # retranslateUi

