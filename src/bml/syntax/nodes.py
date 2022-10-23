from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, TypeVar

from .custom_types import SetExpr

N = TypeVar("N")
L = TypeVar("L")
R = TypeVar("R")

N_co = TypeVar("N_co", covariant=True)


class Node:
    """Base class for syntax tree nodes"""
    def __init__(self, lhs: Node | L, rhs: Node | R) -> None:
        self.lhs: Node | object
        self.rhs: Node | object

    def compute(self) -> Node:
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


@dataclass(slots=True, frozen=True)
class ExistenceNode:
    constant: str
    set_name: str


@dataclass(slots=True)
class SetNode(Node):
    pass


@dataclass(slots=True)
class DefiniteSetNode(SetNode):
    elements: list[int | float | complex]


@dataclass(slots=True)
class IndefiniteSetNode(SetNode):
    constants: dict[str, ExistenceNode]
    expr: SetExpr

    def compute(self) -> N:
        return self


@dataclass(slots=True)
class MatrixNode(Node):
    matrix: list[list[int | float | complex]]
    shape: tuple[int, int]
