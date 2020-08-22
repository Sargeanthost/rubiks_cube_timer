###Not in use
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.timerLabel = QtWidgets.QLabel(self.centralwidget)
        self.timerLabel.setGeometry(QtCore.QRect(270, 210, 221, 61))

        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(30)
        self.timerLabel.setFont(font)

        self.timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timerLabel.setObjectName("timerLabel")

        self.startStopButton = QtWidgets.QPushButton(self.centralwidget)
        self.startStopButton.setGeometry(QtCore.QRect(250, 370, 260, 70))

        font = QtGui.QFont()
        font.setPointSize(20)
        self.startStopButton.setFont(font)
        self.startStopButton.setObjectName("startStopButton")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.timerLabel.setText(_translate("MainWindow", "00:00"))
        self.startStopButton.setText(_translate("MainWindow", "Press"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
