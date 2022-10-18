import textwrap

import bml
from bml.lexer import Lexer
from bml.tokens import Token, TokenType

from .tests import test


@test
def test_symbol_parsing():
    source = textwrap.dedent("""\
    `symbol = 20
    `symbol2 = `symbol * 2
    """)

    actual_tokens = [
        Token(TokenType.SOF),
        Token(TokenType.SYM_CUSTOM, "symbol"),
        Token(TokenType.OP_EQ),
        Token(TokenType.TYPE_REAL, 20.0),
        Token(TokenType.NEWLINE),
        Token(TokenType.SYM_CUSTOM, "symbol2"),
        Token(TokenType.OP_EQ),
        Token(TokenType.SYM_CUSTOM, "symbol"),
        Token(TokenType.OP_MUL),
        Token(TokenType.TYPE_REAL, 2.0),
        Token(TokenType.NEWLINE),
        Token(TokenType.EOF),
    ]

    lexer = Lexer(source)
    tokens = list(lexer.lex())

    assert actual_tokens == tokens

