from copy import deepcopy
from typing import Iterator

from . import syntax as ast
from .logger import AppLogger
from .stack import Stack
from .tokens import Token, TokenType

logger = AppLogger("app")


class Parser:
    def __init__(self, tokens: Iterator[Token]):
        self.tokens = deepcopy(tokens)

        self.current_token = None

        self.existing_symbols = []

        self.lparen_stack: Stack[TokenType] = Stack()
        self.rparen_stack: Stack[TokenType] = Stack()

    def advance(self):
        """Load next token"""
        self.current_token = next(self.tokens)

        return self.current_token

    def parse(self) -> ast.MultiNodeTree:
        """Turn tokens into Abstract Syntax Tree"""
        tree = ast.MultiNodeTree()

        return tree
