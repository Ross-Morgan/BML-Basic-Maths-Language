from copy import deepcopy

from tokens import Token, TokenType

import syntax as ast


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = deepcopy(tokens)

    def parse(self):
        pass
