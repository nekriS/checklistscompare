# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 330)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(650, 330))
        MainWindow.setMaximumSize(QSize(650, 330))
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 30, 181, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 181, 21))
        self.linePass1 = QLineEdit(self.centralwidget)
        self.linePass1.setObjectName(u"linePass1")
        self.linePass1.setGeometry(QRect(200, 30, 261, 22))
        self.linePass1.setReadOnly(True)
        self.datePass1 = QLabel(self.centralwidget)
        self.datePass1.setObjectName(u"datePass1")
        self.datePass1.setGeometry(QRect(470, 30, 171, 21))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(200, 10, 261, 21))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(470, 10, 171, 21))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(470, 60, 171, 21))
        self.datePass2 = QLabel(self.centralwidget)
        self.datePass2.setObjectName(u"datePass2")
        self.datePass2.setGeometry(QRect(470, 80, 171, 21))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 80, 181, 24))
        self.linePass2 = QLineEdit(self.centralwidget)
        self.linePass2.setObjectName(u"linePass2")
        self.linePass2.setGeometry(QRect(200, 80, 261, 22))
        self.linePass2.setReadOnly(True)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(200, 60, 261, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 181, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 110, 181, 21))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(200, 110, 261, 21))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 130, 181, 24))
        self.datePass3 = QLabel(self.centralwidget)
        self.datePass3.setObjectName(u"datePass3")
        self.datePass3.setGeometry(QRect(470, 130, 171, 21))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(470, 110, 171, 21))
        self.linePass3 = QLineEdit(self.centralwidget)
        self.linePass3.setObjectName(u"linePass3")
        self.linePass3.setGeometry(QRect(200, 130, 261, 22))
        self.linePass3.setReadOnly(True)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 160, 631, 81))
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 40, 161, 22))
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 20, 171, 21))
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QRect(210, 20, 76, 20))
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(210, 40, 76, 20))
        self.checkBox_2.setChecked(False)
        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(300, 20, 76, 20))
        self.Compare = QPushButton(self.centralwidget)
        self.Compare.setObjectName(u"Compare")
        self.Compare.setGeometry(QRect(530, 270, 111, 24))
        self.filename_line = QLineEdit(self.centralwidget)
        self.filename_line.setObjectName(u"filename_line")
        self.filename_line.setGeometry(QRect(10, 270, 511, 22))
        self.filename_line.setReadOnly(False)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 250, 261, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CheckListCompare", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043f\u043e\u0441\u043b\u0435 1-\u043e\u0439 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438:", None))
        self.linePass1.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.datePass1.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f:", None))
        self.datePass2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.linePass2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043f\u043e\u0441\u043b\u0435 \u0438\u0441\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0439 \u0444\u0430\u0439\u043b:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.datePass3.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f:", None))
        self.linePass3.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"KNS", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"FAV", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"GME", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"KLN", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a\u0438\u0435 \u0441\u0442\u0440\u043e\u043a\u0438 \u0441\u0440\u0430\u0432\u043d\u0438\u0442\u044c?", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"PCB", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Schematic", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"DB", None))
        self.Compare.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0438\u0442\u044c", None))
        self.filename_line.setText(QCoreApplication.translate("MainWindow", u"output_checklist", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0432\u044b\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430:", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

