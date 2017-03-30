from PyQt5 import QtCore, QtGui, QtWidgets

class QmyPushButton(QtWidgets.QPushButton):
    mouseLeftPressPos = QtCore.pyqtSignal(QtCore.QPoint)
    mouseRightPressPos = QtCore.pyqtSignal(QtCore.QPoint)
    def __init__(self, parent=None):
        super(QmyPushButton, self).__init__(parent)
        self.state = 0;
        self.data = 0;
        self.setStyleSheet("QPushButton{background-image: url(:/image/figure/back0.ico); \
                                       border-style:outset;border: 1px groove gray;border-radius: 1px;}"
                                    "QPushButton:hover{background-image: url(:/image/figure/back1.ico)}");


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mouseLeftPressPos.emit(self.pos())
        elif event.button() == QtCore.Qt.RightButton:
            self.mouseRightPressPos.emit(self.pos())

    def buttonshow(self):
        if self.state == -2:
            self.setStyleSheet("QPushButton{background-image: url(:/image/figure/mine.ico); border-style:inset;\
                                                            border: 1px groove gray; font-size:18px; font-family: Arial}")
        elif self.state ==-1:
            self.setStyleSheet("QPushButton{background-image: url(:/image/figure/back.ico); border-style:inset;\
                                                            border: 1px groove gray; font-size:18px; font-family: Arial}")
        elif self.state ==0:
            self.setStyleSheet("QPushButton{background-image: url(:/image/figure/back0.ico); \
                                           border-style:outset;border: 1px groove gray;border-radius: 1px;}"
                                        "QPushButton:hover{background-image: url(:/image/figure/back1.ico)}")
        elif self.state == 1:
            self.setStyleSheet("QPushButton{background-image: url(:/image/figure/flag0.ico); \
                    border-style:outset;border: 1px groove gray;border-radius: 1px;}"
                    "QPushButton:hover{background-image: url(:/image/figure/flag1.ico)}")
        elif self.state == 2:
            self.setStyleSheet("QPushButton{background-image: url(:/image/figure/question0.ico); \
                           border-style:outset;border: 1px groove gray;border-radius: 1px;}"
                          "QPushButton:hover{background-image: url(:/image/figure/question1.ico)}")


