from PySide6.QtGui import QColor
from PySide6.QtWidgets import QPushButton
import re


class PushButton(QPushButton):
    def _set_bgColor(self, value: QColor):
        self.setStyleSheet(re.sub("background-color: rgb\\(\\d+, \\d+, \\d+\\)", f"background-color: rgb({value.red()}, {value.green()}, {value.blue()})",
                                  self.styleSheet()))

    def _get_bgColor(self):
        backColor = re.match("background-color: rgb\\((\\d+), (\\d+), (\\d+)\\)", self.styleSheet())
        print(backColor.groups()[0])

    bgColor = property(fget=_get_bgColor, fset=_set_bgColor)
