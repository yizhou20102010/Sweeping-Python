from PyQt5 import QtCore, QtGui, QtWidgets
from ui_MineFrame import Ui_Form


class MineFrame(QtWidgets.QWidget,Ui_Form):
    def __init__(self, parent= None):
        super(MineFrame, self).__init__(parent)
        self.setupUi(self)





