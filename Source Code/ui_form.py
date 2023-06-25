# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)
import rc_assets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setMinimumSize(QSize(720, 480))
        MainWindow.setWindowTitle(u"MainWindow")
        icon = QIcon()
        icon.addFile(u":/icon/icon/kdu-beauty.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/*\n"
"* General\n"
"*/\n"
"QToolButton {\n"
"background-color:transparent;\n"
"border-style:none;\n"
"}\n"
"\n"
"QTabWidget, QListView, QTextEdit, QTableWidget {\n"
"border-style:none;\n"
"}\n"
"\n"
"/*\n"
"* Main Region\n"
"*/\n"
"QWidget#widgetTombol {\n"
"/*Default*/\n"
"/* background-color:rgb(7, 51, 97); */\n"
"/*background-color: rgb(137, 51, 186);*/\n"
"background-color:rgb(10, 115, 255)\n"
"}\n"
"\n"
"QWidget#widgetTombol QLabel#labelJudul {\n"
"color:rgb(85, 255, 255);\n"
"font-weight:bold;\n"
"font-size:24px;\n"
"}\n"
"\n"
"QWidget#widgetTombol QToolButton {\n"
"min-width:80px;\n"
"min-height:30px;\n"
"padding: 12px 8px;\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget#widgetTombol QToolButton:hover {\n"
"background-color:rgb(0, 170, 0);\n"
"color:rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLabel#labelVersi {\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"/*\n"
"* Editor Region\n"
"*/\n"
"QWidget#widgetTitleBar QToolButton {\n"
"padding: 4px 12px;\n"
"}\n"
"\n"
"QToolButton#tbE"
                        "xit:hover {\n"
"background-color:rgb(170, 85, 0);\n"
"}\n"
"\n"
"QToolButton#tbMaximize:hover,\n"
"QToolButton#tbMinimize:hover {\n"
"background-color:rgb(170, 170, 0);\n"
"}\n"
"\n"
"QSplitter#splitter {\n"
"margin:0 16px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"border-top:2px solid rgb(0, 170, 255);\n"
"}\n"
"\n"
"QTabWidget QTabBar::tab {\n"
"padding: 4px 12px;\n"
"border-top-right-radius:4px;\n"
"border-top-left-radius:4px;\n"
"}\n"
"\n"
"QTabWidget QTabBar::tab:selected {\n"
"background-color:rgb(0, 170, 255);\n"
"}\n"
"\n"
"QTabWidget QTabBar::tab:!selected {\n"
"background-color:rgb(0, 255, 0);\n"
"margin-top:4px;\n"
"}\n"
"\n"
"QTableWidget > QWidget {\n"
"background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Widget Shortcut */\n"
"QWidget#widgetShortcut QLabel {\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#tombolKembali {\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralLayout = QHBoxLayout(self.centralwidget)
        self.centralLayout.setSpacing(0)
        self.centralLayout.setObjectName(u"centralLayout")
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetTombol = QWidget(self.centralwidget)
        self.widgetTombol.setObjectName(u"widgetTombol")
        self.widgetTombol.setMinimumSize(QSize(225, 0))
        self.layoutMain = QVBoxLayout(self.widgetTombol)
        self.layoutMain.setObjectName(u"layoutMain")
        self.layoutMain.setContentsMargins(16, 32, 16, 8)
        self.labelJudul = QLabel(self.widgetTombol)
        self.labelJudul.setObjectName(u"labelJudul")
        self.labelJudul.setText(u"Data Extractor")

        self.layoutMain.addWidget(self.labelJudul, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.layoutTombol = QVBoxLayout()
        self.layoutTombol.setSpacing(24)
        self.layoutTombol.setObjectName(u"layoutTombol")
        self.tombolFolder = QToolButton(self.widgetTombol)
        self.tombolFolder.setObjectName(u"tombolFolder")
        self.tombolFolder.setText(u"Pilih Folder")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tombolFolder.setIcon(icon1)
        self.tombolFolder.setIconSize(QSize(64, 64))
        self.tombolFolder.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.layoutTombol.addWidget(self.tombolFolder, 0, Qt.AlignHCenter)

        self.tombolShortcut = QToolButton(self.widgetTombol)
        self.tombolShortcut.setObjectName(u"tombolShortcut")
        self.tombolShortcut.setText(u"Tampilkan\n"
"Shortcut")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/keyboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tombolShortcut.setIcon(icon2)
        self.tombolShortcut.setIconSize(QSize(64, 64))
        self.tombolShortcut.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.layoutTombol.addWidget(self.tombolShortcut, 0, Qt.AlignHCenter)

        self.widgetShortcut = QWidget(self.widgetTombol)
        self.widgetShortcut.setObjectName(u"widgetShortcut")
        self.layoutShortcut = QGridLayout(self.widgetShortcut)
        self.layoutShortcut.setObjectName(u"layoutShortcut")
        self.layoutShortcut.setHorizontalSpacing(24)
        self.labelC3a = QLabel(self.widgetShortcut)
        self.labelC3a.setObjectName(u"labelC3a")
        self.labelC3a.setText(u"Copy ke\n"
"Kolom 3")

        self.layoutShortcut.addWidget(self.labelC3a, 7, 0, 1, 1)

        self.tombolKembali = QPushButton(self.widgetShortcut)
        self.tombolKembali.setObjectName(u"tombolKembali")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tombolKembali.sizePolicy().hasHeightForWidth())
        self.tombolKembali.setSizePolicy(sizePolicy)
#if QT_CONFIG(tooltip)
        self.tombolKembali.setToolTip(u"Kembali")
#endif // QT_CONFIG(tooltip)
        self.tombolKembali.setText(u"Kembali")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/undo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tombolKembali.setIcon(icon3)
        self.tombolKembali.setFlat(True)

        self.layoutShortcut.addWidget(self.tombolKembali, 0, 0, 1, 2)

        self.labelC1a = QLabel(self.widgetShortcut)
        self.labelC1a.setObjectName(u"labelC1a")
        self.labelC1a.setText(u"Copy ke\n"
"Kolom 1")

        self.layoutShortcut.addWidget(self.labelC1a, 5, 0, 1, 1)

        self.labelMTa = QLabel(self.widgetShortcut)
        self.labelMTa.setObjectName(u"labelMTa")
        self.labelMTa.setText(u"Pindahkan Resi\n"
"ke Tab Selesai")

        self.layoutShortcut.addWidget(self.labelMTa, 8, 0, 1, 1)

        self.labelMNa = QLabel(self.widgetShortcut)
        self.labelMNa.setObjectName(u"labelMNa")
        self.labelMNa.setText(u"Pindah ke\n"
"Baris Sebelumnya")

        self.layoutShortcut.addWidget(self.labelMNa, 3, 0, 1, 1)

        self.labelMNb = QLabel(self.widgetShortcut)
        self.labelMNb.setObjectName(u"labelMNb")
        self.labelMNb.setText(u"W")

        self.layoutShortcut.addWidget(self.labelMNb, 3, 1, 1, 1)

        self.labelMPa = QLabel(self.widgetShortcut)
        self.labelMPa.setObjectName(u"labelMPa")
        self.labelMPa.setText(u"Pindah ke\n"
"Baris Selanjutnya")

        self.layoutShortcut.addWidget(self.labelMPa, 4, 0, 1, 1)

        self.labelC3b = QLabel(self.widgetShortcut)
        self.labelC3b.setObjectName(u"labelC3b")
        self.labelC3b.setText(u"3")

        self.layoutShortcut.addWidget(self.labelC3b, 7, 1, 1, 1)

        self.labelMTb = QLabel(self.widgetShortcut)
        self.labelMTb.setObjectName(u"labelMTb")
        self.labelMTb.setText(u"Space")

        self.layoutShortcut.addWidget(self.labelMTb, 8, 1, 1, 1)

        self.labelARb = QLabel(self.widgetShortcut)
        self.labelARb.setObjectName(u"labelARb")
        self.labelARb.setText(u"A")

        self.layoutShortcut.addWidget(self.labelARb, 1, 1, 1, 1)

        self.labelMVb = QLabel(self.widgetShortcut)
        self.labelMVb.setObjectName(u"labelMVb")
        self.labelMVb.setText(u"S")

        self.layoutShortcut.addWidget(self.labelMVb, 4, 1, 1, 1)

        self.labelARa = QLabel(self.widgetShortcut)
        self.labelARa.setObjectName(u"labelARa")
        self.labelARa.setText(u"Tambah Baris")

        self.layoutShortcut.addWidget(self.labelARa, 1, 0, 1, 1)

        self.labelC2a = QLabel(self.widgetShortcut)
        self.labelC2a.setObjectName(u"labelC2a")
        self.labelC2a.setText(u"Copy ke\n"
"Kolom 2")

        self.layoutShortcut.addWidget(self.labelC2a, 6, 0, 1, 1)

        self.labelC2b = QLabel(self.widgetShortcut)
        self.labelC2b.setObjectName(u"labelC2b")
        self.labelC2b.setText(u"2")

        self.layoutShortcut.addWidget(self.labelC2b, 6, 1, 1, 1)

        self.labelC1b = QLabel(self.widgetShortcut)
        self.labelC1b.setObjectName(u"labelC1b")
        self.labelC1b.setText(u"1")

        self.layoutShortcut.addWidget(self.labelC1b, 5, 1, 1, 1)

        self.labelDRb = QLabel(self.widgetShortcut)
        self.labelDRb.setObjectName(u"labelDRb")
        self.labelDRb.setText(u"D")

        self.layoutShortcut.addWidget(self.labelDRb, 2, 1, 1, 1)

        self.labelDRa = QLabel(self.widgetShortcut)
        self.labelDRa.setObjectName(u"labelDRa")
        self.labelDRa.setText(u"Hapus Baris")

        self.layoutShortcut.addWidget(self.labelDRa, 2, 0, 1, 1)


        self.layoutTombol.addWidget(self.widgetShortcut)


        self.layoutMain.addLayout(self.layoutTombol)

        self.layoutAbout = QHBoxLayout()
        self.layoutAbout.setObjectName(u"layoutAbout")
        self.labelVersi = QLabel(self.widgetTombol)
        self.labelVersi.setObjectName(u"labelVersi")
        self.labelVersi.setText(u"v0.1")
        self.labelVersi.setAlignment(Qt.AlignCenter)

        self.layoutAbout.addWidget(self.labelVersi, 0, Qt.AlignBottom)

        self.labelLink = QLabel(self.widgetTombol)
        self.labelLink.setObjectName(u"labelLink")
#if QT_CONFIG(tooltip)
        self.labelLink.setToolTip(u"Lihat Update")
#endif // QT_CONFIG(tooltip)
        self.labelLink.setText(u"<html><head><style>a {text-decoration:none;color:rgb(128,200,128);}</style></head><body><p><a href=\"https://www.github.com/obi1529\">GitHub</a></p></body></html>")
        self.labelLink.setAlignment(Qt.AlignCenter)

        self.layoutAbout.addWidget(self.labelLink, 0, Qt.AlignBottom)


        self.layoutMain.addLayout(self.layoutAbout)


        self.centralLayout.addWidget(self.widgetTombol)

        self.widgetEditor = QWidget(self.centralwidget)
        self.widgetEditor.setObjectName(u"widgetEditor")
        self.layoutEditor = QVBoxLayout(self.widgetEditor)
        self.layoutEditor.setSpacing(0)
        self.layoutEditor.setObjectName(u"layoutEditor")
        self.layoutEditor.setContentsMargins(0, 0, 0, 0)
        self.widgetTitleBar = QWidget(self.widgetEditor)
        self.widgetTitleBar.setObjectName(u"widgetTitleBar")
        self.layoutTitleBar = QHBoxLayout(self.widgetTitleBar)
        self.layoutTitleBar.setSpacing(0)
        self.layoutTitleBar.setObjectName(u"layoutTitleBar")
        self.layoutTitleBar.setContentsMargins(0, 0, 0, 48)
        self.titleBarHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutTitleBar.addItem(self.titleBarHorizontalSpacer)

        self.tbMinimize = QToolButton(self.widgetTitleBar)
        self.tbMinimize.setObjectName(u"tbMinimize")
#if QT_CONFIG(tooltip)
        self.tbMinimize.setToolTip(u"Minimize")
#endif // QT_CONFIG(tooltip)
        self.tbMinimize.setText(u"Min")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/window-minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tbMinimize.setIcon(icon4)

        self.layoutTitleBar.addWidget(self.tbMinimize)

        self.tbMaximize = QToolButton(self.widgetTitleBar)
        self.tbMaximize.setObjectName(u"tbMaximize")
#if QT_CONFIG(tooltip)
        self.tbMaximize.setToolTip(u"Maximize/Restore")
#endif // QT_CONFIG(tooltip)
        self.tbMaximize.setText(u"Max")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/window-restore.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tbMaximize.setIcon(icon5)
        self.tbMaximize.setCheckable(True)

        self.layoutTitleBar.addWidget(self.tbMaximize)

        self.tbExit = QToolButton(self.widgetTitleBar)
        self.tbExit.setObjectName(u"tbExit")
#if QT_CONFIG(tooltip)
        self.tbExit.setToolTip(u"Tutup Aplikasi")
#endif // QT_CONFIG(tooltip)
        self.tbExit.setText(u"Ext")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tbExit.setIcon(icon6)

        self.layoutTitleBar.addWidget(self.tbExit)


        self.layoutEditor.addWidget(self.widgetTitleBar)

        self.splitter = QSplitter(self.widgetEditor)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(8)
        self.splitter.setChildrenCollapsible(False)
        self.widgetPdf = QSplitter(self.splitter)
        self.widgetPdf.setObjectName(u"widgetPdf")
        self.widgetPdf.setOrientation(Qt.Vertical)
        self.widgetPdf.setHandleWidth(8)
        self.widgetPdf.setChildrenCollapsible(False)
        self.tabWidget = QTabWidget(self.widgetPdf)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabProses = QWidget()
        self.tabProses.setObjectName(u"tabProses")
        self.layoutTabProses = QHBoxLayout(self.tabProses)
        self.layoutTabProses.setObjectName(u"layoutTabProses")
        self.layoutTabProses.setContentsMargins(0, 0, 0, 0)
        self.listWidgetProses = QListWidget(self.tabProses)
        self.listWidgetProses.setObjectName(u"listWidgetProses")

        self.layoutTabProses.addWidget(self.listWidgetProses)

        self.tabWidget.addTab(self.tabProses, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProses), u"Proses")
        self.tabSelesai = QWidget()
        self.tabSelesai.setObjectName(u"tabSelesai")
        self.LayoutTabSelesai = QHBoxLayout(self.tabSelesai)
        self.LayoutTabSelesai.setObjectName(u"LayoutTabSelesai")
        self.LayoutTabSelesai.setContentsMargins(0, 0, 0, 0)
        self.listWidgetSelesai = QListWidget(self.tabSelesai)
        self.listWidgetSelesai.setObjectName(u"listWidgetSelesai")

        self.LayoutTabSelesai.addWidget(self.listWidgetSelesai)

        self.tabWidget.addTab(self.tabSelesai, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSelesai), u"Selsai")
        self.widgetPdf.addWidget(self.tabWidget)
        self.textEdit = QTextEdit(self.widgetPdf)
        self.textEdit.setObjectName(u"textEdit")
#if QT_CONFIG(tooltip)
        self.textEdit.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.textEdit.setPlaceholderText(u"")
        self.widgetPdf.addWidget(self.textEdit)
        self.splitter.addWidget(self.widgetPdf)
        self.widgetExcel = QWidget(self.splitter)
        self.widgetExcel.setObjectName(u"widgetExcel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widgetExcel.sizePolicy().hasHeightForWidth())
        self.widgetExcel.setSizePolicy(sizePolicy2)
        self.layoutExcel = QVBoxLayout(self.widgetExcel)
        self.layoutExcel.setObjectName(u"layoutExcel")
        self.layoutExcel.setContentsMargins(0, 0, 0, 0)
        self.toolLayout = QHBoxLayout()
        self.toolLayout.setObjectName(u"toolLayout")
        self.tbTambahRow = QToolButton(self.widgetExcel)
        self.tbTambahRow.setObjectName(u"tbTambahRow")
#if QT_CONFIG(tooltip)
        self.tbTambahRow.setToolTip(u"Tambah Row")
#endif // QT_CONFIG(tooltip)
        self.tbTambahRow.setText(u"Add")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tbTambahRow.setIcon(icon7)

        self.toolLayout.addWidget(self.tbTambahRow)

        self.tbHapusRow = QToolButton(self.widgetExcel)
        self.tbHapusRow.setObjectName(u"tbHapusRow")
#if QT_CONFIG(tooltip)
        self.tbHapusRow.setToolTip(u"Hapus Row")
#endif // QT_CONFIG(tooltip)
        self.tbHapusRow.setText(u"Rmv")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tbHapusRow.setIcon(icon8)

        self.toolLayout.addWidget(self.tbHapusRow)

        self.tbOpen = QToolButton(self.widgetExcel)
        self.tbOpen.setObjectName(u"tbOpen")
#if QT_CONFIG(tooltip)
        self.tbOpen.setToolTip(u"Muat File Excel")
#endif // QT_CONFIG(tooltip)
        self.tbOpen.setText(u"Opn")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/excel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tbOpen.setIcon(icon9)

        self.toolLayout.addWidget(self.tbOpen)

        self.tbSave = QToolButton(self.widgetExcel)
        self.tbSave.setObjectName(u"tbSave")
#if QT_CONFIG(tooltip)
        self.tbSave.setToolTip(u"Simpan")
#endif // QT_CONFIG(tooltip)
        self.tbSave.setText(u"Sav")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icon/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tbSave.setIcon(icon10)

        self.toolLayout.addWidget(self.tbSave)

        self.toolHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.toolLayout.addItem(self.toolHorizontalSpacer)

        self.labelStartCell = QLabel(self.widgetExcel)
        self.labelStartCell.setObjectName(u"labelStartCell")
        self.labelStartCell.setText(u"Start Cell :")

        self.toolLayout.addWidget(self.labelStartCell)

        self.leCell = QLineEdit(self.widgetExcel)
        self.leCell.setObjectName(u"leCell")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leCell.sizePolicy().hasHeightForWidth())
        self.leCell.setSizePolicy(sizePolicy3)
        self.leCell.setMaximumSize(QSize(82, 16777215))
#if QT_CONFIG(tooltip)
        self.leCell.setToolTip(u"Mulai dari Cell...")
#endif // QT_CONFIG(tooltip)
        self.leCell.setText(u"")
        self.leCell.setMaxLength(10)
        self.leCell.setFrame(False)
        self.leCell.setPlaceholderText(u"Mulai dari Cell")

        self.toolLayout.addWidget(self.leCell)

        self.labelFileName = QLabel(self.widgetExcel)
        self.labelFileName.setObjectName(u"labelFileName")
        self.labelFileName.setText(u"File Name :")

        self.toolLayout.addWidget(self.labelFileName)

        self.leFileName = QLineEdit(self.widgetExcel)
        self.leFileName.setObjectName(u"leFileName")
#if QT_CONFIG(tooltip)
        self.leFileName.setToolTip(u"Nama File")
#endif // QT_CONFIG(tooltip)
        self.leFileName.setText(u"")
        self.leFileName.setFrame(False)
        self.leFileName.setPlaceholderText(u"Nama File")

        self.toolLayout.addWidget(self.leFileName)

        self.tbClear = QToolButton(self.widgetExcel)
        self.tbClear.setObjectName(u"tbClear")
#if QT_CONFIG(tooltip)
        self.tbClear.setToolTip(u"Bersihkan Tabel")
#endif // QT_CONFIG(tooltip)
        self.tbClear.setText(u"Rf")
        icon11 = QIcon()
        icon11.addFile(u":/icon/icon/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tbClear.setIcon(icon11)

        self.toolLayout.addWidget(self.tbClear)


        self.layoutExcel.addLayout(self.toolLayout)

        self.tableWidget = QTableWidget(self.widgetExcel)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setText(u"Nama Customer");
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setText(u"Nomor Telepon");
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setText(u"Alamat");
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(1)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.layoutExcel.addWidget(self.tableWidget)

        self.splitter.addWidget(self.widgetExcel)

        self.layoutEditor.addWidget(self.splitter)

        self.layoutEditor.setStretch(1, 1)

        self.centralLayout.addWidget(self.widgetEditor)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        pass
    # retranslateUi

