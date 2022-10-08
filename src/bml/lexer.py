import string
from typing import Iterator

from syntax import chars
from logger import AppLogger
from tokens import Token, TokenType

logger = AppLogger("logger")


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

            elif self.current_char == chars.BACKTICK:
                yield self.lex_symbol_name()

            elif self.current_char == chars.COMMA:
                yield Token(TokenType.SYM_COMMA)

            elif self.current_char in chars.OPERATORS:
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
                        self.advance()

                        if self.current_char == ">":
                            yield Token(TokenType.SYM_ARROW)
                            self.advance()
                        else:
                            yield Token(TokenType.OP_EQ)

                        continue
                    case _:
                        raise ValueError(f"Unhandled operator: '{self.current_char}'")  # noqa

            elif self.current_char in chars.PARENS:
                match self.current_char:
                    case "(":
                        yield Token(TokenType.SYM_LRPAREN)
                    case "[":
                        yield Token(TokenType.SYM_LSPAREN)
                    case "{":
                        yield Token(TokenType.SYM_LCPAREN)
                    case ")":
                        yield Token(TokenType.SYM_RRPAREN)
                    case "]":
                        yield Token(TokenType.SYM_RSPAREN)
                    case "}":
                        yield Token(TokenType.SYM_RCPAREN)
                    case _:
                        logger.error(f"Unhandled bracket: '{self.current_char}'")  # noqa

            elif self.current_char in chars.REAL_DIGITS:
                yield self.lex_number()

            else:
                yield self.lex_text()

            self.advance()

    def lex_symbol_name(self) -> Token:
        self.current_char = ""
        name = []

        while True:
            self.advance()

            if self.current_char is None or self.current_char in string.whitespace:  # noqa
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
                case "mod":
                    return Token(TokenType.OP_MOD)
                case _:
                    raise ValueError(f"Unhandled keyword: '{s}'")

        return Token(TokenType.CONST, s)
