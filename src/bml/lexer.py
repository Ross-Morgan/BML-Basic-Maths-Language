import string
from typing import Iterator

from syntax import chars
from logger import AppLogger
from tokens import Token, TokenType


DEBUG = True

logger = AppLogger("logger")

if DEBUG:
    logger.disable()


class Lexer:
    __slots__ = "source", "text_source", "current_char"

    def __init__(self, source: str) -> None:
        self.source = iter(source)
        self.text_source = source

    def advance(self):
        self.current_char = next(self.source, None)
        print(self.current_char)

    def lex(self) -> Iterator[Token]:
        self.advance()

        while self.current_char is not None:
            if self.current_char in string.whitespace:
                # NOTE Below is not necessary but it complains otherwise
                # An empty if will just rope it into the if/elif structure
                # making sure it cannot run any other lexing functions
                # on a whitespace
                if self.current_char == "\n":
                    yield Token(TokenType.NEWLINE)

                self.advance()
                continue

            elif self.current_char == chars.BACKTICK:
                yield self.lex_symbol_name()

            elif self.current_char == chars.COMMA:
                yield Token(TokenType.SYM_COMMA)

            elif self.current_char in chars.OPERATORS:
                yield self.lex_operator()

            elif self.current_char in chars.PARENS:
                yield self.lex_paren()

            elif self.current_char in chars.REAL_DIGITS:
                yield self.lex_number()
                continue

            else:
                yield self.lex_text()

            self.advance()

        yield Token(TokenType.EOF)

    def lex_operator(self) -> Token:
        match self.current_char:
            case "+":
                return Token(TokenType.OP_ADD)
            case "-":
                return Token(TokenType.OP_SUB)
            case "*":
                return Token(TokenType.OP_MUL)
            case "/":
                return Token(TokenType.OP_DIV)
            case "√":
                return Token(TokenType.OP_SQRT)
            case "=":
                self.advance()

                if self.current_char == ">":
                    self.advance()
                    return Token(TokenType.SYM_ARROW)
                else:
                    return Token(TokenType.OP_EQ)
            case _:
                logger.error(f"Unhandled operator: '{self.current_char}'")  # noqa

    def lex_paren(self) -> Token:
        match self.current_char:
            case "(":
                return Token(TokenType.SYM_LRPAREN)
            case "[":
                return Token(TokenType.SYM_LSPAREN)
            case "{":
                return Token(TokenType.SYM_LCPAREN)
            case ")":
                return Token(TokenType.SYM_RRPAREN)
            case "]":
                return Token(TokenType.SYM_RSPAREN)
            case "}":
                return Token(TokenType.SYM_RCPAREN)
            case _:
                logger.error(f"Unhandled bracket: '{self.current_char}'")  # noqa

    def lex_symbol_name(self) -> Token:
        self.current_char = ""
        name = []

        while True:
            self.advance()

            if (self.current_char is None or
                self.current_char in string.whitespace or
                self.current_char in chars.PARENS):
                break

            name.append(self.current_char)

        return Token(TokenType.SYM_CUSTOM, "".join(name))

    def lex_number(self) -> Token:
        logger.info(f"Lexing number: '{self.current_char}'")
        n = [self.current_char]

        self.current_char = ""

        while True:
            self.advance()

            if self.current_char is None or self.current_char not in chars.COMPLEX_DIGITS:  # noqa
                break

            n.append(self.current_char)

        if n == ["i"]:
            return Token(TokenType.TYPE_COMPLEX, complex(0, 1))

        if n[-1] == "i":
            return Token(TokenType.TYPE_COMPLEX, complex(0, float("".join(n[:-1]))))  # noqa

        if "." in n:
            return Token(TokenType.TYPE_REAL, int("".join(n)))
        return Token(TokenType.TYPE_REAL, float("".join(n)))

    def lex_text(self) -> Token:
        print(f"Lexing other: '{self.current_char}'")

        letters = [self.current_char]

        while True:
            self.advance()

            if self.current_char is None or self.current_char not in string.ascii_letters:  # noqa
                break

            letters.append(self.current_char)

        s = "".join(letters)

        if s.lower() in chars.KEYWORDS:
            match s.lower():
                case "exists":
                    return Token(TokenType.KWD_EXISTS)
                case "for":
                    return Token(TokenType.KWD_FOR)
                case "set":
                    return Token(TokenType.KWD_SET)
                case "subset":
                    return Token(TokenType.KWD_SUBSET)
                case "superset":
                    return Token(TokenType.KWD_SUPERSET)
                case "union":
                    return Token(TokenType.KWD_UNION)
                case "intersection":
                    return Token(TokenType.KWD_INTERSECTION)
                case "difference":
                    return Token(TokenType.KWD_DIFFERENCE)
                case "mod":
                    return Token(TokenType.OP_MOD)
                case _:
                    logger.error(f"Unhandled keyword: '{s}'")

        return Token(TokenType.CONST, s)


def main():
    with open("sample/source.bml", encoding="utf-8") as f:
        lexer = Lexer(f.read())

    tokens = list(lexer.lex())

    print()
    print("---------------------------")
    print()

    print(*map(lambda t: f"{t.tt.name}: {t.value}", tokens), sep="\n")


if __name__ == "__main__":
    main()
