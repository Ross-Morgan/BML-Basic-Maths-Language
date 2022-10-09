import sys

from PyQt6 import QtWidgets

import editor


def main():
    app = QtWidgets.QApplication(sys.argv)

    editor_window = editor.gui.EditorAppWindow()
    editor_window.show()

    app.exec()


if __name__ == "__main__":
    main()
