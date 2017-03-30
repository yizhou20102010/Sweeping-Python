from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import MainWindow
from MineFrame import MineFrame
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    # mainWindow = MineFrame();
    mainWindow.show()
    sys.exit(app.exec_())