# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(432, 611)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(432, 238))
        MainWindow.setMaximumSize(QtCore.QSize(432, 611))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Database.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-1, 236, 441, 381))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0);"))
        self.textBrowser.setFrameShape(QtGui.QFrame.Box)
        self.textBrowser.setLineWidth(2)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(-300, 260, 421, 281))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-80, 560, 341, 191))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.lineEdit_4 = QtGui.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 60, 301, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 90, 301, 20))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.radioButton = QtGui.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(30, 120, 45, 17))
        self.radioButton.setAutoExclusive(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.buttonGroup = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radioButton)
        self.pushButton_22 = QtGui.QPushButton(self.widget)
        self.pushButton_22.setGeometry(QtCore.QRect(260, 150, 75, 23))
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.radioButton_2 = QtGui.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(115, 120, 44, 17))
        self.radioButton_2.setAutoExclusive(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_4 = QtGui.QRadioButton(self.widget)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 150, 49, 17))
        self.radioButton_4.setAutoExclusive(True)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.buttonGroup_2 = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.radioButton_3 = QtGui.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(115, 150, 61, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.buttonGroup_2.addButton(self.radioButton_3)
        self.lineEdit_9 = QtGui.QLineEdit(self.widget)
        self.lineEdit_9.setGeometry(QtCore.QRect(30, 20, 301, 20))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(-130, 360, 341, 191))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.lineEdit_10 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(30, 50, 151, 20))
        self.lineEdit_10.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_10.setReadOnly(False)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(200, 50, 131, 20))
        self.lineEdit_11.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_11.setReadOnly(False)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.pushButton_23 = QtGui.QPushButton(self.widget_2)
        self.pushButton_23.setGeometry(QtCore.QRect(260, 150, 75, 23))
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.lineEdit_12 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(30, 20, 301, 20))
        self.lineEdit_12.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_12.setReadOnly(False)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.pushButton_24 = QtGui.QPushButton(self.widget_2)
        self.pushButton_24.setGeometry(QtCore.QRect(170, 150, 75, 23))
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.lineEdit_13 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(30, 80, 151, 20))
        self.lineEdit_13.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineEdit_13.setText(_fromUtf8(""))
        self.lineEdit_13.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_13.setReadOnly(False)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_14 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(200, 80, 131, 20))
        self.lineEdit_14.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_14.setReadOnly(False)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-4, -1, 441, 241))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 13, 421, 191))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.comboBox = QtGui.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox, 2, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_3.addWidget(self.lineEdit_3, 4, 0, 1, 4)
        self.checkBox = QtGui.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_3.addWidget(self.checkBox, 1, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_3.addWidget(self.pushButton_4, 1, 3, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_15 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout_3.addWidget(self.pushButton_15, 2, 1, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout_3.addWidget(self.pushButton_12, 2, 2, 1, 1)
        self.pushButton_16 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.gridLayout_3.addWidget(self.pushButton_16, 2, 3, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setText(_fromUtf8(""))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_3.addWidget(self.lineEdit_6, 6, 0, 1, 4)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget1 = QtGui.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 421, 201))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_7.setText(_fromUtf8(""))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout.addWidget(self.lineEdit_7, 1, 0, 1, 4)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.comboBox_4 = QtGui.QComboBox(self.layoutWidget1)
        self.comboBox_4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.gridLayout.addWidget(self.comboBox_4, 3, 0, 1, 4)
        self.pushButton_5 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 4, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 5, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout.addWidget(self.checkBox_3, 5, 1, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout.addWidget(self.checkBox_4, 5, 2, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.layoutWidget1)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_3, 5, 3, 1, 1)
        self.pushButton_13 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.gridLayout.addWidget(self.pushButton_13, 6, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 6, 1, 1, 2)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(9, 9, 131, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_17 = QtGui.QPushButton(self.tab_3)
        self.pushButton_17.setGeometry(QtCore.QRect(150, 9, 121, 23))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.pushButton_19 = QtGui.QPushButton(self.tab_3)
        self.pushButton_19.setGeometry(QtCore.QRect(285, 9, 131, 23))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.pushButton_10 = QtGui.QPushButton(self.tab_3)
        self.pushButton_10.setGeometry(QtCore.QRect(9, 38, 131, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.comboBox_2 = QtGui.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 39, 271, 20))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.pushButton_11 = QtGui.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(9, 67, 131, 23))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(291, 67, 131, 121))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pushButton_14 = QtGui.QPushButton(self.tab_3)
        self.pushButton_14.setGeometry(QtCore.QRect(150, 67, 131, 23))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_18 = QtGui.QPushButton(self.tab_3)
        self.pushButton_18.setGeometry(QtCore.QRect(9, 96, 131, 23))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.lineEdit_8 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(200, 100, 21, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_15 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(10, 180, 271, 20))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.comboBox_5 = QtGui.QComboBox(self.tab_3)
        self.comboBox_5.setGeometry(QtCore.QRect(10, 150, 271, 20))
        self.comboBox_5.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.comboBox_5.setEditable(True)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 75, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(400, 250, 21, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.widget.raise_()
        self.widget_2.raise_()
        self.calendarWidget.raise_()
        self.tabWidget.raise_()
        self.textBrowser.raise_()
        self.pushButton_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Form1", None))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "DB Server Path", None))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "DB Data Path", None))
        self.radioButton.setText(_translate("MainWindow", "HRM", None))
        self.pushButton_22.setText(_translate("MainWindow", "Deploy", None))
        self.radioButton_2.setText(_translate("MainWindow", "AGN", None))
        self.radioButton_4.setText(_translate("MainWindow", "Trunk", None))
        self.radioButton_3.setText(_translate("MainWindow", "Release", None))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "DB Name", None))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "Jenkins Username", None))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "Jenkins Password", None))
        self.pushButton_23.setText(_translate("MainWindow", "Save", None))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "Redmine API KEY", None))
        self.pushButton_24.setText(_translate("MainWindow", "Clear", None))
        self.lineEdit_13.setPlaceholderText(_translate("MainWindow", "ESS Username", None))
        self.lineEdit_14.setPlaceholderText(_translate("MainWindow", "ESS Password", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "HRM_Trunk", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "HRM_Release", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "AGN_Trunk", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "AGN_Release", None))
        self.checkBox.setText(_translate("MainWindow", "Force Trunk", None))
        self.pushButton_2.setText(_translate("MainWindow", "Update", None))
        self.pushButton_4.setText(_translate("MainWindow", "STOP", None))
        self.pushButton_3.setText(_translate("MainWindow", "Run", None))
        self.pushButton_15.setText(_translate("MainWindow", "Deploy", None))
        self.pushButton_12.setText(_translate("MainWindow", "Clear !!!", None))
        self.pushButton_16.setText(_translate("MainWindow", "Uninstall !!!", None))
        self.label_5.setText(_translate("MainWindow", "DB Server Path", None))
        self.label_2.setText(_translate("MainWindow", "DB Path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Database", None))
        self.label_6.setText(_translate("MainWindow", "Client path", None))
        self.label_7.setText(_translate("MainWindow", "Server config", None))
        self.pushButton_5.setText(_translate("MainWindow", "Start", None))
        self.checkBox_2.setText(_translate("MainWindow", "Trunk", None))
        self.pushButton_6.setText(_translate("MainWindow", "Update", None))
        self.checkBox_3.setText(_translate("MainWindow", "Server", None))
        self.checkBox_4.setText(_translate("MainWindow", "Client", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3", None))
        self.pushButton_13.setText(_translate("MainWindow", "STOP", None))
        self.pushButton_7.setText(_translate("MainWindow", "ClrLocalData", None))
        self.pushButton.setText(_translate("MainWindow", "Enum Rev", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Client", None))
        self.pushButton_8.setText(_translate("MainWindow", "Redmine", None))
        self.pushButton_17.setText(_translate("MainWindow", "Calendar", None))
        self.pushButton_19.setText(_translate("MainWindow", "OPTIONS", None))
        self.pushButton_10.setText(_translate("MainWindow", "Jenkins", None))
        self.pushButton_11.setText(_translate("MainWindow", "Build", None))
        self.pushButton_14.setText(_translate("MainWindow", "Queue", None))
        self.pushButton_18.setText(_translate("MainWindow", "ESSLog", None))
        self.lineEdit_15.setPlaceholderText(_translate("MainWindow", "ESS key", None))
        self.label_9.setText(_translate("MainWindow", "ESS list", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "API", None))
        self.pushButton_9.setText(_translate("MainWindow", "X", None))

