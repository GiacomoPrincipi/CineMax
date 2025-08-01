# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VistaVisualizzaSpettacoloCliente.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QWidget)

from Viste.clickablelabel import ClickableLabel

class Ui_VistaVisualizzaSpettacoloCliente(object):
    def setupUi(self, VistaVisualizzaSpettacoloCliente):
        if not VistaVisualizzaSpettacoloCliente.objectName():
            VistaVisualizzaSpettacoloCliente.setObjectName(u"VistaVisualizzaSpettacoloCliente")
        VistaVisualizzaSpettacoloCliente.resize(790, 499)
        self.Sfondo = QLabel(VistaVisualizzaSpettacoloCliente)
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
        self.labelIconaFoto = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelIconaFoto.setObjectName(u"labelIconaFoto")
        self.labelIconaFoto.setGeometry(QRect(30, 30, 131, 131))
        self.labelIconaFoto.setPixmap(QPixmap(u"Viste/Immagini/IconaFotoCliente.png"))
        self.labelIconaFoto.setScaledContents(True)
        self.labelTitolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelTitolo.setObjectName(u"labelTitolo")
        self.labelTitolo.setGeometry(QRect(180, 100, 63, 20))
        self.labelTitolo.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelTitolo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitoloPrincipale = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelTitoloPrincipale.setObjectName(u"labelTitoloPrincipale")
        self.labelTitoloPrincipale.setGeometry(QRect(180, 30, 211, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.labelTitoloPrincipale.setFont(font1)
        self.labelTitoloPrincipale.setStyleSheet(u"QLabel {\n"
"    color: #D7AA0C;\n"
"}")
        self.labelTitoloPrincipale.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelHomeButton = ClickableLabel(VistaVisualizzaSpettacoloCliente)
        self.labelHomeButton.setObjectName(u"labelHomeButton")
        self.labelHomeButton.setGeometry(QRect(700, 20, 63, 61))
        self.labelHomeButton.setPixmap(QPixmap(u"Viste/Immagini/HomeButtonCliente.png"))
        self.labelHomeButton.setScaledContents(True)
        self.labelGenere = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelGenere.setObjectName(u"labelGenere")
        self.labelGenere.setGeometry(QRect(460, 100, 81, 20))
        self.labelGenere.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelGenere.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelTitoloSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelTitoloSpettacolo.setObjectName(u"labelTitoloSpettacolo")
        self.labelTitoloSpettacolo.setGeometry(QRect(180, 130, 251, 20))
        self.labelTitoloSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelGenereSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelGenereSpettacolo.setObjectName(u"labelGenereSpettacolo")
        self.labelGenereSpettacolo.setGeometry(QRect(460, 130, 131, 20))
        self.labelGenereSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelOrarioInizio = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelOrarioInizio.setObjectName(u"labelOrarioInizio")
        self.labelOrarioInizio.setGeometry(QRect(30, 330, 101, 20))
        self.labelOrarioInizio.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelOrarioInizio.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOrarioInizioSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelOrarioInizioSpettacolo.setObjectName(u"labelOrarioInizioSpettacolo")
        self.labelOrarioInizioSpettacolo.setGeometry(QRect(30, 360, 91, 20))
        self.labelOrarioInizioSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelSala = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelSala.setObjectName(u"labelSala")
        self.labelSala.setGeometry(QRect(30, 190, 81, 20))
        self.labelSala.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelSala.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelSalaSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelSalaSpettacolo.setObjectName(u"labelSalaSpettacolo")
        self.labelSalaSpettacolo.setGeometry(QRect(30, 220, 31, 20))
        self.labelSalaSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelData = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setGeometry(QRect(30, 260, 81, 20))
        self.labelData.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelData.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDataSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelDataSpettacolo.setObjectName(u"labelDataSpettacolo")
        self.labelDataSpettacolo.setGeometry(QRect(30, 290, 91, 20))
        self.labelDataSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelIndietroButton = ClickableLabel(VistaVisualizzaSpettacoloCliente)
        self.labelIndietroButton.setObjectName(u"labelIndietroButton")
        self.labelIndietroButton.setGeometry(QRect(620, 20, 63, 61))
        self.labelIndietroButton.setPixmap(QPixmap(u"Viste/Immagini/IndietroButtonCliente.png"))
        self.labelIndietroButton.setScaledContents(True)
        self.labelOrarioFine = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelOrarioFine.setObjectName(u"labelOrarioFine")
        self.labelOrarioFine.setGeometry(QRect(170, 330, 101, 20))
        self.labelOrarioFine.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelOrarioFine.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelOrarioFineSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelOrarioFineSpettacolo.setObjectName(u"labelOrarioFineSpettacolo")
        self.labelOrarioFineSpettacolo.setGeometry(QRect(170, 360, 101, 20))
        self.labelOrarioFineSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.labelDurata = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelDurata.setObjectName(u"labelDurata")
        self.labelDurata.setGeometry(QRect(30, 400, 101, 20))
        self.labelDurata.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelDurata.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.labelDurataSpettacolo = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelDurataSpettacolo.setObjectName(u"labelDurataSpettacolo")
        self.labelDurataSpettacolo.setGeometry(QRect(30, 430, 141, 20))
        self.labelDurataSpettacolo.setStyleSheet(u"QLabel {\n"
"    color: #965A00;\n"
"}")
        self.pushButtonApri = QPushButton(VistaVisualizzaSpettacoloCliente)
        self.pushButtonApri.setObjectName(u"pushButtonApri")
        self.pushButtonApri.setGeometry(QRect(650, 410, 61, 29))
        self.pushButtonApri.setStyleSheet(u"QPushButton {\n"
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
        self.tableViewBiglietti = QTableView(VistaVisualizzaSpettacoloCliente)
        self.tableViewBiglietti.setObjectName(u"tableViewBiglietti")
        self.tableViewBiglietti.setGeometry(QRect(340, 220, 411, 241))
        self.tableViewBiglietti.setStyleSheet(u"QTableView {\n"
"    background-color: #321E00;\n"
"    color: #965A00;\n"
"    border: 1px solid #190E00;\n"
"    border-radius: 4px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QTableView:focus {\n"
"    outline: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #5A3400;\n"
"    color: #C87800;\n"
"    border: 1px solid #3B1C00;\n"
"	border-left: none;\n"
"    border-right: none;\n"
"	text-align: left;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"	border: 1px solid #190E00;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"	border-bottom: none;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #C86400;\n"
"    color: #FF7800;\n"
"}\n"
"\n"
"QTableView QScrollBar:vertical {\n"
"        background: #B46E00;\n"
"        border: 2px solid #190E00;\n"
"        border-radius: 4px;\n"
"        width: 21px;\n"
"        margin: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:vertical {\n"
"	background: #965A00;\n"
"    min-height: 20px;\n"
"    border-radiu"
                        "s: 4px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:vertical:hover {\n"
"     background: #C86400;\n"
"}\n"
"\n"
"QTableView QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"	background: none;\n"
"    border: none;\n"
"}")
        self.tableViewBiglietti.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableViewBiglietti.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableViewBiglietti.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableViewBiglietti.setTabKeyNavigation(False)
        self.tableViewBiglietti.setProperty(u"showDropIndicator", False)
        self.tableViewBiglietti.setDragDropOverwriteMode(False)
        self.tableViewBiglietti.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableViewBiglietti.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableViewBiglietti.setShowGrid(False)
        self.tableViewBiglietti.setCornerButtonEnabled(False)
        self.tableViewBiglietti.horizontalHeader().setHighlightSections(False)
        self.tableViewBiglietti.verticalHeader().setVisible(False)
        self.tableViewBiglietti.verticalHeader().setMinimumSectionSize(25)
        self.tableViewBiglietti.verticalHeader().setDefaultSectionSize(25)
        self.tableViewBiglietti.verticalHeader().setHighlightSections(False)
        self.labelBiglietti = QLabel(VistaVisualizzaSpettacoloCliente)
        self.labelBiglietti.setObjectName(u"labelBiglietti")
        self.labelBiglietti.setGeometry(QRect(340, 190, 81, 20))
        self.labelBiglietti.setStyleSheet(u"QLabel {\n"
"    color: #C87800;\n"
"}")
        self.labelBiglietti.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Sfondo.raise_()
        self.labelIconaFoto.raise_()
        self.labelTitolo.raise_()
        self.labelTitoloPrincipale.raise_()
        self.labelHomeButton.raise_()
        self.labelGenere.raise_()
        self.labelTitoloSpettacolo.raise_()
        self.labelGenereSpettacolo.raise_()
        self.labelOrarioInizio.raise_()
        self.labelOrarioInizioSpettacolo.raise_()
        self.labelSala.raise_()
        self.labelSalaSpettacolo.raise_()
        self.labelData.raise_()
        self.labelDataSpettacolo.raise_()
        self.labelIndietroButton.raise_()
        self.labelOrarioFine.raise_()
        self.labelOrarioFineSpettacolo.raise_()
        self.labelDurata.raise_()
        self.labelDurataSpettacolo.raise_()
        self.tableViewBiglietti.raise_()
        self.pushButtonApri.raise_()
        self.labelBiglietti.raise_()

        self.retranslateUi(VistaVisualizzaSpettacoloCliente)

        QMetaObject.connectSlotsByName(VistaVisualizzaSpettacoloCliente)
    # setupUi

    def retranslateUi(self, VistaVisualizzaSpettacoloCliente):
        VistaVisualizzaSpettacoloCliente.setWindowTitle(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Spettacolo - CineMax", None))
        self.Sfondo.setText("")
        self.labelIconaFoto.setText("")
        self.labelTitolo.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Titolo:", None))
        self.labelTitoloPrincipale.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Spettacolo", None))
        self.labelHomeButton.setText("")
        self.labelGenere.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Genere:", None))
        self.labelTitoloSpettacolo.setText("")
        self.labelGenereSpettacolo.setText("")
        self.labelOrarioInizio.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Orario Inizio:", None))
        self.labelOrarioInizioSpettacolo.setText("")
        self.labelSala.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Sala:", None))
        self.labelSalaSpettacolo.setText("")
        self.labelData.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Data:", None))
        self.labelDataSpettacolo.setText("")
        self.labelIndietroButton.setText("")
        self.labelOrarioFine.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Orario Fine:", None))
        self.labelOrarioFineSpettacolo.setText("")
        self.labelDurata.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Durata:", None))
        self.labelDurataSpettacolo.setText("")
        self.pushButtonApri.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Apri", None))
        self.labelBiglietti.setText(QCoreApplication.translate("VistaVisualizzaSpettacoloCliente", u"Biglietti:", None))
    # retranslateUi

