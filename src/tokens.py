from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    KWD_EXISTS = auto()
    KWD_FOR = auto()
    KWD_SET = auto()
    KWD_SUBSET = auto()
    KWD_SUPERSET = auto()

    OP_SQRT = auto()

    OP_EQ = auto()
    OP_ADD = auto()
    OP_SUB = auto()
    OP_MUL = auto()
    OP_DIV = auto()

    CONST = auto()
    VAR = auto()

    SYM_CUSTOM = auto()

    SYM_LPAREN = auto()
    SYM_RPAREN = auto()

    TYPE_REAL = auto()
    TYPE_COMPLEX = auto()


@dataclass(frozen=True, slots=True)
class Token:
    tt: TokenType
    value: object = None
