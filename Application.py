from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget, QHBoxLayout, QSizePolicy, QApplication
from PySide6.QtCore import QMargins
from Widgets import *


class Application(QMainWindow):
    app: QApplication = None

    def __init__(self):
        super().__init__()
        self.screen = self.app.screens()[0]

        self.setMaximumWidth(round(self.screen.size().width() / 3 * 2))

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
        self.centralWidget.setObjectName("CentralWidget")
        self.grid = QGridLayout()
        self.grid.setObjectName("Grid")
        self.numberView = NumberView("0")
        self.numberView.setObjectName("NumberView")
        self.numberView.setMaximumWidth(self.maximumWidth())
        self.buttonRemoveLastChar = PushButton("←")
        self.buttonRemoveLastChar.setObjectName("ButtonRemoveLastChar")
        self.buttonAdd = PushButton("+")
        self.buttonAdd.setObjectName("ButtonAdd")
        self.buttonSub = PushButton("-")
        self.buttonSub.setObjectName("ButtonSub")
        self.buttonMultiply = PushButton("x")
        self.buttonMultiply.setObjectName("ButtonMultiply")
        self.buttonDivide = PushButton("÷")
        self.buttonDivide.setObjectName("ButtonDivide")
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(QMargins(0, 0, 0, 0))
        self.buttons: list[PushButton] = [self.buttonZero, self.buttonOne, self.buttonTwo, self.buttonThree,
                                          self.buttonFour, self.buttonFive, self.buttonSix, self.buttonSeven,
                                          self.buttonEight, self.buttonNine, self.buttonNegate, self.buttonResult,
                                          self.buttonRemoveLastChar, self.buttonAdd, self.buttonSub, self.buttonMultiply,
                                          self.buttonDivide]

        self.grid.addWidget(self.numberView, 0, 0, 1, 3)

        self.grid.addWidget(self.buttonSeven, 1, 0)
        self.grid.addWidget(self.buttonEight, 1, 1)
        self.grid.addWidget(self.buttonNine, 1, 2)
        self.grid.addWidget(self.buttonRemoveLastChar, 1, 3)

        self.grid.addWidget(self.buttonFour, 2, 0)
        self.grid.addWidget(self.buttonFive, 2, 1)
        self.grid.addWidget(self.buttonSix, 2, 2)
        self.grid.addWidget(self.buttonAdd, 2, 3)

        self.grid.addWidget(self.buttonOne, 3, 0)
        self.grid.addWidget(self.buttonTwo, 3, 1)
        self.grid.addWidget(self.buttonThree, 3, 2)
        self.grid.addWidget(self.buttonSub, 3, 3)

        self.grid.addWidget(self.buttonNegate, 4, 0)
        self.grid.addWidget(self.buttonZero, 4, 1)
        self.grid.addWidget(self.buttonResult, 4, 2)

        self.numberView.setMinimumHeight(60)
        self.numberView.setStyleSheet("color: white; padding: 6px;")
        self.numberView.setFont(QFont("Roboto", 18, 600, False))

        for button in self.buttons:
            button.setFont(QFont("DM Sans", 25, 500, False))
            button.setStyleSheet("background-color: rgb(0, 0, 0); color: white; width: 100%; height: 100%;")
            button.bgColor = QColor(80, 80, 100)
            button.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
            normal_color = button.bgColor
            button.set_normal_color(button.bgColor)
            enter_color = QColor(normal_color.red() + normal_color.red() / 10, normal_color.green() +
                                 normal_color.green() / 10, normal_color.blue() + normal_color.blue() / 10)
            button.set_enter_color(enter_color)
            button.setCheckable(False)

        self.centralWidget.setLayout(self.grid)
        self.setCentralWidget(self.centralWidget)
        self.setStyleSheet("QMainWindow {background-color: rgb(40, 40, 60);}")
        self.setWindowTitle("Calculadora")
        self.show()
