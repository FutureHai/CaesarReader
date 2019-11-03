import subprocess
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import time
import json
import win32ras
from PyQt5.QtCore import QThread, pyqtSignal, QRunnable, QThreadPool

from myMainWindow import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep


class CaesarReaderWindow(QMainWindow, Ui_myMainWindow):
    chromeDriverPath = os.path.abspath('chromedriver.exe')
    driver = None

    def __init__(self, parent=None):
        super(CaesarReaderWindow, self).__init__(parent)

        self.setupUi(self)
        self.connectPppoeBtn.clicked.connect(self.connect_pppoe)
        self.disconnectPppoeBtn.clicked.connect(self.disconnect_pppoe)
        self.saveConfigBtn.clicked.connect(self.save_config_click)
        self.startReadBtn.clicked.connect(self.start_read_click)
        self.stopReadBtn.clicked.connect(self.end_read_click)
        self.init_config()

    def init_config(self):
        try:
            initConfigTask = InitConfigTask(self)
            pool = QThreadPool.globalInstance()
            pool.start(initConfigTask)
        except Exception as e:
            self.print_log(str(e))
        pass

    def connect_pppoe(self):
        pp = PPPOETask(self)
        pool = QThreadPool.globalInstance()
        pool.start(pp)
        pass

    def popen(self, cmd):
        try:
            popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            popen.wait()
            lines = popen.stdout.readlines()
            return [line.decode('gbk') for line in lines]
        except BaseException as e:
            self.print_log(str(e))
            return -1

    def disconnect_pppoe(self):

        pass

    def save_config_click(self):
        """
        保存全局配置信息
        :return:
        """
        startTime = self.startTimeEdit.text()
        endTime = self.endTimeEdit.text()
        pauseTimeFrom = self.pauseTimeFromEdit.text()
        pauseTimeTo = self.pauseTimeToEdit.text()
        slipTimesFrom = self.slipTimesFromEdit.text()
        slipTimesTo = self.slipTimesToEdit.text()
        chromeLocation = self.chromeLocationEdit.text()
        configObj = {
            'startTime': startTime,
            'endTime': endTime,
            'pauseTimeFrom': pauseTimeFrom,
            'pauseTimeTo': pauseTimeTo,
            'slipTimesFrom': slipTimesFrom,
            'slipTimesTo': slipTimesTo,
            'chromeLocationEdit': chromeLocation
        }

        with open(os.path.abspath('config.ini'), 'w') as f:
            f.write(json.dumps(configObj))
            f.flush()
            f.close()
        pass

    def start_read_click(self):
        """
        开始阅读
        :return:

        try:
            driverThread = DriverThread()
            driverThread.trigger.connect(self.build_driver)
            driverThread.start()
        except Exception as e:
            self.print_log(e)
        pass
         """
        self.build_driver()
        pass

    def end_read_click(self):
        if self.driver:
            self.driver.quit()
        pass

    def build_driver(self):
        print("aaaaaaaaaaaaaaa")
        mobileEmulation = {"deviceMetrics": {"width": 320, "height": 640, "pixelRatio": 3.0},
                           "userAgent": 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'}
        # mobileEmulation = {'deviceName': 'Apple iPhone 5'}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=250,640')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--disable-javascript')
        chrome_options.binary_location = self.chromeLocationEdit.text()
        chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_experimental_option('w3c', False)
        print("bbbbbbbbbbbbbbbbb")
        self.driver = webdriver.Chrome(executable_path=self.chromeDriverPath, options=chrome_options)
        # 操作这个对象.
        self.driver.get('https://www.baidu.com')
        sleep(3)
        print("ccccccccccccccccccc")
        action = TouchActions(self.driver)
        action.scroll(0, 200).perform()
        sleep(3)
        action.scroll(0, 200).perform()
        sleep(3)
        action.scroll(0, 200).perform()
        # driver.get('https://www.oceanbluecloud.com')
        sleep(3)
        #driver.quit()
        pass

    def print_log(self, message):
        try:
            logTask = LogTask(self, message)
            pool = QThreadPool.globalInstance()
            pool.start(logTask)
        except Exception as msg:
            print(msg)
        pass

    def print_log_sync(self, message):
        self.logTxtBr.append(message)
        self.logTxtBr.moveCursor(self.logTxtBr.textCursor().End)  # 光标移到最后，这样就会自动显示出来
        pass

    def ConnectPPPOE(self, dialname, account, passwd):
        dial_params = (dialname, '', '', account, passwd, '')
        return win32ras.Dial(None, None, dial_params, None)

    def DialBroadband(self):
        dialname = '宽带连接'  # just a name
        account = self.accountEdit.text()
        passwd = self.passwordEdit.text()
        self.print_log_sync("begin connect! account:" + account + " password:" + passwd)
        try:
            # handle is a pid, for disconnect or showipadrress, if connect success return 0.
            # account is the username that your ISP supposed, passwd is the password.
            handle, result = self.ConnectPPPOE(dialname, account, passwd)
            if result == 0:
                self.print_log_sync("Connection success!")
                return handle, result
            else:
                print("Connection failed, wait for 5 seconds and try again...")
                self.print_log_sync("Connection failed, wait for 5 seconds and try again...")
                time.sleep(5)
                #self.DialBroadband()
                return -1, -1
        except Exception as e:
            self.print_log_sync("Can't finish this connection, please check out." + str(e))
            return -1, -1

    def DisconnectPPPOE(self, handle):
        self.print_log_sync("Disconnection start!")
        if handle is not None:
            try:
                win32ras.HangUp(handle)
                self.print_log_sync("Disconnection success!")
                return "success"
            except Exception as e:
                self.print_log_sync("Disconnection failed, wait for 5 seconds and try again...")
                time.sleep(5)
                self.DisconnectPPPOE(handle)
        else:
            self.print_log_sync("Can't find the process!")
            return

    def Check_for_Broadband(self):
        connections = win32ras.EnumConnections()
        if len(connections) == 0:
            self.print_log_sync("The system is not running any broadband connection.")
            return
        else:
            self.print_log_sync("The system is running %d broadband connection." % len(connections))
            return connections

    def ShowIpAddress(self, handle):
        #self.print_log_sync(str(win32ras.GetConnectStatus(handle)))
        self.print_log_sync("ready ipconfig")

        ipconfig_result_list = self.popen('ipconfig')
        if ipconfig_result_list == -1:
            return

        ip_str = None
        have_ppp = 0
        for line in ipconfig_result_list:
            if line.find("宽带连接") >= 0:
                have_ppp = 1

            if have_ppp == 1:
                if line.strip().startswith("IPv4 地址"):
                    ip_str = line.split(":")[1].strip()
                    have_ppp = 0

        if ip_str:
            self.print_log_sync("ip_str is " + ip_str)
            self.pppoeIpLbl.setText(ip_str)
        pass


class InitConfigTask(QRunnable):
    def __init__(self, window):
        super(InitConfigTask, self).__init__()
        self.window = window
        pass

    def run(self):
        try:
            with open(os.path.abspath('config.ini'), 'r') as f:
                configJson = f.read()
                configDic = json.loads(configJson)
                self.window.startTimeEdit.setText(configDic["startTime"])
                self.window.endTimeEdit.setText(configDic["endTime"])
                self.window.pauseTimeFromEdit.setText(configDic["pauseTimeFrom"])
                self.window.pauseTimeToEdit.setText(configDic["pauseTimeTo"])
                self.window.slipTimesFromEdit.setText(configDic["slipTimesFrom"])
                self.window.slipTimesToEdit.setText(configDic["slipTimesTo"])
                self.window.chromeLocationEdit.setText(configDic["chromeLocation"])
        except Exception as e:
            print(e)
        pass


class DriverThread(QThread):
    trigger = pyqtSignal()

    def __init__(self):
        super(DriverThread, self).__init__()
        pass

    def run(self):
        self.trigger.emit()
        pass


class LogTask(QRunnable):
    def __init__(self, window, message):
        super(LogTask, self).__init__()
        self.window = window
        self.message = message
        pass

    def run(self):
        self.window.logTxtBr.append(self.message)
        self.window.logTxtBr.moveCursor(self.window.logTxtBr.textCursor().End)  # 光标移到最后，这样就会自动显示出来
        pass


class PPPOETask(QRunnable):
    def __init__(self, window):
        super(PPPOETask, self).__init__()
        self.window = window
        pass

    def run(self):
        try:
            data = self.window.Check_for_Broadband()
            # if exist running broadband connection, disconnected it.
            if data is not None:
                for p in data:
                    self.window.print_log_sync("p[0] is " + str(p[0]))
                    self.window.ShowIpAddress(p[0])
                    if self.window.DisconnectPPPOE(p[0]) == "success":
                        self.window.print_log_sync("%s has been disconnected." % p[1])
                    time.sleep(3)
            else:
                try:
                    pid, res = self.window.DialBroadband()
                    if res == 0:
                        self.window.ShowIpAddress(pid)
                    else:
                        self.window.print_log_sync(str(pid) + " " + str(res))
                    time.sleep(3)
                except Exception as ee:
                    self.window.print_log_sync(str(ee))
        except Exception as e:
            self.window.print_log_sync(str(e))
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CaesarReaderWindow()
    win.show()
    sys.exit(app.exec_())
