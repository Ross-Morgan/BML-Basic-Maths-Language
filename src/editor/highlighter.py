import re
from dataclasses import dataclass

from PyQt6 import QtCore, QtGui


COLOUR = QtCore.Qt.GlobalColor


class BMLHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent: QtGui.QTextDocument = None):
        super().__init__(parent)
        self._mapping: dict[re.Pattern, QtGui.QTextCharFormat] = {}

    def add_mapping(self, pattern: re.Pattern, pattern_format: QtGui.QTextCharFormat):
        self._mapping[pattern] = pattern_format

    def highlightBlock(self, text: str) -> None:
        for pattern, fmt in self._mapping.items():
            for match in pattern.finditer(text):
                start, end = match.span()
                self.setFormat(start, end-start, fmt)


@dataclass(slots=True)
class PatternFormat:
    pattern: re.Pattern = re.compile(".")
    text_format: QtGui.QTextCharFormat = None


def fmt(colour: QtCore.Qt.GlobalColor) -> QtGui.QTextCharFormat:
    f = QtGui.QTextCharFormat()
    f.setForeground(colour)

    return f


def new_highlighter(document: QtGui.QTextDocument):
    patterns: dict[str, PatternFormat] = {
        "for": None,
        "exists": None,
        "matrix": None,
        "set": None,
        "func": None,
        "subset": None,
        "superset": None,
        "union": None,
        "intersection": None,
        "difference": None,
        "mod": None,
        "=>": None,
        "√": None,
        "+": None,
        "-": None,
        "*": None,
        "/": None,
        "`sym": None,
        ",": None,
        "(": None,
        "[": None,
        "{": None,
        ")": None,
        "]": None,
        "}": None,
    }

    for kwd in patterns:
        if patterns[kwd] is None:
            patterns[kwd] = PatternFormat()

    patterns["set"].pattern = re.compile(r"^set(?=\s)", re.MULTILINE),
    patterns["set"].text_format = fmt(COLOUR.cyan)

    patterns["func"].pattern = re.compile(r"^func(?=\s)", re.MULTILINE)
    patterns["func"].text_format = fmt(COLOUR.cyan)

    patterns["for"].pattern = re.compile(r"(?<=\s)for(?=\s)", re.MULTILINE)
    patterns["for"].text_format = fmt(COLOUR.green)

    patterns["exists"].pattern = re.compile(r"(?<=\s)exists(?=\s)", re.MULTILINE)
    patterns["exists"].text_format = fmt(COLOUR.green)

    syntax_highlighter = BMLHighlighter(parent=document)

    for f in patterns.values():
        syntax_highlighter.add_mapping(f.pattern, f.text_format)

    return syntax_highlighter
