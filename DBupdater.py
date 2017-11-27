#!-*-coding:utf-8-*-
import sys
import os
import re
import shelve
import time
import subprocess
import threading
import datetime
import win32clipboard
from zipfile import *
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.utils.crumb_requester import CrumbRequester
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
from redmine import Redmine
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
        self.ui.lineEdit_7.setText(self.cl_exp_path)
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
        self.clientupd = [r'\Experium.exe',r'\expenu.dll',r'\exprus.dll',r'\GCalDav.dll',r'\MailEngine.dll',r'\SMSEngine.dll',r'\Telephony.dll']
        self.srvupd = [r'\exp_srv.exe',r'\sdatacnv.exe',r'\sdatasrv.exe',r'\sexpsrv.exe',r'\smetasrch.exe',r'\smetasrv.exe',r'\srmeta.exe',r'\wcnvnode.exe',r'\wdatacnv.exe',r'\wdatasrv.exe',r'\wmetasrch.exe',r'\wmetasrv.exe',r'\wrmeta.exe']
        self.localdatas = [r'C:\Users\win7_test\AppData\Roaming\Experium\Client']

        self.J = Jenkins('http://buildsrv.experium.ru/', username="golubkin", password="aquasoft",
                         requester=CrumbRequester(baseurl='http://buildsrv.experium.ru/', username="golubkin",
                                                  password="aquasoft"))
        self.ui.comboBox_2.addItems(self.J.keys())

        self.ui.calendarWidget.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.ui.calendarWidget.setWindowTitle('Calendar for Redmine')

        self.ui.widget.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.ui.widget.setWindowTitle('Database Info')
        self.ui.widget.setWindowModality(QtCore.Qt.WindowModal)

        self.ui.widget_2.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.ui.widget_2.setWindowTitle('API Options')
        self.ui.widget_2.setWindowModality(QtCore.Qt.WindowModal)

        self.ui.pushButton.clicked.connect(self.enumver)
        self.ui.pushButton_7.clicked.connect(self.clrlocal_cl)
        self.ui.pushButton_11.clicked.connect(self.jenkins_build)
        self.ui.pushButton_9.clicked.connect(self.ui.textBrowser.clear)
        self.ui.pushButton_3.clicked.connect(lambda: self.start_thread(self.start))
        self.ui.pushButton_4.clicked.connect(lambda: self.start_thread(self.stop))
        self.ui.pushButton_6.clicked.connect(lambda: self.start_thread(self.update_cl))
        self.ui.pushButton_5.clicked.connect(lambda: self.start_thread(self.start_cl))
        self.ui.pushButton_2.clicked.connect(lambda: self.start_thread(self.update))
        self.ui.pushButton_10.clicked.connect(self.jenkins)
        self.ui.pushButton_8.clicked.connect(self.redmine)
        self.ui.pushButton_12.clicked.connect(lambda: self.start_thread(self.update_db))
        self.ui.pushButton_13.clicked.connect(lambda: self.start_thread(self.stop_cl))
        self.ui.pushButton_14.clicked.connect(self.jenkins_queue)
        self.ui.pushButton_18.clicked.connect(lambda: self.start_thread(self.ess))
        self.ui.pushButton_19.clicked.connect(self.ui.widget_2.show)
        self.ui.pushButton_17.clicked.connect(self.calendar)
        self.ui.pushButton_15.clicked.connect(self.prep_deploy_databases)
        self.ui.pushButton_22.clicked.connect(self.deploy_database)
        self.ui.pushButton_16.clicked.connect(self.uninstall_databases)
        self.ui.pushButton_24.clicked.connect(self.clear_opt)
        self.ui.comboBox_4.customContextMenuRequested.connect(self.open_menu)
        self.ui.comboBox_5.customContextMenuRequested.connect(self.open_menu_ess)
        try:
            self.ui.comboBox_4.addItems(self.DB['SConfig'])
            if self.ui.comboBox_4.currentText() == '':
                self.ui.comboBox_4.addItem('127.0.0.1')
        except:
            self.ui.comboBox_4.addItem('127.0.0.1')
        try:
            self.ui.comboBox_5.addItems(self.DB['ESS'])
            if self.ui.comboBox_5.currentText() == '':
                self.ui.comboBox_5.addItem('msmeta6.experium.ru')
        except:
            self.ui.comboBox_5.addItem('msmeta6.experium.ru')

        self.logger = Logger(self.ui.textBrowser)
        sys.stdout = self.logger

        for k in self.DB.keys():
            if not k in ['HRM_Trunk','HRM_Release','AGN_Trunk','AGN_Release']:
                self.ui.comboBox.addItem(k)

        self.DB.close()
        self.t_time = None
        self.ui.calendarWidget.selectionChanged.connect(lambda: self.start_thread(self.redmine_anyday))
        #self.ui.tabWidget.setStyleSheet("background-image: url(./Experium.jpg)")
        self.ui.textBrowser.setStyleSheet("background-color: yellow; color: black")

        self.movie = QMovie("exp.gif", QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.ui.label_8.setMovie(self.movie)

    def mstart(self):
        """sart animnation"""
        self.movie.start()

    def mstop(self):
        """stop the animation"""
        self.movie.stop()

    def open_menu(self, position):
        menu = QMenu()
        delete_action = menu.addAction("Delete")
        clear_action = menu.addAction("ClearAll")
        saveto_d_b_action = menu.addAction("SaveToDB")
        action = menu.exec_(self.ui.comboBox_4.mapToGlobal(position))
        if action == delete_action:
            self.ui.comboBox_4.removeItem(self.ui.comboBox_4.currentIndex())
        elif action == clear_action:
            self.ui.comboBox_4.clear()
        elif action == saveto_d_b_action:
            DB = shelve.open('DB.txt')
            DB['SConfig'] = [self.ui.comboBox_4.itemText(i) for i in range(self.ui.comboBox_4.count())]
            DB.close()

    def open_menu_ess(self, position):
        menu = QMenu()
        delete_action = menu.addAction("Delete")
        clear_action = menu.addAction("ClearAll")
        saveto_d_b_action = menu.addAction("SaveToDB")
        action = menu.exec_(self.ui.comboBox_5.mapToGlobal(position))
        if action == delete_action:
            self.ui.comboBox_5.removeItem(self.ui.comboBox_5.currentIndex())
        elif action == clear_action:
            self.ui.comboBox_5.clear()
        elif action == saveto_d_b_action:
            DB = shelve.open('DB.txt')
            DB['ESS'] = [self.ui.comboBox_5.itemText(i) for i in range(self.ui.comboBox_5.count())]
            DB.close()

    @staticmethod
    def output_to_box(text):
        print(text.toUtf8())

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
        self.DB[str(self.DB_name)] = [str(self.DB_data_path), str(self.DB_serv_path), type_flag, trunk_flag]
        self.DB.close()
        self.ui.widget.hide()
        self.ui.comboBox.addItem(str(self.DB_name))
        wdatasrv = open('wdatasrv.par', 'r')
        wdatasrv1 = open('wdatasrv1.par', 'w')
        wmetasrv1 = open('wmetasrv1.par', 'w')
        wmetasrv = open('wmetasrv.par', 'r')
        srvini = open('exp_srv.ini', 'r')
        srvini1 = open('exp_srv1.ini', 'w')
        text = wdatasrv.read()
        wdatasrv1.write(text.replace('DB_data_path', str(self.DB_data_path)))
        text = wmetasrv.read()
        wmetasrv1.write(text.replace('DB_data_path', str(self.DB_data_path)))
        text = srvini.read()
        srvini1.write(text.replace('DB_serv_path', str(self.DB_serv_path)))
        srvini.close()
        srvini1.close()
        wdatasrv.close()
        wdatasrv1.close()
        wmetasrv.close()
        wmetasrv1.close()
        self.wid_write('copy /Y "wdatasrv1.par" "%s\wdatasrv.par"') % str(self.DB_serv_path)
        self.wid_write('copy /Y "wmetasrv1.par" "%s\wmetasrv.par"') % str(self.DB_serv_path)
        self.wid_write('copy /Y "exp_srv1.ini" "%s\exp_srv.ini"') % str(self.DB_serv_path)

    def uninstall_databases(self):
        self.DB = shelve.open('DB.txt')
        if not self.ui.comboBox.currentText() in ['HRM_Trunk', 'HRM_Release', 'AGN_Trunk', 'AGN_Release']:
            self.DB.pop(str(self.ui.comboBox.currentText()))
            self.ui.comboBox.removeItem(self.ui.comboBox.currentIndex())

    @staticmethod
    def wid_write(cmd):
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)
        print p.stdout.read()

    @staticmethod
    def start_thread(meth):
        threading.Thread(target=meth).start()

    def clrlocal_cl(self):
        for f in self.localdatas:
            self.wid_write('RMDIR /s /Q '+f)

    def jenkins(self):
        self.thread2 = Thread2(self)
        self.thread2.message2[str].connect(self.output_to_box)
        self.thread2.start()

    def redmine(self):
        self.thread1 = Thread1(self)
        self.thread1.message1[str].connect(self.output_to_box)
        self.thread1.start()

    def ess(self):
        import requests

        self.ui.lineEdit_8.setStyleSheet("background-color: white")
        if self.ui.lineEdit_15.text() != "":
            ess_key = str(self.ui.lineEdit_15.text())
            url = '%s/SupportSrv/SupportSrv.svc/Support/control/api/grep' % self.ui.comboBox_5.currentText()
            headers = {
                'accept': "application/json, text/plain, */*",
                'origin': "https://msmeta6.experium.ru",
                'x-devtools-emulate-network-conditions-client-id': "41f1c26a-9fd4-48be-b7e5-82cfd3d85220",
                'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
                'content-type': "application/json;charset=UTF-8",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                'authorization': "Basic c3VwcG9ydDpjNTEyODQzNw==",
                'cache-control': "no-cache"}
            try:
                r = requests.post(url, headers=headers, json={'id': ess_key}, verify=False)
                if r.status_code == 200:
                    data = r.text.encode('latin1').decode('utf-8')
                    win32clipboard.OpenClipboard()
                    win32clipboard.EmptyClipboard()
                    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, data)
                    win32clipboard.CloseClipboard()
                    self.ui.lineEdit_8.setStyleSheet("background-color: green")
                else:
                    self.ui.lineEdit_8.setStyleSheet("background-color: red")
            except:
                self.ui.lineEdit_8.setStyleSheet("background-color: red")

    def jenkins_build(self):
        j = self.J.get_job(self.ui.comboBox_2.currentText())
        if not j.is_queued_or_running():
            self.J.build_job(self.ui.comboBox_2.currentText())

    def jenkins_queue(self):
        self.thread4 = Thread4(self)
        self.thread4.message4[str].connect(self.output_to_box)
        self.thread4.signal_start[str].connect(self.mstart)
        self.thread4.signal_stop[str].connect(self.mstop)
        self.thread4.start()

    def calendar(self):
        self.ui.calendarWidget.show()

    def redmine_anyday(self):
        self.thread3 = Thread3(self)
        self.thread3.message3[str].connect(self.output_to_box)
        self.thread3.start()

    def update_cl(self):
        if self.ui.checkBox_4.isChecked():
            if self.ui.checkBox_2.isChecked():
                self.wid_write("taskkill /im experium.exe")
                time.sleep(3)
                for f in self.clientupd:
                    self.wid_write('copy /Y "'+self.trunk_expcl_path+f+'" "'+self.cl_exp_path+f+'"')
            else:
                self.wid_write("taskkill /im experium.exe")
                time.sleep(3)
                for f in self.clientupd:
                    self.wid_write('copy /Y "'+self.release_expcl_path+f+'" "'+self.cl_exp_path+f+'"')
            for f in self.localdatas:
                self.wid_write('RMDIR /s /Q '+f)

        if self.ui.checkBox_3.isChecked():
            self.wid_write("taskkill /t /im exp_srv.exe")
            time.sleep(15)
            self.wid_write("taskkill /t /im wdatacnv.exe")
            if self.ui.checkBox_2.isChecked():
                for f in self.srvupd:
                    self.wid_write('copy /Y "'+self.X_serv_trunk_path+f+'" "'+self.cl_exp_path+f+'"')
            else:
                for f in self.srvupd:
                    self.wid_write('copy /Y "'+self.X_serv_release_path+f+'" "'+self.cl_exp_path+f+'"')
        print('DONE!!!')

    def start_cl(self):
        config = open(self.cl_exp_path + '\config.ini', 'r')
        regex = re.compile(r"^.*Server.*$")
        text2 = []
        for line in config.readlines():
            text2.append(regex.sub('Server=' + str(re.findall('[^ ()]+', str(self.ui.comboBox_4.currentText()))[0]), line))
        config.close()
        config = open(self.cl_exp_path + '\config.ini', 'w')
        config.writelines(text2)
        config.close()
        for i in range(int(self.ui.comboBox_3.currentIndex())+1):
            os.startfile(self.cl_exp_path+'\experium.exe')
        if self.ui.checkBox_3.isChecked():
            os.startfile(self.cl_exp_path+'\exp_srv.exe')
            time.sleep(10)
            self.wid_write("taskkill /im wdatacnv.exe")
            time.sleep(3)
            os.startfile(self.cl_exp_path+'\wdatacnv.exe')

    def stop_cl(self):
        self.wid_write("taskkill /im experium.exe")
        if self.ui.checkBox_3.isChecked():
            self.wid_write("taskkill /t /im exp_srv.exe")
            time.sleep(15)
            self.wid_write("taskkill /t /im wdatacnv.exe")
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
        self.ui.lineEdit.setText("TRUNK "+str(max(versions)))
        versions = [re.findall(r'\d{4,}',f) for f in os.listdir(self.release_expcl_path)]
        self.ui.lineEdit_2.setText("RELEASE "+str(max(versions)))

    def clear_opt(self):
        self.ui.lineEdit_10.clear()
        self.ui.lineEdit_11.clear()
        self.ui.lineEdit_12.clear()
        self.ui.lineEdit_13.clear()
        self.ui.lineEdit_14.clear()
        self.test = QtGui.QFileDialog.getOpenFileName(self, 'Выберите файл для отправки')
        print (self.test)

    @staticmethod
    def save_opt():
        """TODO"""

    def __del__(self):
        self.ui = None


class Thread1(QtCore.QThread):
    def __del__(self):
        self.wait()
    message1 = QtCore.pyqtSignal(str)

    def run(self):
        t_time = datetime.date.today()
        redmine = Redmine('http://help.heliosoft.ru', key='ceb184c8482614bd34a72612861176c9a02732ee')
        issues_open_me = redmine.issue.filter(status_id='open', assigned_to_id=148)
        issues_open_all_totay = redmine.issue.filter(project_id='experium', status_id='open',
                                                         created_on=str(t_time))
        issues_open_all_totay_up = redmine.issue.filter(project_id='experium', status_id='open',
                                                            updated_on=str(t_time))
        self.message1.emit('ISSUES ASSIGNED TO ME!!!')
        for t in issues_open_me:
            self.message1.emit('<a href="http://help.heliosoft.ru/issues/' + str(t.id) + '">' + str(t.id) + '</a> ***' + str(t.status) + '*** ' + str(t).decode('utf8'))

        self.message1.emit('\n\nEXPERIUM ISSUES CREATED TODAY!!! ' + str(t_time))
        for t in issues_open_all_totay:
            self.message1.emit('<a href="http://help.heliosoft.ru/issues/' + str(t.id) + '">' + str(t.id) + '</a> ***' + str(t.status) + '*** ' + str(t).decode('utf8'))

        self.message1.emit('\n\nEXPERIUM ISSUES UPDATE TODAY!!! ' + str(t_time))
        for t in issues_open_all_totay_up:
            self.message1.emit('<a href="http://help.heliosoft.ru/issues/' + str(t.id) + '">' + str(t.id) + '</a> ***' + str(t.status) + '*** ' + str(t).decode('utf8'))


class Thread2(QtCore.QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.Job = w.ui.comboBox_2.currentText()
        self.J = w.J

    def __del__(self):
        self.wait()

    message2 = QtCore.pyqtSignal(str)

    def run(self):
        j = self.J.get_job(self.Job)
        q = j.get_last_good_build()
        self.message2.emit('Last good build of '+self.Job+' - '+str(q)+' SVN REV - '+str(q._get_svn_rev()))
        changes = q.get_changeset_items()
        for t in xrange(len(changes)):
            self.message2.emit('\n'+str(t + 1)+str(changes[t]['msg']).decode('utf8'))
        self.message2.emit('')


class Thread3(QtCore.QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.date = w.ui.calendarWidget.selectedDate().toPyDate()

    def __del__(self):
        self.wait()

    message3 = QtCore.pyqtSignal(str)

    def run(self):
        redmine = Redmine('http://help.heliosoft.ru', key='ceb184c8482614bd34a72612861176c9a02732ee')
        issues_open_all_totay = redmine.issue.filter(project_id='experium', status_id='open', created_on=self.date)
        self.message3.emit('EXPERIUM ISSUES CREATED !!! ' + str(self.date))
        for t in issues_open_all_totay:
            self.message3.emit('<a href="http://help.heliosoft.ru/issues/'+str(t.id)+'">'+str(t.id)+'</a> ***'+str(t.status)+'*** '+str(t).decode('utf8'))
        self.message3.emit('')


class Thread4(QtCore.QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.Job = w.ui.comboBox_2.currentText()
        self.J = w.J

    def __del__(self):
        self.wait()

    message4 = QtCore.pyqtSignal(str)
    signal_start = QtCore.pyqtSignal(str)
    signal_stop = QtCore.pyqtSignal(str)

    def run(self):
        j = self.J.get_job(self.Job)
        if j.is_running():
            self.message4.emit('%s Is Running' % self.Job)
            self.signal_start.emit('job_start')
            while j.is_running():
                time.sleep(10)
            self.message4.emit('%s Is Finished' % self.Job)
            self.signal_stop.emit('job_stop')
        elif j.is_queued:
            self.message4.emit('%s Is Queued' % self.Job)




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