from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt

class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)