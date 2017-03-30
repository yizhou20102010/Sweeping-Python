# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MineFrame import MineFrame

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 434)
        self.mainwindow=MainWindow
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/figure/timg.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.MineWidget = QtWidgets.QWidget(self.centralWidget)
        self.MineWidget.setGeometry(QtCore.QRect(10, 100, 261, 261))
        self.phlayout = QtWidgets.QHBoxLayout()
        self.MineWidget.setLayout(self.phlayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MineWidget.sizePolicy().hasHeightForWidth())
        self.MineWidget.setSizePolicy(sizePolicy)
        self.MineWidget.setObjectName("MineWidget")

        self.LCDWidget = QtWidgets.QWidget(self.centralWidget)
        self.LCDWidget.setGeometry(QtCore.QRect(150, 10, 120, 41))
        self.LCDWidget.setObjectName("LCDWidget")
        self.plcdlayerout = QtWidgets.QHBoxLayout()
        self.m_timenumber = QtWidgets.QLineEdit()
        self.plcdlayerout.addWidget(self.m_timenumber)
        self.plcdlayerout.setContentsMargins(0,0,0,0)
        self.plcdlayerout.setSpacing(0)
        self.LCDWidget.setLayout(self.plcdlayerout)

        self.NumWidget = QtWidgets.QWidget(self.centralWidget)
        self.NumWidget.setGeometry(QtCore.QRect(10, 10, 120, 41))
        self.NumWidget.setObjectName("NumWidget")
        self.m_minenumber = QtWidgets.QLineEdit()
        self.pnumlayerout = QtWidgets.QHBoxLayout()
        self.pnumlayerout.addWidget(self.m_minenumber)
        self.pnumlayerout.setContentsMargins(0,0,0,0)
        self.pnumlayerout.setSpacing(0)
        self.NumWidget.setLayout(self.pnumlayerout)
        # self.m_minenumber.clicked.connect(self.onbuttonclicked)

        # self.phlayout = QtWidgets.QHBoxLayout()
        # self.pframe = MineFrame()
        # self.phlayout.addWidget(self.pframe)
        # self.MineWidget.setLayout(self.phlayout)
        self.pframe=None
        self.pframe = MineFrame()
        self.phlayout.addWidget(self.pframe)

        self.pframe.gamebegin.connect(self.onGameBegin)
        self.pframe.gameover.connect(self.onGameOver)
        self.pframe.mineflag.connect(self.onMineFlag)
        self.showFrame(9, 9, 10)
        # print(self.rownum)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 311, 26))
        self.menuBar.setObjectName("menuBar")
        self.game = QtWidgets.QMenu(self.menuBar)
        self.game.setObjectName("game")
        self.menuD = QtWidgets.QMenu(self.menuBar)
        self.menuD.setObjectName("menuD")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_NewGame = QtWidgets.QAction(MainWindow)
        self.action_NewGame.setObjectName("action_NewGame")
        self.action_Option = QtWidgets.QAction(MainWindow)
        self.action_Option.setObjectName("action_Option")
        self.game.addAction(self.action_NewGame)
        self.game.addSeparator()
        self.game.addAction(self.action_Option)
        self.menuBar.addAction(self.game.menuAction())
        self.menuBar.addAction(self.menuD.menuAction())
        self.action_NewGame.triggered.connect(self.onNewGame)
        self.action_Option.triggered.connect(self.onGameOption)

        self.timercount=0
        self.m_timer=QtCore.QTimer()
        self.m_timer.timeout.connect(self.onTimerDonw)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "扫雷"))
        self.game.setTitle(_translate("MainWindow", "游戏(&G)"))
        self.menuD.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.action_NewGame.setText(_translate("MainWindow", "新游戏(&N)"))
        self.action_Option.setText(_translate("MainWindow", "选项(&O)"))

    def showFrame(self, rnum, cnum, mnum):
        self.rownum=rnum
        self.colnum = cnum
        self.minenum = mnum

        self.timercount=0
        self.remainminenum=self.minenum

        self.mainwindow.setFixedSize(cnum*32+40, rnum*32+150)
        self.m_timenumber.setReadOnly(True);
        self.m_timenumber.setText("0");
        self.m_timenumber.setAlignment(QtCore.Qt.AlignCenter)
        mrect=self.mainwindow.geometry()
        self.LCDWidget.setGeometry(mrect.width()-84,20,64,32)

        self.m_minenumber.setReadOnly(True)
        self.m_minenumber.setText("%d"% mnum)
        self.m_minenumber.setAlignment(QtCore.Qt.AlignCenter)
        self.NumWidget.setGeometry(20,20,64,32)

        self.MineWidget.setGeometry(20,80, self.colnum*32, self.rownum*32)
        self.phlayout.setContentsMargins(0,0,0,0)
        self.phlayout.setSpacing(0)

        self.pframe.ShowMineFrame(self.rownum, self.colnum, self.minenum)

    def onGameBegin(self):
        self.m_timer.start(1000)

    def onGameOver(self, flag):
        self.m_timer.stop()
        titlestr=""
        if flag ==-1:
            titlestr="游戏失败"
        else:
            titlestr="游戏成功"
        tipstr="请重新开局(YES)或离开(No)"
        rb = QtWidgets.QMessageBox.information(self, titlestr, tipstr, QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        if rb ==QtWidgets.QMessageBox.Yes:
            self.showFrame(self.rownum, self.colnum, self.minenum)
        else:
            self.close()

    def onMineFlag(self, remark):
        print("mineflag: ", end="")
        self.remainminenum = self.remainminenum+remark
        if self.remainminenum<0:
            self.remainminenum=0
        elif self.remainminenum>self.minenum:
            self.remainminenum=self.minenum
        self.m_minenumber.setText("%d"%self.remainminenum)

    def onNewGame(self):
        self.showFrame(self.rownum, self.colnum, self.minenum)
    def onGameOption(self):
        liststr=["初级", "中级", "高级"]
        itemstr,ok0=QtWidgets.QInputDialog.getItem(self, "Option", "等级选择", liststr, 0, False);
        if itemstr == "初级":
            self.showFrame(9,9,10)
        elif itemstr == "中级":
            self.showFrame(16,16,40)
        elif itemstr == "高级":
            self.showFrame(16,30,99)
        else:
            self.showFrame(self.rownum, self.colnum, self.minenum)

    def onbuttonclicked(self):
        print("clicked")
    def onTimerDonw(self):
        self.timercount=self.timercount+1
        self.m_timenumber.setText("%d"%self.timercount)
import resource_rc
