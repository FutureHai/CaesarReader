# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_myMainWindow(object):
    def setupUi(self, myMainWindow):
        myMainWindow.setObjectName("myMainWindow")
        myMainWindow.resize(800, 600)
        myMainWindow.setMinimumSize(QtCore.QSize(800, 600))
        myMainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        myMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(myMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 380))
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 380))
        self.tabWidget.setMaximumSize(QtCore.QSize(500, 380))
        self.tabWidget.setObjectName("tabWidget")
        self.logTab = QtWidgets.QWidget()
        self.logTab.setObjectName("logTab")
        self.logTxtBr = QtWidgets.QTextBrowser(self.logTab)
        self.logTxtBr.setGeometry(QtCore.QRect(0, 0, 500, 352))
        self.logTxtBr.setMinimumSize(QtCore.QSize(500, 352))
        self.logTxtBr.setMaximumSize(QtCore.QSize(500, 352))
        self.logTxtBr.setLineWidth(1)
        self.logTxtBr.setObjectName("logTxtBr")
        self.tabWidget.addTab(self.logTab, "")
        self.linkTab = QtWidgets.QWidget()
        self.linkTab.setObjectName("linkTab")
        self.linkTxtBr = QtWidgets.QTextBrowser(self.linkTab)
        self.linkTxtBr.setGeometry(QtCore.QRect(0, 0, 500, 352))
        self.linkTxtBr.setMinimumSize(QtCore.QSize(500, 352))
        self.linkTxtBr.setMaximumSize(QtCore.QSize(500, 352))
        self.linkTxtBr.setObjectName("linkTxtBr")
        self.tabWidget.addTab(self.linkTab, "")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(499, 22, 4, 550))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.configGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.configGBox.setGeometry(QtCore.QRect(503, 15, 295, 555))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.configGBox.setFont(font)
        self.configGBox.setAlignment(QtCore.Qt.AlignCenter)
        self.configGBox.setObjectName("configGBox")
        self.label = QtWidgets.QLabel(self.configGBox)
        self.label.setGeometry(QtCore.QRect(0, 40, 110, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.startTimeEdit = QtWidgets.QLineEdit(self.configGBox)
        self.startTimeEdit.setGeometry(QtCore.QRect(115, 40, 35, 21))
        self.startTimeEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startTimeEdit.setObjectName("startTimeEdit")
        self.label_2 = QtWidgets.QLabel(self.configGBox)
        self.label_2.setGeometry(QtCore.QRect(160, 40, 40, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.configGBox)
        self.label_3.setGeometry(QtCore.QRect(240, 40, 50, 21))
        self.label_3.setObjectName("label_3")
        self.endTimeEdit = QtWidgets.QLineEdit(self.configGBox)
        self.endTimeEdit.setGeometry(QtCore.QRect(200, 40, 35, 21))
        self.endTimeEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endTimeEdit.setObjectName("endTimeEdit")
        self.label_4 = QtWidgets.QLabel(self.configGBox)
        self.label_4.setGeometry(QtCore.QRect(0, 70, 110, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.pauseTimeFromEdit = QtWidgets.QLineEdit(self.configGBox)
        self.pauseTimeFromEdit.setGeometry(QtCore.QRect(115, 70, 35, 21))
        self.pauseTimeFromEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pauseTimeFromEdit.setObjectName("pauseTimeFromEdit")
        self.label_5 = QtWidgets.QLabel(self.configGBox)
        self.label_5.setGeometry(QtCore.QRect(160, 70, 40, 21))
        self.label_5.setObjectName("label_5")
        self.pauseTimeToEdit = QtWidgets.QLineEdit(self.configGBox)
        self.pauseTimeToEdit.setGeometry(QtCore.QRect(200, 70, 35, 21))
        self.pauseTimeToEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pauseTimeToEdit.setObjectName("pauseTimeToEdit")
        self.label_6 = QtWidgets.QLabel(self.configGBox)
        self.label_6.setGeometry(QtCore.QRect(240, 70, 50, 21))
        self.label_6.setObjectName("label_6")
        self.slipTimesFromEdit = QtWidgets.QLineEdit(self.configGBox)
        self.slipTimesFromEdit.setGeometry(QtCore.QRect(115, 100, 35, 21))
        self.slipTimesFromEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.slipTimesFromEdit.setObjectName("slipTimesFromEdit")
        self.label_7 = QtWidgets.QLabel(self.configGBox)
        self.label_7.setGeometry(QtCore.QRect(0, 100, 110, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.configGBox)
        self.label_8.setGeometry(QtCore.QRect(240, 100, 50, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.configGBox)
        self.label_9.setGeometry(QtCore.QRect(160, 100, 40, 21))
        self.label_9.setObjectName("label_9")
        self.slipTimesToEdit = QtWidgets.QLineEdit(self.configGBox)
        self.slipTimesToEdit.setGeometry(QtCore.QRect(200, 100, 35, 21))
        self.slipTimesToEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.slipTimesToEdit.setObjectName("slipTimesToEdit")
        self.label_10 = QtWidgets.QLabel(self.configGBox)
        self.label_10.setGeometry(QtCore.QRect(20, 160, 110, 21))
        self.label_10.setObjectName("label_10")
        self.chromeLocationEdit = QtWidgets.QLineEdit(self.configGBox)
        self.chromeLocationEdit.setGeometry(QtCore.QRect(20, 180, 251, 21))
        self.chromeLocationEdit.setObjectName("chromeLocationEdit")
        self.saveConfigBtn = QtWidgets.QPushButton(self.configGBox)
        self.saveConfigBtn.setGeometry(QtCore.QRect(180, 220, 93, 28))
        self.saveConfigBtn.setObjectName("saveConfigBtn")
        self.startReadBtn = QtWidgets.QPushButton(self.configGBox)
        self.startReadBtn.setGeometry(QtCore.QRect(20, 500, 93, 28))
        self.startReadBtn.setObjectName("startReadBtn")
        self.stopReadBtn = QtWidgets.QPushButton(self.configGBox)
        self.stopReadBtn.setGeometry(QtCore.QRect(180, 500, 93, 28))
        self.stopReadBtn.setObjectName("stopReadBtn")
        self.addContentBtn = QtWidgets.QPushButton(self.configGBox)
        self.addContentBtn.setGeometry(QtCore.QRect(20, 450, 93, 28))
        self.addContentBtn.setObjectName("addContentBtn")
        self.label_11 = QtWidgets.QLabel(self.configGBox)
        self.label_11.setGeometry(QtCore.QRect(20, 350, 261, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.configGBox)
        self.label_12.setGeometry(QtCore.QRect(65, 380, 141, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.configGBox)
        self.label_13.setGeometry(QtCore.QRect(240, 130, 50, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.configGBox)
        self.label_14.setGeometry(QtCore.QRect(160, 130, 40, 21))
        self.label_14.setObjectName("label_14")
        self.pxToEdit = QtWidgets.QLineEdit(self.configGBox)
        self.pxToEdit.setGeometry(QtCore.QRect(200, 130, 35, 21))
        self.pxToEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pxToEdit.setObjectName("pxToEdit")
        self.pxFromEdit = QtWidgets.QLineEdit(self.configGBox)
        self.pxFromEdit.setGeometry(QtCore.QRect(115, 130, 35, 21))
        self.pxFromEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pxFromEdit.setObjectName("pxFromEdit")
        self.label_17 = QtWidgets.QLabel(self.configGBox)
        self.label_17.setGeometry(QtCore.QRect(0, 130, 110, 21))
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 570, 800, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pppoeGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.pppoeGBox.setGeometry(QtCore.QRect(0, 385, 498, 184))
        self.pppoeGBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pppoeGBox.setObjectName("pppoeGBox")
        self.accountLbl = QtWidgets.QLabel(self.pppoeGBox)
        self.accountLbl.setGeometry(QtCore.QRect(30, 50, 75, 22))
        self.accountLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.accountLbl.setObjectName("accountLbl")
        self.passwordLbl = QtWidgets.QLabel(self.pppoeGBox)
        self.passwordLbl.setGeometry(QtCore.QRect(30, 80, 75, 22))
        self.passwordLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passwordLbl.setObjectName("passwordLbl")
        self.accountEdit = QtWidgets.QLineEdit(self.pppoeGBox)
        self.accountEdit.setGeometry(QtCore.QRect(110, 50, 120, 22))
        self.accountEdit.setObjectName("accountEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.pppoeGBox)
        self.passwordEdit.setGeometry(QtCore.QRect(110, 80, 120, 22))
        self.passwordEdit.setObjectName("passwordEdit")
        self.label_15 = QtWidgets.QLabel(self.pppoeGBox)
        self.label_15.setGeometry(QtCore.QRect(250, 50, 75, 22))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.pppoeGBox)
        self.label_16.setGeometry(QtCore.QRect(250, 80, 75, 22))
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.pppoeStatusLbl = QtWidgets.QLabel(self.pppoeGBox)
        self.pppoeStatusLbl.setGeometry(QtCore.QRect(330, 50, 120, 22))
        self.pppoeStatusLbl.setText("")
        self.pppoeStatusLbl.setObjectName("pppoeStatusLbl")
        self.pppoeIpLbl = QtWidgets.QLabel(self.pppoeGBox)
        self.pppoeIpLbl.setGeometry(QtCore.QRect(330, 80, 120, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pppoeIpLbl.setPalette(palette)
        self.pppoeIpLbl.setText("")
        self.pppoeIpLbl.setObjectName("pppoeIpLbl")
        self.connectPppoeBtn = QtWidgets.QPushButton(self.pppoeGBox)
        self.connectPppoeBtn.setGeometry(QtCore.QRect(30, 130, 93, 28))
        self.connectPppoeBtn.setObjectName("connectPppoeBtn")
        self.disconnectPppoeBtn = QtWidgets.QPushButton(self.pppoeGBox)
        self.disconnectPppoeBtn.setGeometry(QtCore.QRect(140, 130, 93, 28))
        self.disconnectPppoeBtn.setObjectName("disconnectPppoeBtn")
        myMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(myMainWindow)
        self.statusbar.setObjectName("statusbar")
        myMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(myMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(myMainWindow)

    def retranslateUi(self, myMainWindow):
        _translate = QtCore.QCoreApplication.translate
        myMainWindow.setWindowTitle(_translate("myMainWindow", "CReader"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logTab), _translate("myMainWindow", "日志"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.linkTab), _translate("myMainWindow", "链接"))
        self.configGBox.setTitle(_translate("myMainWindow", "全局配置"))
        self.label.setText(_translate("myMainWindow", "只在"))
        self.label_2.setText(_translate("myMainWindow", "点 -"))
        self.label_3.setText(_translate("myMainWindow", "点运行"))
        self.label_4.setText(_translate("myMainWindow", "浏览后停顿时间"))
        self.label_5.setText(_translate("myMainWindow", "秒 -"))
        self.label_6.setText(_translate("myMainWindow", "秒"))
        self.label_7.setText(_translate("myMainWindow", "设置下滑次数"))
        self.label_8.setText(_translate("myMainWindow", "次"))
        self.label_9.setText(_translate("myMainWindow", "次 -"))
        self.label_10.setText(_translate("myMainWindow", "谷歌启动路径："))
        self.saveConfigBtn.setText(_translate("myMainWindow", "保存设置"))
        self.startReadBtn.setText(_translate("myMainWindow", "载入连接"))
        self.stopReadBtn.setText(_translate("myMainWindow", "停止任务"))
        self.addContentBtn.setText(_translate("myMainWindow", "新增内容"))
        self.label_11.setText(_translate("myMainWindow", "注意：不要直接关闭浏览器，请使用"))
        self.label_12.setText(_translate("myMainWindow", "“停止任务”按钮"))
        self.label_13.setText(_translate("myMainWindow", "px"))
        self.label_14.setText(_translate("myMainWindow", "px -"))
        self.label_17.setText(_translate("myMainWindow", "设置下滑像素"))
        self.pppoeGBox.setTitle(_translate("myMainWindow", "拨号设置"))
        self.accountLbl.setText(_translate("myMainWindow", "连接账号："))
        self.passwordLbl.setText(_translate("myMainWindow", "连接密码："))
        self.label_15.setText(_translate("myMainWindow", "当前状态："))
        self.label_16.setText(_translate("myMainWindow", "当前IP："))
        self.connectPppoeBtn.setText(_translate("myMainWindow", "开始拨号"))
        self.disconnectPppoeBtn.setText(_translate("myMainWindow", "断开连接"))
