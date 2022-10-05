import string
from typing import Iterator

from chars import BACKTICK, COMPLEX_DIGITS, L_PARENS, OPERATORS, R_PARENS
from tokens import Token, TokenType


class Lexer:
    __slots__ = "source", "text_source", "current_char"

    def __init__(self, source: str) -> None:
        self.source = iter(source)
        self.text_source = source

    def advance(self):
        self.current_char = next(self.source, None)

    def lex(self) -> Iterator[Token]:
        self.advance()

        while self.current_char is not None:
            if self.current_char in string.whitespace:
                # NOTE Below is not necessary but it complains otherwise
                # An empty if will just rope it into the if/elif structure
                # making sure it cannot run any other lexing functions
                # on a whitespace
                self.advance()
                continue

            elif self.current_char == BACKTICK:
                yield self.lex_symbol_name()

            elif self.current_char in OPERATORS:
                match self.current_char:
                    case "+":
                        yield Token(TokenType.OP_ADD)
                    case "-":
                        yield Token(TokenType.OP_SUB)
                    case "*":
                        yield Token(TokenType.OP_MUL)
                    case "/":
                        yield Token(TokenType.OP_DIV)
                    case "√":
                        yield Token(TokenType.OP_SQRT)
                    case "=":
                        yield Token(TokenType.OP_EQ)
                    case _:
                        raise ValueError(f"Unhandled operator: '{self.current_char}'")

            elif self.current_char in L_PARENS:
                yield Token(TokenType.SYM_LPAREN)

            elif self.current_char in R_PARENS:
                yield Token(TokenType.SYM_RPAREN)

            elif self.current_char in COMPLEX_DIGITS:
                yield self.lex_number()

            else:
                yield self.lex_text()

            self.advance()

    def lex_symbol_name(self) -> Token:
        self.current_char = ""
        name = []

        while True:
            self.advance()

            if self.current_char is None or self.current_char in string.whitespace:
                break

            name.append(self.current_char)

        return Token(TokenType.SYM_CUSTOM, "".join(name))

    def lex_number(self) -> Token:
        print(f"Lexing number: '{self.current_char}'")
        n = [self.current_char]

        self.current_char = ""

        while True:
            self.advance()

            if self.current_char is None or self.current_char not in COMPLEX_DIGITS:
                break

            n.append(self.current_char)

        if n == ["i"]:
            return Token(TokenType.TYPE_COMPLEX, complex(0, 1))

        if n[-1] == "i":
            return Token(TokenType.TYPE_COMPLEX, complex(0, float("".join(n[:-1]))))
        return Token(TokenType.TYPE_REAL, float("".join(n)))

    def lex_text(self) -> Token:
        print(f"Lexing other: '{self.current_char}'")

        l = [self.current_char]

        while True:
            self.advance()

            if self.current_char is None or self.current_char not in string.ascii_letters:
                break

            l.append(self.current_char)

        s = "".join(l)

        match s.lower():
            case "set":
                return Token(TokenType.KWD_SET)
            case "exists":
                return Token(TokenType.KWD_EXISTS)
            case "for":
                return Token(TokenType.KWD_FOR)
            case _:
                return Token(TokenType.CONST, s)




def main():
    source = open("./sample/source.bml", encoding="utf-8").read()

    lexer = Lexer(source)
    tokens = lexer.lex()

    print(*list(tokens), sep="\n")


if __name__ == "__main__":
    main()
