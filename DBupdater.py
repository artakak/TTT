#!-*-coding:utf-8-*-
import sys
import os
import re
import shelve
import time
import subprocess
import threading
import datetime
from zipfile import *
#import RedmineAPI
from redmine import Redmine
#import JenkinsAPI
from jenkinsapi.jenkins import Jenkins
# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from ui_test import Ui_MainWindow


#( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'ui_test.ui' )

class Logger(object):
    def __init__(self, output):
        self.output = output

    def write(self, string):
        if not (string == "\n"):
            trstring = QtGui.QApplication.translate("MainWindow", string.strip(), None, QtGui.QApplication.UnicodeUTF8)
            self.output.append(trstring)

class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.DB = shelve.open('DB.txt')
        self.DB['HRM_Trunk'] = [r'C:\ProgramData\Experium_DB_TRUNK_HRM', r'C:\Program Files\EXPERIUM_DB_TRUNK_HRM']
        self.DB['HRM_Release'] = [r'C:\ProgramData\Experium_DB_RELEASE_HRM', r'C:\Program Files\EXPERIUM_DB_RELEASE_HRM']
        self.DB['AGN_Trunk'] = [r'C:\ProgramData\Experium_DB_TRUNK_KA', r'C:\Program Files\EXPERIUM_DB_TRUNK']
        self.DB['AGN_Release'] = [r'C:\ProgramData\Experium_DB_RELEASE_KA', r'C:\Program Files\EXPERIUM_DB_RELEASE_RA']
        self.trunk_expcl_path = r'X:\ExperiumTrunk'
        self.release_expcl_path = r'X:\ExperiumRelease'
        self.cl_exp_path = r'C:\Program Files\Experium'
        self.cl_expgr_path = r'C:\Program Files\ExperiumGr'
        self.ui.lineEdit_7.setText(self.cl_exp_path)
        self.ui.lineEdit_8.setText(self.cl_expgr_path)
        self.ui.pushButton.clicked.connect(self.enumver)
        self.ui.lineEdit_3.setText(self.DB['HRM_Trunk'][0])
        self.ui.lineEdit_6.setText(self.DB['HRM_Trunk'][1])
        self.DB.close()
        self.ui.comboBox.currentIndexChanged.connect(self.db_change)

        self.cl_localdata_path = r'C:\Users\win7_test\AppData\Roaming\Experium\Client'

        data_trunk_hrm_path = r'C:\ProgramData\Experium_DB_TRUNK_HRM'
        data_trunk_ka_path = r'C:\ProgramData\Experium_DB_TRUNK_KA'
        data_release_hrm_path = r'C:\ProgramData\Experium_DB_RELEASE_HRM'
        data_release_ka_path = r'C:\ProgramData\Experium_DB_RELEASE_KA'
        self.data_trunk_path = r'X:\ExperiumTrunk\DB'
        self.data_release_path = r'X:\ExperiumRelease\DB'
        self.X_serv_release_path = r'X:\winserverexe\newexe'
        self.X_serv_trunk_path = r'X:\winserverexe\newexe\trunkexe'
        self.clientupd = [r'\Experium.exe',r'\expenu.dll',r'\exprus.dll',r'\GCalDav.dll',r'\MailEngine.dll',r'\SMSEngine.dll']
        self.srvupd = [r'\exp_srv.exe',r'\sdatacnv.exe',r'\sdatasrv.exe',r'\sexpsrv.exe',r'\smetasrch.exe',r'\smetasrv.exe',r'\srmeta.exe',r'\wcnvnode.exe',r'\wdatacnv.exe',r'\wdatasrv.exe',r'\wmetasrch.exe',r'\wmetasrv.exe',r'\wrmeta.exe']
        self.localdatas = [r'C:\Users\win7_test\AppData\Roaming\ExperiumGr\Client',r'C:\Users\win7_test\AppData\Roaming\Experium\Client']
        self.J = Jenkins('http://buildsrv.experium.ru/', username="golubkin", password="aquasoft")
        self.ui.comboBox_2.addItems(self.J.keys())

        self.ui.pushButton_3.clicked.connect(lambda : self.start_thread(self.start))
        self.ui.pushButton_4.clicked.connect(lambda : self.start_thread(self.stop))
        self.ui.pushButton_6.clicked.connect(lambda : self.start_thread(self.update_cl))
        self.ui.pushButton_5.clicked.connect(lambda : self.start_thread(self.start_cl))
        self.ui.pushButton_2.clicked.connect(lambda : self.start_thread(self.update))
        self.ui.pushButton_7.clicked.connect(self.clrlocal_cl)
        self.ui.pushButton_8.clicked.connect(lambda : self.start_thread(self.redmine))
        self.ui.pushButton_10.clicked.connect(lambda : self.start_thread(self.jenkins))
        self.ui.pushButton_12.clicked.connect(lambda : self.start_thread(self.update_db))
        self.ui.pushButton_11.clicked.connect(self.jenkins_build)
        self.ui.pushButton_9.clicked.connect(self.ui.textBrowser.clear)
        self.logger = Logger(self.ui.textBrowser)
        sys.stdout = self.logger



    def wid_write(self, cmd):
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)
        print p.stdout.read()


    def start_thread(self, meth):
        t = threading.Thread(target=meth)
        t.start()

    def clrlocal_cl(self):
        for f in self.localdatas:
            self.wid_write('RMDIR /s /Q '+f)

    def jenkins(self):
        j = self.J.get_job(self.ui.comboBox_2.currentText())
        q = j.get_last_good_build()
        print('Last good build of '+self.ui.comboBox_2.currentText()+' - '+str(q)+' SVN REV - '+str(q._get_svn_rev()))
        changes = q.get_changeset_items()
        for t in xrange(len(changes)):
            print(str(t+1)+') '+str(changes[t]['msg']).decode('utf8'))
        print('')

    def jenkins_build(self):
        j = self.J.get_job(self.ui.comboBox_2.currentText())
        if j.is_queued_or_running():
            return (1)
        else:
            self.J.build_job(self.ui.comboBox_2.currentText())


    def redmine(self):
        t_time = datetime.date.today()
        redmine = Redmine('http://help.heliosoft.ru', key='ceb184c8482614bd34a72612861176c9a02732ee')
        revpat = r'r\d{5,}'
        issues_open_me = redmine.issue.filter(status_id='open', CF_19='148')
        issues_open_all_totay = redmine.issue.filter(project_id='experium', status_id='open', created_on=str(t_time))
        issues_open_all_totay_up = redmine.issue.filter(project_id='experium', status_id='open', updated_on=str(t_time))
        customt = None
        print('ISSUES FOR ME!!!')
        for t in issues_open_me:
            try:
                customt = t.custom_fields.get(19)
                if customt.value == '148':
                    notes = []
                    revision = []
                    journals = t.journals
                    for k in journals:
                        notes.append(u' '.join(k.notes).encode('utf8').replace(' ',''))
                    for n in notes:
                        revision.append(re.findall(revpat,str(n)))
                    print('<a href="http://help.heliosoft.ru/issues/'+str(t.id)+'">'+str(t.id)+'</a>'+' '+str(max(revision))+' ***'+str(t.status)+'*** '+str(t).decode('utf8'))
            except: customt = None
        print('')

        print('EXPERIUM ISSUES CREATED TODAY!!! '+str(t_time))
        for t in issues_open_all_totay:
            print('<a href="http://help.heliosoft.ru/issues/'+str(t.id)+'">'+str(t.id)+'</a>'+' ***'+str(t.status)+'*** '+str(t).decode('utf8'))
        print('')

        print('EXPERIUM ISSUES UPDATE TODAY!!! '+str(t_time))
        for t in issues_open_all_totay_up:
            print('<a href="http://help.heliosoft.ru/issues/'+str(t.id)+'">'+str(t.id)+'</a>'+' ***'+str(t.status)+'*** '+str(t).decode('utf8'))
        print('')


    def update_cl(self):
        if self.ui.checkBox_2.isChecked():
            self.wid_write("taskkill /im experium.exe")
            for f in self.clientupd:
                self.wid_write('copy /Y "'+self.trunk_expcl_path+f+'" "'+self.cl_exp_path+f+'"')
                self.wid_write('copy /Y "'+self.trunk_expcl_path+f+'" "'+self.cl_expgr_path+f+'"')
        else:
            self.wid_write("taskkill /im experium.exe")
            for f in self.clientupd:
                self.wid_write('copy /Y "'+self.release_expcl_path+f+'" "'+self.cl_exp_path+f+'"')
                self.wid_write('copy /Y "'+self.release_expcl_path+f+'" "'+self.cl_expgr_path+f+'"')
        for f in self.localdatas:
            self.wid_write('RMDIR /s /Q '+f)


        if self.ui.checkBox_3.isChecked():
            self.wid_write("taskkill /t /im exp_srv.exe")
            time.sleep(15)
            if self.ui.checkBox_2.isChecked():
                for f in self.srvupd:
                    self.wid_write('copy /Y "'+self.X_serv_trunk_path+f+'" "'+self.cl_exp_path+f+'"')
            else:
                for f in self.srvupd:
                    self.wid_write('copy /Y "'+self.X_serv_release_path+f+'" "'+self.cl_exp_path+f+'"')
        print('DONE!!!')

    def start_cl(self):
        os.startfile(self.cl_exp_path+'\experium.exe')
        if self.ui.checkBox_3.isChecked():
            os.startfile(self.cl_exp_path+'\exp_srv.exe')



    def start(self):
        self.ui.pushButton_3.setEnabled(False)
        self.server = str(self.ui.lineEdit_6.displayText())
        try:
            self.wid_write('RMDIR /s /Q '+self.cl_localdata_path)
            self.stop()
            self.ui.pushButton_3.setEnabled(False)
        except: pass
        self.wid_write('"'+str(self.server)+'\installandrun.cmd"')
        os.startfile(self.cl_exp_path+'\experium.exe')
        print('DONE!!!')


    def stop(self):
        self.wid_write('"'+str(self.server)+'\pause.cmd"')
        self.wid_write('"'+str(self.server)+'\uninstallsvc.cmd"')
        self.ui.pushButton_3.setEnabled(True)
        print('DONE!!!')

    def update(self):
        self.server = str(self.ui.lineEdit_6.displayText())
        try:
            self.stop()
        except: pass
        if str(self.ui.comboBox.currentText()) == 'HRM_Trunk' or str(self.ui.comboBox.currentText()) == 'AGN_Trunk':
            for f in self.srvupd:
                self.wid_write('copy /Y "'+self.X_serv_trunk_path+f+'" "'+self.server+f+'"')
        else:
            for f in self.srvupd:
                self.wid_write('copy /Y "'+self.X_serv_release_path+f+'" "'+self.server+f+'"')
        if self.ui.checkBox.isChecked():
            for f in self.srvupd:
                self.wid_write('copy /Y "'+self.X_serv_trunk_path+f+'" "'+self.server+f+'"')
        print('DONE!!!')

    def update_db(self):
        data_path = self.ui.lineEdit_3.displayText()
        self.server = str(self.ui.lineEdit_6.displayText())
        try:
            self.stop()
        except: pass
        if str(self.ui.comboBox.currentText()) == 'HRM_Trunk' or str(self.ui.comboBox.currentText()) == 'AGN_Trunk':
            X_path = self.data_trunk_path
            if str(self.ui.comboBox.currentText()) == 'HRM_Trunk':
                base1 = 'db0hr.zip'
            else:
                base1 = 'db0ra.zip'
        else:
            X_path = self.data_release_path
            if str(self.ui.comboBox.currentText()) == 'HRM_Release':
                base1 = 'db0hr.zip'
            else:
                base1 = 'db0ra.zip'
        base = r'\\'+base1
        self.wid_write('RMDIR /s /Q '+data_path+'\BACKUPDATA')
        self.wid_write('RMDIR /s /Q '+data_path+'\DATASERVERDATA')
        self.wid_write('RMDIR /s /Q '+data_path+'\METASERVERDATA')
        self.wid_write('copy /Y "'+X_path+base+'" "'+data_path+base+'"')
        z = ZipFile(data_path+base,'r')
        z.extractall(data_path)
        z.close()
        self.wid_write('DEL /Q '+data_path+base)
        print('DONE!!!')

    def db_change(self):
        self.DB = shelve.open('DB.txt')
        DB_name = str(self.ui.comboBox.currentText())
        self.ui.lineEdit_3.setText(self.DB[DB_name][0])
        self.ui.lineEdit_6.setText(self.DB[DB_name][1])
        self.DB.close()

    def enumver(self):
        versions = [re.findall(r'\d{4,}',f) for f in os.listdir(self.trunk_expcl_path)]
        self.ui.lineEdit.setText(str(max(versions)))
        versions = [re.findall(r'\d{4,}',f) for f in os.listdir(self.release_expcl_path)]
        self.ui.lineEdit_2.setText(str(max(versions)))

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