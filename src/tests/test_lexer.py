import load_path  # noqa NOSONAR

from bml.lexer import Lexer
from bml.tokens import Token, TokenType


SOURCE = """\
`number = 20

`add = `number + 2
`sub = `number - 2
`mul = `number * 2
`div = `number / 2
"""


def test_symbol_parsing():
    actual_tokens = [
        Token(TokenType.SOF),

        # Assignment
        Token(TokenType.SYM_CUSTOM, "number"),
        Token(TokenType.OP_EQ),
        Token(TokenType.TYPE_REAL, 20.0),

        Token(TokenType.NEWLINE),
        Token(TokenType.NEWLINE),

        # Addition
        Token(TokenType.SYM_CUSTOM, "add"),
        Token(TokenType.OP_EQ),
        Token(TokenType.SYM_CUSTOM, "number"),
        Token(TokenType.OP_ADD),
        Token(TokenType.TYPE_REAL, 2.0),

        Token(TokenType.NEWLINE),

        # Subtraction
        Token(TokenType.SYM_CUSTOM, "sub"),
        Token(TokenType.OP_EQ),
        Token(TokenType.SYM_CUSTOM, "number"),
        Token(TokenType.OP_SUB),
        Token(TokenType.TYPE_REAL, 2.0),

        Token(TokenType.NEWLINE),

        # Multiplication
        Token(TokenType.SYM_CUSTOM, "mul"),
        Token(TokenType.OP_EQ),
        Token(TokenType.SYM_CUSTOM, "number"),
        Token(TokenType.OP_MUL),
        Token(TokenType.TYPE_REAL, 2.0),

        Token(TokenType.NEWLINE),

        # Division
        Token(TokenType.SYM_CUSTOM, "div"),
        Token(TokenType.OP_EQ),
        Token(TokenType.SYM_CUSTOM, "number"),
        Token(TokenType.OP_DIV),
        Token(TokenType.TYPE_REAL, 2.0),

        Token(TokenType.NEWLINE),

        Token(TokenType.EOF),
    ]

    lexer = Lexer(SOURCE)
    tokens = list(lexer.lex())

    assert actual_tokens == tokens
