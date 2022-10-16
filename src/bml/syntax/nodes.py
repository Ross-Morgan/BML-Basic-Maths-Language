from dataclasses import dataclass
from typing import Callable, TypeVar

N = TypeVar("N")
N_co = TypeVar("N_co", covariant=True)


N = TypeVar("N")
L = TypeVar("L")
R = TypeVar("R")


class Node:
    """Base class for syntax tree nodes"""

    def __init__(self, lhs: L | N, rhs: R | N):
        self.lhs = lhs
        self.rhs = rhs

    def compute(self) -> N_co:
        if isinstance(self.lhs, Node):
            self.lhs = self.lhs.compute()
        if isinstance(self.rhs, Node):
            self.rhs = self.rhs.compute()


@dataclass(slots=True)
class SymbolNode(Node):
    symbol_name: str


@dataclass(slots=True)
class AssignmentNode(Node):
    symbol: str
    value: object


@dataclass(slots=True)
class NumericNode(Node):
    operator: Callable[[N, N], N_co]

    lhs: int | float | complex | Node
    rhs: int | float | complex | Node

    def compute(self):
        super().compute()

        return self.operator(self.lhs, self.rhs)
