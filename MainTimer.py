import time
import sys
from pyTwistyScrambler import scrambler333 as pyt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import  QApplication, QMainWindow, QMenu, QAction, QActionGroup
from PyQt5.QtGui import QFont, QKeyEvent
from PyQt5.QtCore import QRect, Qt

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
WIN_HEIGHT = SCREEN_HEIGHT*.8
WIN_WIDTH = SCREEN_WIDTH/2

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0, WIN_WIDTH, WIN_HEIGHT)
        self.setWindowTitle('Timer')
        self.group = QActionGroup(self)
        self.menu = QMenu("Background Colors", self)
        self.isBackgroundBlue = self.group.addAction(QAction('Blue', self.menu, checkable=True))
        self.isBackgroundTeal = self.group.addAction(QAction('Teal', self.menu, checkable=True))
        self.isBackgroundGrey = self.group.addAction(QAction('Grey', self.menu, checkable=True))
        self.isBackgroundDefault = self.group.addAction(QAction('Default', self.menu, checkable=True))
        self.isBackgroundDefault.setChecked(True)
        self.menu.addAction(self.isBackgroundBlue)
        self.menu.addAction(self.isBackgroundTeal)
        self.menu.addAction(self.isBackgroundGrey)
        self.menu.addAction(self.isBackgroundDefault)

        #timerlabel
        self.timerLabel = QtWidgets.QLabel(self)
        timerFont = QtGui.QFont('DS-Digital', 30)
        timerGeometry = QRect(WIN_WIDTH/2 - 130,WIN_HEIGHT/2 - 35, 260, 70)
        self.timerLabel.setGeometry(timerGeometry)
        self.timerLabel.setAlignment(Qt.AlignCenter)
        # timerLabel.setStyleSheet("border: 1px solid black;")
        self.timerLabel.setFont(timerFont)
        self.timerLabel.setText('00:00')
        
        #scramble label
        scrambleLabel = QtWidgets.QLabel(self)
        scrambleFont = QtGui.QFont('Open Sans', 20)
        scrambleGeometry = QRect(0,0,WIN_WIDTH, 90)
        scrambleLabel.setGeometry(scrambleGeometry)
        scrambleLabel.setAlignment(Qt.AlignCenter )
        scrambleLabel.setFont(scrambleFont)
        scrambleLabel.setText(pyt.get_WCA_scramble())

        #scramble button
        scrambleButton = QtWidgets.QPushButton(self)
        scrambleButtonFont = QFont('Open Sans', 10)
        scrambleButton.setFont(scrambleButtonFont)
        scrambleButton.setText('New Scramble')
        scrambleButtonGeometry = QRect(WIN_WIDTH/2-65, 80, 130,35)
        scrambleButton.setGeometry(scrambleButtonGeometry)
        scrambleButton.clicked.connect(lambda: scrambleLabel.setText(pyt.get_WCA_scramble()))
        #-----------------------------------------------#
        self.menuBar().addMenu(self.menu)
        self.show()
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_0:
            timeis = time.struct_time()  
            while count< 1000:
                self.timerLabel.setText(timeis)
                count += 1000

    
    # print(self.isBackgroundDefault.isChecked())
    
    
def main():
    app = QApplication(sys.argv)
    win = App()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()