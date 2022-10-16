from copy import deepcopy
from typing import Iterator

# import syntax as ast
from tokens import Token, TokenType


class Parser:
    def __init__(self, tokens: Iterator[Token]):
        self.tokens = deepcopy(tokens)

    def parse(self):
        for token in self.tokens:
            pass
