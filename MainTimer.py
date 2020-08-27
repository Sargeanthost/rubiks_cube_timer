import sys
from datetime import *
from math import floor
from pyTwistyScrambler import scrambler333 as pyt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# TODO Make background color changer themes and not colors, then make 
# TODO cont- backgroundColor call those defs that set background
# TODO make timer show on timer label

# prevent button from clicking due to keyboard input
# https://stackoverflow.com/questions/63540492/how-to-stop-spacebar-from-triggering-a-focused-qpushbutton-in-pyqt5/63540920?noredirect=1#comment112359195_63540920
class Listener(QtCore.QObject):
    def __init__(self, button):
        super().__init__(button)
        self._button = button
        self.button.installEventFilter(self)

    @property
    def button(self):
        return self._button

    def eventFilter(self, obj, event):
        if obj is self.button and event.type() == QtCore.QEvent.KeyPress:
            return True
        return super().eventFilter(obj, event)


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        left = 1920 / 2 - (900 / 2)
        top = 1080 / 2 - (900 / 2)
        width = 900
        height = 900

        self.setGeometry(left, top, width, height)
        self.setWindowTitle("Timer")

        self.setStyleSheet(
            """
                    App {
                        background-color: rgb(240,240,240)
                    }
                    QPushButton {
                        background-color: rgb(240,240,240);
                        border-style: solid;
                        border-width: 1px;
                        border-color: black;
                    }
                """
        )

        self.initUI()

    def initUI(self):
        self.isCounting = False
        self.timeNow = datetime.now()

        self.group = QActionGroup(self)
        self.menu = QMenu("Background Colors", self)
        self.isBackgroundBlue = self.group.addAction(
            QAction("Blue", self.menu, checkable=True)
        )
        self.isBackgroundTeal = self.group.addAction(
            QAction("Teal", self.menu, checkable=True)
        )
        self.isBackgroundGrey = self.group.addAction(
            QAction("Grey", self.menu, checkable=True)
        )
        self.isBackgroundDefault = self.group.addAction(
            QAction("Off White", self.menu, checkable=True)
        )
        self.isBackgroundDefault.setChecked(True)
        self.menu.addAction(self.isBackgroundBlue)
        self.menu.addAction(self.isBackgroundTeal)
        self.menu.addAction(self.isBackgroundGrey)
        self.menu.addAction(self.isBackgroundDefault)

        # timerlabel
        self.timerLabel = QLabel(self)
        timerFont = QFont("DS-Digital", 30)
        timerGeometry = QRect(320, 400, 260, 70)
        self.timerLabel.setGeometry(timerGeometry)
        self.timerLabel.setAlignment(Qt.AlignCenter)
        # timerLabel.setStyleSheet("border: 1px solid black;")
        self.timerLabel.setFont(timerFont)
        self.timerLabel.setText("00:00")

        # scramble label
        scrambleLabel = QLabel(self)
        scrambleFont = QFont("Open Sans", 20)
        scrambleGeometry = QRect(0, 0, 900, 90)
        scrambleLabel.setGeometry(scrambleGeometry)
        scrambleLabel.setAlignment(Qt.AlignCenter)
        scrambleLabel.setFont(scrambleFont)
        scrambleLabel.setText(pyt.get_WCA_scramble())

        # scramble button
        scrambleButton = QPushButton(self)
        scrambleButtonFont = QFont("Open Sans", 10)
        scrambleButton.setFont(scrambleButtonFont)
        scrambleButton.setText("New Scramble")
        scrambleButtonGeometry = QRect(385, 80, 130, 35)
        scrambleButton.setGeometry(scrambleButtonGeometry)
        scrambleButton.clicked.connect(
            lambda: scrambleLabel.setText(pyt.get_WCA_scramble())
        )
        listener = Listener(scrambleButton)

        # shortcuts and events
        spaceKey = QShortcut(Qt.Key_Space, self, autoRepeat=False)
        spaceKey.activated.connect(self.processTime)
        # -----------------------------------------------#
        self.menu.triggered.connect(self.backgroundColor)
        self.menuBar().addMenu(self.menu)
        self.show()

    # timer --only for creating time object -- will merge into one later
    def processTime(self):
        self.isCounting = not self.isCounting
        if self.isCounting == True:
            self.timeNow = datetime.now()
        else:
            self.elapsedTime = datetime.now() - self.timeNow

            totalSeconds = float("{:.2f}".format(self.elapsedTime.total_seconds()))

            minutes = str(floor(totalSeconds / 60))
            seconds = str(totalSeconds)
            mils = "{:.2f}".format(totalSeconds % 1)

            time = [minutes, seconds[:-3], mils[2:]]
            print("Time elapsed is:", ":".join(time))

    # background color setter
    def backgroundColor(self):
        for action in self.menu.actions():
            if action.isChecked() and action.text() == "Blue":
                self.setStyleSheet(
                    """
                    App {
                        background-color: rgb(10, 10, 255);
                        }
                    QPushButton {
                        background-color: rgb(10, 10, 255);
                        border-style: solid;
                        border-width: 1px;
                        border-color: black;
                    }
                """
                )
            elif action.isChecked() and action.text() == "Teal":
                self.setStyleSheet(
                    """
                    App {
                        background-color: rgb(0,140,140);
                    }
                    QPushButton {
                        background-color: rgb(0,140,140);
                        border-style: solid;
                        border-width: 1px;
                        border-color: black;
                    }    
                """
                )
            elif action.isChecked() and action.text() == "Grey":
                self.setStyleSheet(
                    """
                    App {
                        background-color: rgb(50,50,50);
                    }
                    QPushButton {
                        background-color: rgb(50,50,50);
                        border-style: solid;
                        border-width: 1px;
                        border-color: black;
                    }
                """
                )
            elif action.isChecked() and action.text() == "Off White":
                self.setStyleSheet(
                    """
                    App {
                        background-color: rgb(240,240,240)
                    }
                    QPushButton {
                        background-color: rgb(240,240,240);
                        border-style: solid;
                        border-width: 1px;
                        border-color: black;
                    }
                """
                )


def main():
    app = QApplication(sys.argv)
    win = App()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
