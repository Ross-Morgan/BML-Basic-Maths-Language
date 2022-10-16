from copy import deepcopy
import operator
from typing import Iterator

import syntax as ast
from tokens import Token, TokenType, Types


class Parser:
    def __init__(self, tokens: Iterator[Token]):
        self.tokens = deepcopy(tokens)

        self.current_token = None

        self.existing_symbols = []

        self.lparen_stack = Stack()
        self.rparen_stack = Stack()


    def advance(self):
        self.current_token = next(self.tokens)

    def parse(self):
        while self.current_token.tt is not TokenType.EOF:
            self.advance()

            match self.current_token.tt:
                case TokenType.SYM_CUSTOM:
                    node = self.parse_assignment()

                case TokenType.KWD_SET:
                    self.parse_set()

    def parse_assignment(self) -> ast.nodes.AssignmentNode:
        symbol = self.current_token

        self.advance()

        assert self.current_token.tt is TokenType.OP_EQ

        self.advance()

        if self.current_token.tt is TokenType.SYM_CUSTOM:
            if self.current_token.value in self.existing_symbols:
                return ast.nodes.AssignmentNode(symbol, ast.nodes.SymbolNode(symbol))

            return ast.nodes.AssignmentNode(symbol, self.parse_assignment())

        if self.current_token.tt is TokenType.TYPE_REAL:
            return ast.nodes.AssignmentNode(symbol, self.parse_numeric())

    def parse_set(self):
        self.advance()

        set_name = self.current_token

    def parse_numeric(self):
        numeric = self.current_token

        self.advance()

        if self.current_token.tt in Types.PAREN_TYPES:
            self.advance()

        if self.current_token.tt in Types.OPERATOR_TYPES:
            self.advance()

            match self.current_token.tt:
                case TokenType.OP_EQ:
                    pass
                case TokenType.OP_NE:
                    pass
                case TokenType.OP_GT:
                    pass
                case TokenType.OP_GE:
                    pass
                case TokenType.OP_LT:
                    pass
                case TokenType.OP_LE:
                    pass
                case TokenType.OP_ADD:
                    pass
                case TokenType.OP_SUB:
                    pass
                case TokenType.OP_MUL:
                    pass
                case TokenType.OP_DIV:
                    pass
                case TokenType.OP_MOD:
                    pass
