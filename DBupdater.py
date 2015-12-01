#!-*-coding:utf-8-*-
import sys
import os
import re
# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# from PyQt4 import uic
from ui_test import Ui_MainWindow


#( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'ui_test.ui' )

class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.trunk_expcl_path = r'X:\ExperiumTrunk'
        self.release_expcl_path = r'X:\ExperiumRelease'
        self.ui.pushButton.clicked.connect(self.enumver)
        self.ui.lineEdit_3.setText(r'C:\ProgramData\Experium_DB_TRUNK_HRM')
        self.ui.lineEdit_4.setText(r'X:\ExperiumTrunk\DB')
        self.ui.lineEdit_5.setText(r'X:\ExperiumRelease\DB')
        self.ui.lineEdit_6.setText(r'X:\winserverexe\newexe\trunkexe')
        self.ui.comboBox.c

    def db_chanfe(self):


    def enumver(self):
        version = []
        for f in os.listdir(self.trunk_expcl_path):
            version.append(re.findall(r'\d{4,}',f))
        self.ui.lineEdit.setText(str(max(version)))
        version = []
        for f in os.listdir(self.release_expcl_path):
            version.append(re.findall(r'\d{4,}',f))
        self.ui.lineEdit_2.setText(str(max(version)))



    def __del__(self):
        self.ui = None


#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('DBupdater')

    # create widget
    w = MainWindow()
    w.setWindowTitle('DBupdater')
    w.show()

    # connection
    QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))

    # execute application
    sys.exit(app.exec_())