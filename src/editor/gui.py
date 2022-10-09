from PyQt6 import QtCore, QtGui, QtWidgets

from . import highlighter


class EditorWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(1280, 720)
        self.setStyleSheet("QWidget { font-size: 30px; }")

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.setup_ui()
        self.setup_editor()

    def setup_ui(self):
        self.text_box = QtWidgets.QPlainTextEdit(self)
        self.text_box.resize(self.size())
        self.text_box.setFont(QtGui.QFont("Consolas"))
        self.text_box.setStyleSheet("margin-top: 20px; background-color: #232323; color: white;")  # noqa

    def setup_editor(self):
        self.highlighter = highlighter.new_highlighter()
        self.highlighter.setDocument(self.text_box.document())

    def resizeEvent(self, new: QtGui.QResizeEvent) -> None:
        self.text_box.resize(new.size())


class EditorAppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        e = EditorWidget()

        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.GlobalColor.darkGray)

        self.setCentralWidget(e)
