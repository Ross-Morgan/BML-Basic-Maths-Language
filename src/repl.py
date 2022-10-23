from bml.lexer import Lexer
from bml.parser import Parser


class ReplInstance:
    def __init__(self) -> None:
        self.data = {
            "sets": [],
            "matricies": [],
            "symbols": [],
        }

    def parse_line(self, line: str):
        lexer = Lexer(line)
        parser = Parser(lexer.lex())

        ast = parser.parse()
        ast = ast.compile()
        ast.simplify()
