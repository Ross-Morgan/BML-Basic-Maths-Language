import sys

from PyQt6 import QtCore, QtGui, QtWidgets

from . import highlighter


class EditorWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.setMinimumSize(1280, 720)
        self.setStyleSheet("QWidget { font-size: 30px; }")

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.highlighter = highlighter.new_highlighter()

    def setup_editor(self):
        pass


class EditorAppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(self)

        e = EditorWidget()

        self.setCentralWidget(e)
