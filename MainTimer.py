from pyTwistyScrambler import scrambler333 as pyt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import  QApplication, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, Qt  
import sys

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
WIN_HEIGHT = SCREEN_HEIGHT*.8
WIN_WIDTH = SCREEN_WIDTH/2
isScrambleFirst = True



def App():

    def newScramble():
        return pyt.get_WCA_scramble()
    #setup
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0,0, WIN_WIDTH, WIN_HEIGHT)
    win.setWindowTitle("Timer")

    #timerlabel
    timerLabel = QtWidgets.QLabel(win)
    timerFont = QtGui.QFont('DS-Digital', 30)
    timerGeometry = QRect(WIN_WIDTH/2 - 130,WIN_HEIGHT/2 - 35, 260, 70)
    timerLabel.setGeometry(timerGeometry)
    timerLabel.setAlignment(Qt.AlignCenter)
    # timerLabel.setStyleSheet("border: 1px solid black;")
    timerLabel.setFont(timerFont)
    timerLabel.setText('00:00')

    #newscramble label
    scrambleLabel = QtWidgets.QLabel(win)
    scrambleFont = QtGui.QFont('Open Sans', 20)
    scrambleGeometry = QRect(0,0,WIN_WIDTH, 70)
    scrambleLabel.setGeometry(scrambleGeometry)
    scrambleLabel.setAlignment(Qt.AlignCenter )
    scrambleLabel.setFont(scrambleFont)
    scrambleLabel.setText(newScramble())

    #new scramble button
    scrambleButton = QtWidgets.QPushButton(win)
    scrambleButtonFont = QFont('Open Sans', 10)
    scrambleButton.setFont(scrambleButtonFont)
    scrambleButton.setText('New Scramble')
    scrambleButtonGeometry = QRect(WIN_WIDTH/2-65, 60, 130,35)
    scrambleButton.setGeometry(scrambleButtonGeometry)
    scrambleButton.clicked.connect(lambda: scrambleLabel.setText(pyt.get_WCA_scramble()))


    win.show()
    sys.exit(app.exec_())
App()