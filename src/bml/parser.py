from copy import deepcopy
from typing import Iterator

from . import syntax as ast
from .tokens import Token, TokenType, Types
from .stack import Stack
from .logger import AppLogger


logger = AppLogger("app")


class Parser:
    def __init__(self, tokens: Iterator[Token]):
        self.tokens = deepcopy(tokens)

        self.current_token = None

        self.existing_symbols = []

        self.lparen_stack: Stack[TokenType] = Stack()
        self.rparen_stack: Stack[TokenType] = Stack()


    def advance(self):
        self.current_token = next(self.tokens)

        return self.current_token

    def parse(self):
        pass
