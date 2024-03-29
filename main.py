import json
import random
import subprocess
import sys, os

import win32ras

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtCore import QThread, pyqtSignal, QRunnable, QThreadPool

from myMainWindow import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep
from selenium.webdriver.chrome.service import Service


class CaesarReaderWindow(QMainWindow, Ui_myMainWindow):
    def __init__(self, parent=None):
        super(CaesarReaderWindow, self).__init__(parent)

        self.chromeDriverPath = os.path.abspath('chromedriver.exe')
        self.driver = None
        self.c_service = None
        self.startReadFlag = False
        self.stopReadFlag = False
        self.stopPPPOEFlag = False
        # 已完成文章篇数
        self.readNum = 0
        # 剩余文章篇数
        self.unReadNum = 0
        self.driverThread = DriverThread(self)
        self.pppoeThread = PPPOETask(self)

        self.setupUi(self)
        self.connectPppoeBtn.clicked.connect(self.connect_pppoe_click)
        self.disconnectPppoeBtn.clicked.connect(self.disconnect_pppoe_click)
        self.saveConfigBtn.clicked.connect(self.save_config_click)
        self.startReadBtn.clicked.connect(self.start_read_click)
        self.stopReadBtn.clicked.connect(self.end_read_click)
        self.init_config()

    def init_config(self):
        """
        初始化全局配置
        :return:
        """
        try:
            initConfigTask = InitConfigTask(self)
            pool = QThreadPool.globalInstance()
            pool.start(initConfigTask)
        except Exception as e:
            self.print_log(str(e))
        pass

    def popen(self, cmd):
        try:
            popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            popen.wait()
            lines = popen.stdout.readlines()
            return [line.decode('gbk') for line in lines]
        except Exception as e:
            self.print_log("获取ip异常")
            return -1

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
        pxFrom = self.pxFromEdit.text()
        pxTo = self.pxToEdit.text()
        chromeLocation = self.chromeLocationEdit.text()
        if not (
                startTime and
                endTime and
                pauseTimeFrom and
                pauseTimeTo and
                slipTimesFrom and
                slipTimesTo and
                pxFrom and
                pxTo and
                chromeLocation):
            return

        configObj = {
            'startTime': startTime,
            'endTime': endTime,
            'pauseTimeFrom': pauseTimeFrom,
            'pauseTimeTo': pauseTimeTo,
            'slipTimesFrom': slipTimesFrom,
            'slipTimesTo': slipTimesTo,
            'pxFrom': pxFrom,
            'pxTo': pxTo,
            'chromeLocation': chromeLocation
        }

        with open(os.path.abspath('config.ini'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(configObj))
            f.flush()
            f.close()
        pass

    def start_read_click(self):
        """
        开始阅读按钮点击
        :return:
        """
        self.startReadFlag = True
        self.stopReadFlag = False
        try:
            if not self.driverThread.isRunning():
                self.driverThread.trigger.connect(self.reconnect_pppoe)
                self.driverThread.start()
        except Exception as e:
            self.print_log(str(e))
        pass

    def end_read_click(self):
        """
        停止阅读按钮点击
        :return:
        """
        self.startReadFlag = False
        self.stopReadFlag = True

        try:
            if self.driver is not None:
                self.driver.quit()
                self.driver = None
        except Exception as msg:
            pass

        try:
            if self.c_service is not None:
                self.c_service.stop()
                self.c_service = None
        except Exception as msg:
            pass
        pass

    def connect_pppoe_click(self):
        """
        开始拨号按钮点击
        :return:
        """
        self.stopPPPOEFlag = False
        try:
            if not self.pppoeThread.isRunning():
                self.pppoeThread.trigger.connect(self.read_next)
                self.pppoeThread.start()
        except Exception as e:
            self.print_log(str(e))
        pass

    def disconnect_pppoe_click(self):
        """
        停止拨号按钮点击
        :return:
        """
        self.stopPPPOEFlag = True

        data = self.check_for_broadband()
        if data is not None:
            for p in data:
                self.show_ip_address()
                if self.disconnect_pppoe(p[0]) == "success":
                    self.print_log("宽带%s已经断开" % p[1])
                sleep(5)
        pass

    def read_next(self):
        """
        阅读下一篇
        :return:
        """
        if not self.startReadFlag:
            return

        if self.stopReadFlag or self.stopPPPOEFlag:
            return

        self.start_read_click()
        pass

    def reconnect_pppoe(self):
        """
        重新连接pppoe
        :return:
        """
        if self.stopReadFlag or self.stopPPPOEFlag:
            return
        self.connect_pppoe_click()
        pass

    def build_driver(self, url):
        """
        构建阅读driver
        :return:
        """
        if not url:
            self.stopReadFlag = True
            self.print_log("已全部阅读完成\n")
            return

        self.readNum = self.readNum + 1
        self.print_log("开始阅读第 %d 篇，剩余 %d 篇" % (self.readNum, self.unReadNum))
        self.print_log("当前：%s" % url)
        self.c_service = Service(self.chromeDriverPath)
        self.c_service.command_line_args()
        self.c_service.start()

        mobileEmulation = {"deviceMetrics": {"width": 320, "height": 640, "pixelRatio": 3.0},
                           "userAgent": 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'}
        # mobileEmulation = {'deviceName': 'Apple iPhone 5'}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=250,640')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--disable-javascript')
        chrome_options.add_argument('--log-level=3')
        chrome_options.binary_location = self.chromeLocationEdit.text()
        chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=chrome_options)

        # 操作这个对象.
        self.driver.get(url)
        num = random.randint(int(self.slipTimesFromEdit.text()), int(self.slipTimesToEdit.text()))
        # 下滑次数
        hasNum = 0
        for n in range(num):
            if not self.stopReadFlag:
                holdTime = random.randint(int(self.pauseTimeFromEdit.text()), int(self.pauseTimeToEdit.text()))
                px = random.randint(int(self.pxFromEdit.text()), int(self.pxToEdit.text()))
                self.print_log("第 %d 次下滑，等待 %d 秒, 下滑 %d 像素" % (n + 1, holdTime, px))
                # 每次下滑停顿时间
                sleep(holdTime)
                action = TouchActions(self.driver)
                action.scroll(0, 200).perform()
                hasNum = hasNum + 1
            else:
                break

        try:
            if self.driver is not None:
                self.driver.quit()
                self.driver = None
        except Exception as msg:
            pass

        try:
            if self.c_service is not None:
                self.c_service.stop()
                self.c_service = None
        except Exception as msg:
            pass

        if self.stopReadFlag:
            self.print_log("第 %d 篇阅未完成，共下滑 %d 次\n" % (self.readNum, hasNum))
            return
        else:
            self.print_log("第 %d 篇阅读完成，共下滑 %d 次\n" % (self.readNum, hasNum))

        try:
            # 删除第一行
            with open(os.path.abspath('unread.txt'), 'r', encoding='utf-8') as f:
                content = f.readlines()
                with open(os.path.abspath('unread.txt'), 'w+', encoding='utf-8') as f1:
                    f1.writelines(content[1:])
                    f1.flush()
                    f1.close()
                f.close()

            # 追加到最后一行
            with open(os.path.abspath('read.txt'), 'a', encoding='utf-8') as f:
                f.write(url)
                f.close()
        except Exception as e:
            print(e)
        pass

    def build_pppoe(self):
        """
        构建pppoe
        :return:
        """
        data = self.check_for_broadband()
        if data is not None:
            for p in data:
                self.show_ip_address()
                if self.disconnect_pppoe(p[0]) == "success":
                    self.print_log("宽带%s已经断开" % p[1])
                sleep(5)
        else:
            try:
                pid, res = self.dial_broadband()
                if res == 0:
                    self.show_ip_address()
                sleep(5)
            except Exception as ee:
                pass
        pass

    def print_log(self, message):
        """
        异度打印日志
        :param message: 日志信息
        :return:
        """
        try:
            logTask = LogTask(self, message)
            pool = QThreadPool.globalInstance()
            pool.start(logTask)
        except Exception as msg:
            print(msg)
        pass

    def setUnReadNum(self, num):
        self.unReadNum = num

    def connect_pppoe(self, dialname, account, passwd):
        dial_params = (dialname, '', '', account, passwd, '')
        return win32ras.Dial(None, None, dial_params, None)

    def dial_broadband(self):
        """
        宽带拨号
        :return:
        """
        self.pppoeStatusLbl.setText("正在拨号...")
        dialname = '宽带连接'  # just a name
        account = self.accountEdit.text()
        passwd = self.passwordEdit.text()
        self.print_log("正在拨号")
        try:
            # handle is a pid, for disconnect or showipadrress, if connect success return 0.
            # account is the username that your ISP supposed, passwd is the password.
            handle, result = self.connect_pppoe(dialname, account, passwd)
            if result == 0:
                self.print_log("拨号成功")
                self.pppoeStatusLbl.setText("拨号成功")
                return handle, result
            else:
                if self.stopPPPOEFlag:
                    self.print_log("拨号失败")
                    self.pppoeStatusLbl.setText("拨号失败")
                    return -1, -1
                else:
                    self.print_log("拨号失败，3秒后重试")
                    self.pppoeStatusLbl.setText("正在重试")
                    sleep(3)
                    return self.dial_broadband()
        except Exception as e:
            self.print_log("拨号异常" + str(e))
            return -1, -1

    def disconnect_pppoe(self, handle):
        self.print_log("正在断开宽带!")
        self.pppoeStatusLbl.setText("正在断开")
        if handle is not None:
            try:
                win32ras.HangUp(handle)
                self.print_log("宽带断开成功!")
                self.pppoeStatusLbl.setText("断开成功")
                return "success"
            except Exception as e:
                self.print_log("宽带断开失败，3秒后重试")
                self.pppoeStatusLbl.setText("断开失败")
                sleep(3)
                return self.disconnect_pppoe(handle)
        else:
            self.print_log("宽带断开异常")
            self.pppoeStatusLbl.setText("断开失败")
            return "fail"

    def check_for_broadband(self):
        connections = win32ras.EnumConnections()
        if len(connections) == 0:
            self.print_log("系统未运行任何宽带连接")
            return
        else:
            self.print_log("系统正在运行%d个宽带连接" % len(connections))
            return connections

    def show_ip_address(self):
        self.print_log("正在查询IP")
        self.pppoeIpLbl.setText("")

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

        if ip_str is not None:
            self.print_log("IP地址为： " + ip_str)
            self.pppoeIpLbl.setText(ip_str)
        pass


class InitConfigTask(QRunnable):
    def __init__(self, window):
        super(InitConfigTask, self).__init__()
        self.window = window
        pass

    def run(self):
        try:
            with open(os.path.abspath('config.ini'), 'r', encoding='utf-8') as f:
                configJson = f.read()
                configDic = json.loads(configJson)
                self.window.startTimeEdit.setText(configDic["startTime"])
                self.window.endTimeEdit.setText(configDic["endTime"])
                self.window.pauseTimeFromEdit.setText(configDic["pauseTimeFrom"])
                self.window.pauseTimeToEdit.setText(configDic["pauseTimeTo"])
                self.window.slipTimesFromEdit.setText(configDic["slipTimesFrom"])
                self.window.slipTimesToEdit.setText(configDic["slipTimesTo"])
                self.window.pxFromEdit.setText(configDic["pxFrom"])
                self.window.pxToEdit.setText(configDic["pxTo"])
                self.window.chromeLocationEdit.setText(configDic["chromeLocation"])
                f.close()
        except Exception as e:
            print(e)
        pass


class DriverThread(QThread):
    trigger = pyqtSignal()

    def __init__(self, window):
        super(DriverThread, self).__init__()
        self.window = window
        pass

    def run(self):
        # 获取下一篇文章
        url = ""
        try:
            with open(os.path.abspath('unread.txt'), 'r', encoding='utf-8') as f:  # 打开文件
                lines = f.readlines()  # 读取所有行
                lth = len(lines)
                if lth > 0:
                    url = lines[0]  # 取第一行
                    self.window.setUnReadNum(lth - 1)
                else:
                    self.window.setUnReadNum(0)
                f.close()
        except Exception as e:
            pass

        self.window.build_driver(url)
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


class PPPOETask(QThread):
    trigger = pyqtSignal()

    def __init__(self, window):
        super(PPPOETask, self).__init__()
        self.window = window
        pass

    def run(self):
        try:
            self.window.build_pppoe()
            self.trigger.emit()
        except Exception as e:
            self.window.print_log(str(e))
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CaesarReaderWindow()
    win.show()
    sys.exit(app.exec_())
