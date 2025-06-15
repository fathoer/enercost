# separator.py

from PyQt6.QtWidgets import QFrame


def horizontal_separator():
    line = QFrame()
    line.setFrameShape(QFrame.Shape.HLine)
    line.setFrameShadow(QFrame.Shadow.Sunken)
    return line
