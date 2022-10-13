from dataclasses import dataclass
from typing import Callable, TypeVar

from . import Node

N = TypeVar("N")
N_co = TypeVar("N_co", covariant=True)


@dataclass(slots=True)
class SymbolNode(Node):
    symbol_name: str


@dataclass(slots=True)
class NumericNode(Node):
    operator: Callable[[N, N], N_co]

    lhs: int | float | complex | Node
    rhs: int | float | complex | Node


@dataclass(slots=True)
class AssignmentNode(Node):
    symbol: str
    value: object
