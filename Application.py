from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget, QHBoxLayout
from PySide6.QtCore import QMargins
from Widgets import PushButton


class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        self.buttonZero = PushButton("0")
        self.buttonZero.setObjectName("ButtonZero")
        self.buttonOne = PushButton("1")
        self.buttonOne.setObjectName("ButtonOne")
        self.buttonTwo = PushButton("2")
        self.buttonTwo.setObjectName("ButtonTwo")
        self.buttonThree = PushButton("3")
        self.buttonThree.setObjectName("ButtonThree")
        self.buttonFour = PushButton("4")
        self.buttonFour.setObjectName("ButtonFour")
        self.buttonFive = PushButton("5")
        self.buttonFive.setObjectName("ButtonFive")
        self.buttonSix = PushButton("6")
        self.buttonSix.setObjectName("ButtonSix")
        self.buttonSeven = PushButton("7")
        self.buttonSeven.setObjectName("ButtonSeven")
        self.buttonEight = PushButton("8")
        self.buttonEight.setObjectName("ButtonEight")
        self.buttonNine = PushButton("9")
        self.buttonNine.setObjectName("ButtonNine")
        self.buttonNegate = PushButton("-/+")
        self.buttonNegate.setObjectName("ButtonNegate")
        self.buttonResult = PushButton("=")
        self.buttonResult.setObjectName("ButtonResult")
        self.centralWidget = QWidget()
        self.grid = QGridLayout()
        self.grid.setObjectName("Grid")
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(QMargins(0, 0, 0, 0))
        self.buttons: list[PushButton] = [self.buttonZero, self.buttonOne, self.buttonTwo, self.buttonThree, self.buttonFour, self.buttonFive,
                                          self.buttonSix, self.buttonSeven, self.buttonEight, self.buttonNine, self.buttonNegate, self.buttonResult]

        self.grid.addWidget(self.buttonSeven, 0, 0)
        self.grid.addWidget(self.buttonEight, 0, 1)
        self.grid.addWidget(self.buttonNine, 0, 2)

        self.grid.addWidget(self.buttonFour, 1, 0)
        self.grid.addWidget(self.buttonFive, 1, 1)
        self.grid.addWidget(self.buttonSix, 1, 2)

        self.grid.addWidget(self.buttonOne, 2, 0)
        self.grid.addWidget(self.buttonTwo, 2, 1)
        self.grid.addWidget(self.buttonThree, 2, 2)

        self.grid.addWidget(self.buttonNegate, 3, 0)
        self.grid.addWidget(self.buttonZero, 3, 1)
        self.grid.addWidget(self.buttonResult, 3, 2)

        for button in self.buttons:
            button.setFont(QFont("DM Sans", 15, 500, False))
            button.setStyleSheet("background-color: rgb(0, 0, 0); color: white; width: 100%; height: 100%;")
            button.bgColor = QColor(80, 80, 100)

        self.centralWidget.setLayout(self.grid)
        self.setCentralWidget(self.centralWidget)
        self.setStyleSheet("QMainWindow {background-color: rgb(40, 40, 60);}")
        self.show()
