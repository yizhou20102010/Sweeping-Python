# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MineFrame.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from QmyPushButton import QmyPushButton
import  random

class Ui_Form(object):
    gamebegin=QtCore.pyqtSignal()
    gameover=QtCore.pyqtSignal(int)
    mineflag=QtCore.pyqtSignal(int)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.mygridlayout = QtWidgets.QGridLayout(Form)
        self.mygridlayout.setContentsMargins(0, 0, 0, 0)
        self.mygridlayout.setSpacing(0)

        self.isFirstPress = True
        self.showbtnnum = 0

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def ShowMineFrame(self, rnum, cnum, mine):
        self.rownum=rnum
        self.colnum=cnum
        self.minenum=mine
        self.pbtnlist=[];
        for i in range(0, rnum):
            for j in range(0,cnum):
                btn = QmyPushButton()
                btn.data=0
                btn.state=0
                self.pbtnlist.append(btn)

        for i in range(0,rnum):
            for j in range(0,cnum):
                btn = self.pbtnlist[i*cnum+j]
                btn.setMaximumSize(32,32)
                btn.setMinimumSize(32, 32)
                self.mygridlayout.addWidget(btn, i, j)
                btn.mouseLeftPressPos.connect(self.onMouseLeftPress)
                btn.mouseRightPressPos.connect(self.onMouseRightPress)

        self.randomGen()

    def randomGen(self):
        k=0
        while k<self.minenum:
            row=random.randrange(0, self.rownum)
            col=random.randrange(0, self.colnum)
            if self.pbtnlist[row*self.colnum+col].data!=-1:
                self.pbtnlist[row*self.colnum+col].data=-1
                k=k+1
                for i0 in [row-1, row, row+1]:
                    for j0 in [col-1, col, col+1]:
                        if i0>=0 and i0<self.rownum and j0>=0 and j0<self.colnum :
                            index = i0 * self.colnum + j0
                            if self.pbtnlist[index].data!=-1:
                                self.pbtnlist[index].data=self.pbtnlist[index].data+1

        # for i in range(0, len(self.pbtnlist)):
        #     self.pbtnlist[i].setText("%d"%self.pbtnlist[i].data)


    def onMouseLeftPress(self,pos):
        if self.isFirstPress:
            self.isFirstPress=False
            self.gamebegin.emit()

        index=int(pos.y()/32*self.colnum + pos.x()/32)
        if index >=len(self.pbtnlist):
            return
        btn=self.pbtnlist[index]
        if btn.data == -1:
            btn.state=-2
            btn.buttonshow()
            for i in range(0, len(self.pbtnlist)):
                btn=self.pbtnlist[i];
                if btn.data == -1:
                    btn.state = -2
                    btn.buttonshow()
            self.gameover.emit(-1)
        elif btn.state !=-1:
            self.showblankround(index)
            if self.rownum*self.colnum - self.showbtnnum == self.minenum:
                self.gameover.emit(1)


    def onMouseRightPress(self, pos):
        if self.isFirstPress:
            self.isFirstPress=False
            self.gamebegin.emit()

        index=int(pos.y()/32*self.colnum+pos.x()/32)
        if index >= len(self.pbtnlist):
            return
        btn=self.pbtnlist[index]
        if btn.state!=-1 and btn.state!=-2:
            if btn.state ==1:
                self.mineflag.emit(1)
            btn.state=(btn.state+1)%3
            btn.buttonshow()
            if btn.state == 1:
                self.mineflag.emit(-1)


    def showblankround(self, index):
        if index<0 or index>len(self.pbtnlist)-1:
            return
        btn=self.pbtnlist[index]
        if btn.data == -1 or btn.state == -1:
            return
        self.showbtnnum=self.showbtnnum+1
        btn.state=-1
        btn.buttonshow()
        if btn.data !=0:
            btn.setText("%d" % btn.data)
            return
        elif btn.data == 0 :
            row=int(index/self.colnum)
            col=index%self.colnum
            print(index, self.rownum, self.colnum)
            print("row: ",row,end=" ")
            print(col)
            for i0 in [row - 1, row, row + 1]:
                for j0 in [col - 1, col, col + 1]:
                    if i0 >= 0 and i0 < self.rownum and j0 >= 0 and j0 < self.colnum:
                        self.showblankround(i0*self.colnum+j0)

