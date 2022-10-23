from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    NEWLINE = auto()           # <\n>
    SOF = auto()               # <sof>
    EOF = auto()               # <eof>

    KWD_EXISTS = auto()        # exists
    KWD_FOR = auto()           # for

    KWD_MATRIX = auto()        # matrix
    KWD_SET = auto()           # set
    KWD_FUNC = auto()          # func

    # Set operations
    KWD_SUBSET = auto()        # subset
    KWD_SUPERSET = auto()      # superset
    KWD_UNION = auto()         # union
    KWD_INTERSECTION = auto()  # interection
    KWD_DIFFERENCE = auto()    # difference

    OP_EXP = auto()            # ^ | e
    OP_MOD = auto()            # mod
    OP_SQRT = auto()           # √
    OP_ADD = auto()            # +
    OP_SUB = auto()            # -
    OP_MUL = auto()            # *
    OP_DIV = auto()            # /
    OP_EQ = auto()             # =
    OP_NE = auto()             # =/=
    OP_GT = auto()             # >
    OP_LT = auto()             # <
    OP_GE = auto()             # >=
    OP_LE = auto()             # <=

    CONST = auto()
    VAR = auto()

    SYM_CUSTOM = auto()        # `<text>

    SYM_ARROW = auto()         # =>
    SYM_COMMA = auto()         # ,

    SYM_LRPAREN = auto()       # (
    SYM_RRPAREN = auto()       # [
    SYM_LSPAREN = auto()       # {
    SYM_RSPAREN = auto()       # )
    SYM_LCPAREN = auto()       # ]
    SYM_RCPAREN = auto()       # }

    TYPE_REAL = auto()
    TYPE_COMPLEX = auto()


@dataclass(frozen=True, slots=True)
class Token:
    tt: TokenType
    value: object = None

    def __repr__(self) -> str:
        return f"Token<type: {self.tt}, value: {self.value}>"


class TokenGroup:
    OPERATOR_TYPES = [
        TokenType.OP_ADD,
        TokenType.OP_SUB,
        TokenType.OP_MUL,
        TokenType.OP_DIV,
        TokenType.OP_SQRT,
        TokenType.OP_EQ,
        TokenType.OP_GT,
        TokenType.OP_GE,
        TokenType.OP_LT,
        TokenType.OP_LE,
        TokenType.OP_NE
    ]

    PAREN_TYPES = [
        TokenType.SYM_LRPAREN,
        TokenType.SYM_LSPAREN,
        TokenType.SYM_LCPAREN,
        TokenType.SYM_RRPAREN,
        TokenType.SYM_RSPAREN,
        TokenType.SYM_RCPAREN,
    ]
