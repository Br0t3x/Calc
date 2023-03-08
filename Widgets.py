from PySide6.QtCore import QEvent, QPropertyAnimation
from PySide6.QtGui import QColor, QEnterEvent, QMouseEvent, Qt
from PySide6.QtWidgets import QPushButton, QLabel
import re


class PushButton(QPushButton):
    _bgColor: QColor = None
    _enterColor: QColor = None
    _normalColor: QColor = None

    def _set_bgColor(self, value: QColor):
        self._bgColor = value
        self.setStyleSheet(re.sub("background-color: rgb\\(\\d+, \\d+, \\d+\\)",
                                  f"background-color: rgb({value.red()}, {value.green()}, {value.blue()})",
                                  self.styleSheet()))

    def _get_bgColor(self):
        return self._bgColor

    def set_normal_color(self, value: QColor):
        self._normalColor = value

    def get_normal_color(self) -> QColor:
        return self._normalColor

    def set_enter_color(self, value: QColor):
        self._enterColor = value

    def get_enter_color(self) -> QColor:
        return self._enterColor

    bgColor = property(fget=_get_bgColor, fset=_set_bgColor)

    def enterEvent(self, event: QEnterEvent) -> None:
        anim = QPropertyAnimation(self, b"bgColor", self)
        anim.setStartValue(self._bgColor)
        anim.setEndValue(self.get_enter_color())
        anim.setDuration(1000)
        anim.start()

    def leaveEvent(self, event: QEvent) -> None:
        anim = QPropertyAnimation(self, b"bgColor", self)
        anim.setStartValue(self._bgColor)
        anim.setEndValue(self.get_normal_color())
        anim.setDuration(1000)
        anim.start()

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        central_widget = self.parent()
        view: NumberView = central_widget.findChild(NumberView, "NumberView",
                                                    Qt.FindChildOption.FindChildrenRecursively)
        black_list = ["ButtonNegate", "ButtonRemoveLastChar", "ButtonResult", "ButtonAdd", "ButtonSub",
                      "ButtonMultiply", "ButtonDivide", "ButtonPow", "ButtonDot", "ButtonOpenParenthesis",
                      "ButtonCloseParenthesis", ""]

        if view is not None:
            if not black_list.__contains__(self.objectName()):
                view.setText(view.text() + self.text())

    @property
    def normalColor(self):
        return self._normalColor


class NumberView(QLabel):
    pass
