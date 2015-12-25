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
from PyQt4 import QtGui, QtCore
from ui_test import Ui_MainWindow


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
        self.DB['HRM_Trunk'] = [r'C:\ProgramData\Experium_DB_TRUNK_HRM', r'C:\Program Files\EXPERIUM_DB_TRUNK_HRM','0','0']
        self.DB['HRM_Release'] = [r'C:\ProgramData\Experium_DB_RELEASE_HRM', r'C:\Program Files\EXPERIUM_DB_RELEASE_HRM','0','1']
        self.DB['AGN_Trunk'] = [r'C:\ProgramData\Experium_DB_TRUNK_KA', r'C:\Program Files\EXPERIUM_DB_TRUNK','1','0']
        self.DB['AGN_Release'] = [r'C:\ProgramData\Experium_DB_RELEASE_KA', r'C:\Program Files\EXPERIUM_DB_RELEASE_RA','1','1']
        self.trunk_expcl_path = r'X:\ExperiumTrunk'
        self.release_expcl_path = r'X:\ExperiumRelease'
        self.cl_exp_path = r'C:\Program Files\Experium'
        self.cl_expgr_path = r'C:\Program Files\ExperiumGr'
        self.ui.lineEdit_7.setText(self.cl_exp_path)
        self.ui.lineEdit_8.setText(self.cl_expgr_path)
        self.ui.lineEdit_3.setText(self.DB['HRM_Trunk'][0])
        self.ui.lineEdit_6.setText(self.DB['HRM_Trunk'][1])
        self.type_flag = (self.DB['HRM_Trunk'][2])
        self.trunk_flag = (self.DB['HRM_Trunk'][3])
        self.ui.comboBox.currentIndexChanged.connect(self.db_change)
        self.cl_localdata_path = r'C:\Users\win7_test\AppData\Roaming\Experium\Client'
        self.data_trunk_path = r'X:\ExperiumTrunk\DB'
        self.data_release_path = r'X:\ExperiumRelease\DB'
        self.X_serv_release_path = r'X:\winserverexe\newexe'
        self.X_serv_trunk_path = r'X:\winserverexe\newexe\trunkexe'
        self.clientupd = [r'\Experium.exe',r'\expenu.dll',r'\exprus.dll',r'\GCalDav.dll',r'\MailEngine.dll',r'\SMSEngine.dll']
        self.srvupd = [r'\exp_srv.exe',r'\sdatacnv.exe',r'\sdatasrv.exe',r'\sexpsrv.exe',r'\smetasrch.exe',r'\smetasrv.exe',r'\srmeta.exe',r'\wcnvnode.exe',r'\wdatacnv.exe',r'\wdatasrv.exe',r'\wmetasrch.exe',r'\wmetasrv.exe',r'\wrmeta.exe']
        self.localdatas = [r'C:\Users\win7_test\AppData\Roaming\ExperiumGr\Client',r'C:\Users\win7_test\AppData\Roaming\Experium\Client']

        self.J = Jenkins('http://buildsrv.experium.ru/', username="golubkin", password="aquasoft")
        self.ui.comboBox_2.addItems(self.J.keys())

        self.ui.calendarWidget.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
        self.ui.calendarWidget.setWindowTitle('Calendar for Redmine')
        #self.ui.calendarWidget.setWindowModality(QtCore.Qt.WindowModal)

        self.ui.widget.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.ui.widget.setWindowTitle('Database Info')
        self.ui.widget.setWindowModality(QtCore.Qt.WindowModal)

        self.ui.pushButton.clicked.connect(self.enumver)
        self.ui.pushButton_7.clicked.connect(self.clrlocal_cl)
        self.ui.pushButton_11.clicked.connect(self.jenkins_build)
        self.ui.pushButton_9.clicked.connect(self.ui.textBrowser.clear)
        self.ui.pushButton_3.clicked.connect(lambda : self.start_thread(self.start))
        self.ui.pushButton_4.clicked.connect(lambda : self.start_thread(self.stop))
        self.ui.pushButton_6.clicked.connect(lambda : self.start_thread(self.update_cl))
        self.ui.pushButton_5.clicked.connect(lambda : self.start_thread(self.start_cl))
        self.ui.pushButton_2.clicked.connect(lambda : self.start_thread(self.update))
        self.ui.pushButton_8.clicked.connect(lambda : self.start_thread(self.redmine))
        self.ui.pushButton_10.clicked.connect(lambda : self.start_thread(self.jenkins))
        self.ui.pushButton_12.clicked.connect(lambda : self.start_thread(self.update_db))
        self.ui.pushButton_13.clicked.connect(lambda : self.start_thread(self.stop_cl))
        self.ui.pushButton_14.clicked.connect(lambda : self.start_thread(self.jenkins_queue))
        self.ui.pushButton_17.clicked.connect(self.calendar)
        self.ui.pushButton_15.clicked.connect(self.prep_deploy_databases)
        self.ui.pushButton_22.clicked.connect(self.deploy_database)
        self.ui.pushButton_16.clicked.connect(self.uninstall_databases)

        self.logger = Logger(self.ui.textBrowser)
        sys.stdout = self.logger

        for k in self.DB.keys():
            if not k in ['HRM_Trunk','HRM_Release','AGN_Trunk','AGN_Release']:
                self.ui.comboBox.addItem(k)

        self.DB.close()
        self.t_time = None
        self.ui.calendarWidget.selectionChanged.connect(lambda : self.start_thread(self.redmine_anyday))

    def prep_deploy_databases(self):
        self.ui.widget.show()
        self.ui.pushButton_22.setEnabled(False)
        self.DB_name, ok = QtGui.QInputDialog.getText(self, 'DBName', 'Enter DB name:')
        self.ui.lineEdit_9.setText(str(self.DB_name))
        self.DB_serv_path = QtGui.QFileDialog.getExistingDirectory(self, 'Select DB Server Path','/')
        self.ui.lineEdit_4.setText(str(self.DB_serv_path))
        self.DB_data_path = QtGui.QFileDialog.getExistingDirectory(self, 'Select DB Data Path','/')
        self.ui.lineEdit_5.setText(str(self.DB_data_path))
        if str(self.DB_name) !='' and str(self.DB_data_path) !='' and str(self.DB_serv_path) !='':
            self.ui.pushButton_22.setEnabled(True)

    def deploy_database(self):
        if self.ui.radioButton.isChecked():
            type_flag = '0'
        elif self.ui.radioButton_2.isChecked():
            type_flag = '1'
        else: return(0)
        if self.ui.radioButton_4.isChecked():
            trunk_flag = '0'
        elif self.ui.radioButton_3.isChecked():
            trunk_flag = '1'
        else: return(0)
        self.DB = shelve.open('DB.txt')
        self.DB[str(self.DB_name)] = [str(self.DB_data_path),str(self.DB_serv_path),type_flag,trunk_flag]
        self.DB.close()
        self.ui.widget.hide()
        self.ui.comboBox.addItem(str(self.DB_name))
        wdatasrv = open('wdatasrv.par','r')
        wdatasrv1 = open('wdatasrv1.par','w')
        wmetasrv1 = open('wmetasrv1.par','w')
        wmetasrv = open('wmetasrv.par','r')
        srvini = open('exp_srv.ini','r')
        srvini1 = open('exp_srv1.ini','w')
        text = wdatasrv.read()
        wdatasrv1.write(text.replace('DB_data_path',str(self.DB_data_path)))
        text = wmetasrv.read()
        wmetasrv1.write(text.replace('DB_data_path',str(self.DB_data_path)))
        text = srvini.read()
        srvini1.write(text.replace('DB_serv_path',str(self.DB_serv_path)))
        srvini.close()
        srvini1.close()
        wdatasrv.close()
        wdatasrv1.close()
        wmetasrv.close()
        wmetasrv1.close()
        self.wid_write('copy /Y "wdatasrv1.par" "'+str(self.DB_serv_path)+'\wdatasrv.par"')
        self.wid_write('copy /Y "wmetasrv1.par" "'+str(self.DB_serv_path)+'\wmetasrv.par"')
        self.wid_write('copy /Y "exp_srv1.ini" "'+str(self.DB_serv_path)+'\exp_srv.ini"')

    def uninstall_databases(self):
        self.DB = shelve.open('DB.txt')
        if not self.ui.comboBox.currentText() in ['HRM_Trunk','HRM_Release','AGN_Trunk','AGN_Release']:
            self.DB.pop(str(self.ui.comboBox.currentText()))
            self.ui.comboBox.removeItem(self.ui.comboBox.currentIndex())

    def wid_write(self, cmd):
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)
        print p.stdout.read()

    def start_thread(self, meth):
        threading.Thread(target=meth).start()

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
        if not j.is_queued_or_running():
            self.J.build_job(self.ui.comboBox_2.currentText())

    def jenkins_queue(self):
        j = self.J.get_job(self.ui.comboBox_2.currentText())
        if j.is_running():
            print(self.ui.comboBox_2.currentText()+' Is Running')
            i = 5
            while j.is_running():
                self.ui.progressBar.setValue(i)
                i+=5
                if i == 100: i = 0
            print(self.ui.comboBox_2.currentText()+' Is Finished')
            self.ui.progressBar.setValue(0)
        elif j.is_queued:
            print(self.ui.comboBox_2.currentText()+' Is Queued')

    def calendar(self):
        self.ui.calendarWidget.show()

    def redmine_anyday(self):
        self.t_time = str(self.ui.calendarWidget.selectedDate().toPyDate())
        redmine = Redmine('http://help.heliosoft.ru', key='ceb184c8482614bd34a72612861176c9a02732ee')
        issues_open_all_totay = redmine.issue.filter(project_id='experium', status_id='open', created_on=str(self.t_time))
        print('EXPERIUM ISSUES CREATED !!! '+str(self.t_time))
        for t in issues_open_all_totay:
            print('<a href="http://help.heliosoft.ru/issues/'+str(t.id)+'">'+str(t.id)+'</a>'+' ***'+str(t.status)+'*** '+str(t).decode('utf8'))
        print('')

    def redmine(self):
        t_time = datetime.date.today()
        redmine = Redmine('http://help.heliosoft.ru', key='ceb184c8482614bd34a72612861176c9a02732ee')
        issues_open_me = redmine.issue.filter(status_id='open', assigned_to_id=148)
        issues_open_all_totay = redmine.issue.filter(project_id='experium', status_id='open', created_on=str(t_time))
        issues_open_all_totay_up = redmine.issue.filter(project_id='experium', status_id='open', updated_on=str(t_time))
        print('ISSUES ASSIGNED TO ME!!!')
        for t in issues_open_me:
            print('<a href="http://help.heliosoft.ru/issues/'+str(t.id)+'">'+str(t.id)+'</a>'+' ***'+str(t.status)+'*** '+str(t).decode('utf8'))
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
        if self.ui.checkBox_4.isChecked():
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

    def stop_cl(self):
        self.wid_write("taskkill /im experium.exe")
        if self.ui.checkBox_3.isChecked():
            self.wid_write("taskkill /t /im exp_srv.exe")
            time.sleep(15)
        print('DONE!!!')

    def start(self):
        self.server = str(self.ui.lineEdit_6.displayText())
        self.wid_write('RMDIR /s /Q '+self.cl_localdata_path)
        self.stop()
        self.ui.pushButton_3.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        self.wid_write('sc create SDataSrv binPath= "'+self.server+'\sdatasrv.exe" type= own start= demand error= normal"')
        self.wid_write('sc create SMetaSrch binPath= "'+self.server+'\smetasrch.exe" type= own start= demand error= normal"')
        self.wid_write('sc create SMetaSrv binPath= "'+self.server+'\smetasrv.exe" type= own start= demand error= normal"')
        self.wid_write('sc create SDataCnv binPath= "'+self.server+'\sdatacnv.exe" type= own start= demand error= normal"')
        self.wid_write('sc create ExperiumLauncherService binPath= "'+self.server+'\sexpsrv.exe" type= own start= auto error= normal"')
        self.wid_write('sc start "ExperiumLauncherService"')
        os.startfile(self.cl_exp_path+'\experium.exe')
        print('DONE!!!')

    def stop(self):
        self.server = str(self.ui.lineEdit_6.displayText())
        self.wid_write('sc stop "ExperiumLauncherService"')
        self.wid_write('sc delete "SDataSrv"')
        self.wid_write('sc delete "SDataCnv"')
        self.wid_write('sc delete "SMetaSrch"')
        self.wid_write('sc delete "SMetaSrv"')
        self.wid_write('sc delete "ExperiumLauncherService"')
        self.ui.pushButton_3.setEnabled(True)
        self.ui.comboBox.setEnabled(True)
        print('DONE!!!')

    def update(self):
        self.server = str(self.ui.lineEdit_6.displayText())
        self.stop()
        print(str(self.trunk_flag))
        print(str(self.type_flag))
        if str(self.trunk_flag) == '0':
            for f in self.srvupd:
                self.wid_write('copy /Y "'+self.X_serv_trunk_path+f+'" "'+self.server+f+'"')
        if str(self.trunk_flag) == '1':
            for f in self.srvupd:
                self.wid_write('copy /Y "'+self.X_serv_release_path+f+'" "'+self.server+f+'"')
        if self.ui.checkBox.isChecked():
            for f in self.srvupd:
                self.wid_write('copy /Y "'+self.X_serv_trunk_path+f+'" "'+self.server+f+'"')
        print('DONE!!!')

    def update_db(self):
        data_path = str(self.ui.lineEdit_3.displayText())
        self.server = str(self.ui.lineEdit_6.displayText())
        self.stop()
        if str(self.trunk_flag) == '0':
            X_path = self.data_trunk_path
            if str(self.type_flag) == '0':
                base1 = 'db0hr.zip'
            if str(self.type_flag) == '1':
                base1 = 'db0ra.zip'
        if str(self.trunk_flag) == '1':
            X_path = self.data_release_path
            if str(self.type_flag) == '0':
                base1 = 'db0hr.zip'
            if str(self.type_flag) == '1':
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
        self.type_flag = str(self.DB[DB_name][2])
        self.trunk_flag = str(self.DB[DB_name][3])
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