# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaInserisciProdottoAmministratore.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_VistaInserisciProdottoAmministratore(object):
    def setupUi(self, VistaInserisciProdottoAmministratore):
        if not VistaInserisciProdottoAmministratore.objectName():
            VistaInserisciProdottoAmministratore.setObjectName(u"VistaInserisciProdottoAmministratore")
        VistaInserisciProdottoAmministratore.resize(790, 499)
        self.Sfondo = QLabel(VistaInserisciProdottoAmministratore)
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
        self.labelIconaFotoAmministratore = QLabel(VistaInserisciProdottoAmministratore)
        self.labelIconaFotoAmministratore.setObjectName(u"labelIconaFotoAmministratore")
        self.labelIconaFotoAmministratore.setGeometry(QRect(30, 30, 131, 131))
        self.labelIconaFotoAmministratore.setPixmap(QPixmap(u"Immagini/IconaFotoAmministratore.png"))
        self.labelIconaFotoAmministratore.setScaledContents(True)
        self.labelNome = QLabel(VistaInserisciProdottoAmministratore)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(180, 100, 63, 20))
        self.labelNome.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitoloPrincipale = QLabel(VistaInserisciProdottoAmministratore)
        self.labelTitoloPrincipale.setObjectName(u"labelTitoloPrincipale")
        self.labelTitoloPrincipale.setGeometry(QRect(180, 30, 351, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitoloPrincipale.setFont(font1)
        self.labelTitoloPrincipale.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelTitoloPrincipale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelIngredienti = QLabel(VistaInserisciProdottoAmministratore)
        self.labelIngredienti.setObjectName(u"labelIngredienti")
        self.labelIngredienti.setGeometry(QRect(40, 180, 81, 20))
        self.labelIngredienti.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelIngredienti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDisponibile = QLabel(VistaInserisciProdottoAmministratore)
        self.labelDisponibile.setObjectName(u"labelDisponibile")
        self.labelDisponibile.setGeometry(QRect(40, 360, 101, 20))
        self.labelDisponibile.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelDisponibile.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelAllergeni = QLabel(VistaInserisciProdottoAmministratore)
        self.labelAllergeni.setObjectName(u"labelAllergeni")
        self.labelAllergeni.setGeometry(QRect(40, 240, 81, 20))
        self.labelAllergeni.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelAllergeni.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelPrezzo = QLabel(VistaInserisciProdottoAmministratore)
        self.labelPrezzo.setObjectName(u"labelPrezzo")
        self.labelPrezzo.setGeometry(QRect(40, 300, 81, 20))
        self.labelPrezzo.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPrezzo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditNome = QLineEdit(VistaInserisciProdottoAmministratore)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setGeometry(QRect(180, 120, 171, 26))
        self.lineEditNome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.lineEditPrezzo = QLineEdit(VistaInserisciProdottoAmministratore)
        self.lineEditPrezzo.setObjectName(u"lineEditPrezzo")
        self.lineEditPrezzo.setGeometry(QRect(40, 320, 81, 26))
        self.lineEditPrezzo.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.comboBoxDisponibile = QComboBox(VistaInserisciProdottoAmministratore)
        self.comboBoxDisponibile.setObjectName(u"comboBoxDisponibile")
        self.comboBoxDisponibile.setGeometry(QRect(40, 380, 76, 26))
        self.comboBoxDisponibile.setStyleSheet(u"QComboBox {\n"
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
        self.checkBoxAllergene1 = QCheckBox(VistaInserisciProdottoAmministratore)
        self.checkBoxAllergene1.setObjectName(u"checkBoxAllergene1")
        self.checkBoxAllergene1.setGeometry(QRect(40, 260, 91, 24))
        self.checkBoxAllergene1.setStyleSheet(u"QCheckBox {\n"
"	color: #962D00;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    background-color: #320F00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"\n"
"")
        self.checkBoxAllergene2 = QCheckBox(VistaInserisciProdottoAmministratore)
        self.checkBoxAllergene2.setObjectName(u"checkBoxAllergene2")
        self.checkBoxAllergene2.setGeometry(QRect(150, 260, 81, 24))
        self.checkBoxAllergene2.setStyleSheet(u"QCheckBox {\n"
"	color: #962D00;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    background-color: #320F00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"\n"
"")
        self.checkBoxAllergene3 = QCheckBox(VistaInserisciProdottoAmministratore)
        self.checkBoxAllergene3.setObjectName(u"checkBoxAllergene3")
        self.checkBoxAllergene3.setGeometry(QRect(260, 260, 131, 24))
        self.checkBoxAllergene3.setStyleSheet(u"QCheckBox {\n"
"	color: #962D00;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    background-color: #320F00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"\n"
"")
        self.checkBoxAllergene4 = QCheckBox(VistaInserisciProdottoAmministratore)
        self.checkBoxAllergene4.setObjectName(u"checkBoxAllergene4")
        self.checkBoxAllergene4.setGeometry(QRect(420, 260, 71, 24))
        self.checkBoxAllergene4.setStyleSheet(u"QCheckBox {\n"
"	color: #962D00;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    background-color: #320F00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"\n"
"")
        self.checkBoxAllergene5 = QCheckBox(VistaInserisciProdottoAmministratore)
        self.checkBoxAllergene5.setObjectName(u"checkBoxAllergene5")
        self.checkBoxAllergene5.setGeometry(QRect(520, 260, 61, 24))
        self.checkBoxAllergene5.setStyleSheet(u"QCheckBox {\n"
"	color: #962D00;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    background-color: #320F00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"\n"
"")
        self.lineEditIngredienti = QLineEdit(VistaInserisciProdottoAmministratore)
        self.lineEditIngredienti.setObjectName(u"lineEditIngredienti")
        self.lineEditIngredienti.setGeometry(QRect(40, 200, 451, 26))
        self.lineEditIngredienti.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.pushButtonConferma = QPushButton(VistaInserisciProdottoAmministratore)
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
        self.pushButtonAnnulla = QPushButton(VistaInserisciProdottoAmministratore)
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
        self.labelPrezzoPunti = QLabel(VistaInserisciProdottoAmministratore)
        self.labelPrezzoPunti.setObjectName(u"labelPrezzoPunti")
        self.labelPrezzoPunti.setGeometry(QRect(330, 300, 131, 20))
        self.labelPrezzoPunti.setStyleSheet(u"QLabel {\n"
"    color: #C83C00;\n"
"}")
        self.labelPrezzoPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEditPrezzoPunti = QLineEdit(VistaInserisciProdottoAmministratore)
        self.lineEditPrezzoPunti.setObjectName(u"lineEditPrezzoPunti")
        self.lineEditPrezzoPunti.setGeometry(QRect(330, 320, 81, 26))
        self.lineEditPrezzoPunti.setStyleSheet(u"QLineEdit {\n"
"    background-color: #320F00;\n"
"    color: #962D00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}")
        self.checkBoxAllergene6 = QCheckBox(VistaInserisciProdottoAmministratore)
        self.checkBoxAllergene6.setObjectName(u"checkBoxAllergene6")
        self.checkBoxAllergene6.setGeometry(QRect(610, 260, 61, 24))
        self.checkBoxAllergene6.setStyleSheet(u"QCheckBox {\n"
"	color: #962D00;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    background-color: #320F00;\n"
"    border: 1px solid #190700;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	    background-color: #C83200;\n"
"}\n"
"\n"
"\n"
"")
        self.labelErroreNome = QLabel(VistaInserisciProdottoAmministratore)
        self.labelErroreNome.setObjectName(u"labelErroreNome")
        self.labelErroreNome.setGeometry(QRect(360, 120, 121, 20))
        self.labelErroreNome.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreNome.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreIngredienti = QLabel(VistaInserisciProdottoAmministratore)
        self.labelErroreIngredienti.setObjectName(u"labelErroreIngredienti")
        self.labelErroreIngredienti.setGeometry(QRect(500, 200, 161, 20))
        self.labelErroreIngredienti.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreIngredienti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErroreDisponibile = QLabel(VistaInserisciProdottoAmministratore)
        self.labelErroreDisponibile.setObjectName(u"labelErroreDisponibile")
        self.labelErroreDisponibile.setGeometry(QRect(130, 380, 161, 20))
        self.labelErroreDisponibile.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErroreDisponibile.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErrorePrezzo = QLabel(VistaInserisciProdottoAmministratore)
        self.labelErrorePrezzo.setObjectName(u"labelErrorePrezzo")
        self.labelErrorePrezzo.setGeometry(QRect(130, 320, 161, 20))
        self.labelErrorePrezzo.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErrorePrezzo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelErrorePrezzoPunti = QLabel(VistaInserisciProdottoAmministratore)
        self.labelErrorePrezzoPunti.setObjectName(u"labelErrorePrezzoPunti")
        self.labelErrorePrezzoPunti.setGeometry(QRect(420, 320, 161, 20))
        self.labelErrorePrezzoPunti.setStyleSheet(u"QLabel {\n"
"    color: #FF0000\n"
"}")
        self.labelErrorePrezzoPunti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(VistaInserisciProdottoAmministratore)

        QMetaObject.connectSlotsByName(VistaInserisciProdottoAmministratore)
    # setupUi

    def retranslateUi(self, VistaInserisciProdottoAmministratore):
        VistaInserisciProdottoAmministratore.setWindowTitle(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Inserisci Prodotto - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFotoAmministratore.setText("")
        self.labelNome.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Nome:", None))
        self.labelTitoloPrincipale.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Inserisci Prodotto", None))
        self.labelIngredienti.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Ingredienti:", None))
        self.labelDisponibile.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Disponibilit\u00e0:", None))
        self.labelAllergeni.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Allergeni:", None))
        self.labelPrezzo.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Prezzo:", None))
        self.lineEditNome.setText("")
        self.lineEditPrezzo.setText("")
        self.checkBoxAllergene1.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Latticini", None))
        self.checkBoxAllergene2.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Glutine", None))
        self.checkBoxAllergene3.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Frutta a guscio", None))
        self.checkBoxAllergene4.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Pesce", None))
        self.checkBoxAllergene5.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Soia", None))
        self.lineEditIngredienti.setText("")
        self.pushButtonConferma.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Conferma", None))
        self.pushButtonAnnulla.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Annulla", None))
        self.labelPrezzoPunti.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Prezzo in Punti:", None))
        self.lineEditPrezzoPunti.setText("")
        self.checkBoxAllergene6.setText(QCoreApplication.translate("VistaInserisciProdottoAmministratore", u"Uova", None))
        self.labelErroreNome.setText("")
        self.labelErroreIngredienti.setText("")
        self.labelErroreDisponibile.setText("")
        self.labelErrorePrezzo.setText("")
        self.labelErrorePrezzoPunti.setText("")
    # retranslateUi

