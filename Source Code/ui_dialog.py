# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout, QVBoxLayout, QHBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Dialog(QDialog):
    def __init__(self, nthCell, excelName):
        super().__init__()
        self.resize(345, 128)
        self.setWindowTitle(u"Simpan")
        self.setStyleSheet(u"QWidget#widgetDeskripsi QLabel {\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QLabel#labelCellValue,\n"
"QLabel#labelNamaValue {\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnBatal,\n"
"QPushButton#btnSimpan {\n"
"min-width: 64px;\n"
"font-size: 16px;\n"
"border-style: none;\n"
"padding: 4px 8px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton#btnBatal {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 24, 128);\n"
"}\n"
"QPushButton#btnBatal:hover {\n"
"background-color: rgb(255, 21, 56);\n"
"}\n"
"\n"
"QPushButton#btnSimpan {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 122, 255);\n"
"}\n"
"QPushButton#btnSimpan:hover {\n"
"background-color: rgb(56, 109, 255);\n"
"}")
        self.setSizeGripEnabled(True)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSimpan = QPushButton(self)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setText(u"Simpan")

        self.horizontalLayout.addWidget(self.btnSimpan)

        self.btnBatal = QPushButton(self)
        self.btnBatal.setObjectName(u"btnBatal")
        self.btnBatal.setText(u"Batal")

        self.horizontalLayout.addWidget(self.btnBatal)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.widgetDeskripsi = QWidget(self)
        self.widgetDeskripsi.setObjectName(u"widgetDeskripsi")
        self.formLayout = QFormLayout(self.widgetDeskripsi)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(24)
        self.labelCell = QLabel(self.widgetDeskripsi)
        self.labelCell.setObjectName(u"labelCell")
        self.labelCell.setText(u"Mulai dari Cell")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelCell)

        self.labelCellValue = QLabel(self.widgetDeskripsi)
        self.labelCellValue.setObjectName(u"labelCellValue")
        self.labelCellValue.setText(nthCell)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.labelCellValue)

        self.labelNama = QLabel(self.widgetDeskripsi)
        self.labelNama.setObjectName(u"labelNama")
        self.labelNama.setText(u"Simpan dengan Nama")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelNama)

        self.labelNamaValue = QLabel(self.widgetDeskripsi)
        self.labelNamaValue.setObjectName(u"labelNamaValue")
        self.labelNamaValue.setText(excelName)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.labelNamaValue)

        self.gridLayout.addWidget(self.widgetDeskripsi, 0, 0, 1, 1)

        # Tombol
        self.btnBatal.clicked.connect(self.close)
        self.btnSimpan.clicked.connect(self.simpanDitekan)

    def simpanDitekan(self) :
        self.accept()


class Success(QDialog) :
    import rc_assets
    def __init__(self, location:str):
        super().__init__()
        # Variable
        self.location = location

        self.resize(345, 128)
        self.setWindowTitle(u"Simpan")
        self.setStyleSheet(u"QWidget#widgetDeskripsi QLabel {\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QLabel#labelDeskripsi {\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#btnBukaFolder,\n"
"QPushButton#btnOk {\n"
"min-width: 64px;\n"
"font-size: 16px;\n"
"border-style: none;\n"
"padding: 4px 8px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton#btnBukaFolder {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 24, 128);\n"
"}\n"
"QPushButton#btnBukaFolder:hover {\n"
"background-color: rgb(255, 21, 56);\n"
"}\n"
"\n"
"QPushButton#btnOk {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 122, 255);\n"
"}\n"
"QPushButton#btnOk:hover {\n"
"background-color: rgb(56, 109, 255);\n"
"}")
        self.setSizeGripEnabled(False)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnOk = QPushButton(self)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setText(u"OK")

        self.horizontalLayout.addWidget(self.btnOk)

        self.btnBukaFolder = QPushButton(self)
        self.btnBukaFolder.setObjectName(u"btnBukaFolder")
        self.btnBukaFolder.setText(u"Buka Folder")

        self.horizontalLayout.addWidget(self.btnBukaFolder)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.widgetDeskripsi = QWidget(self)
        self.widgetDeskripsi.setObjectName(u"widgetDeskripsi")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetDeskripsi)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gambar = QLabel(self.widgetDeskripsi)
        self.gambar.setObjectName(u"gambar")
        self.gambar.setMaximumSize(QSize(64, 64))
        self.gambar.setText(u"")
        self.gambar.setPixmap(QPixmap(u":/icon/icon/success-icon.png"))
        self.gambar.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.gambar)

        self.labelDeskripsi = QLabel(self.widgetDeskripsi)
        self.labelDeskripsi.setObjectName(u"labelDeskripsi")
        self.labelDeskripsi.setText(u"Berhasil Menyimpan!")
        self.labelDeskripsi.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.labelDeskripsi)

        self.horizontalLayout_2.setStretch(1, 1)

        self.gridLayout.addWidget(self.widgetDeskripsi, 0, 0, 1, 1)

        # Button
        self.btnOk.clicked.connect(self.okClicked)
        self.btnBukaFolder.clicked.connect(self.bukaFolderClicked)

    def okClicked(self) :
        self.close()

    def bukaFolderClicked(self) :
        os.popen(f'explorer.exe "{self.location}"')
        self.close()



