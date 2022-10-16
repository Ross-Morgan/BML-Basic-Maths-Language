"""
# BML Syntax Tree
"""

from __future__ import annotations

from typing import TypeVar

# from . import nodes, tree

N = TypeVar("N")
L = TypeVar("L")
R = TypeVar("R")


class Node:
    """Base class for syntax tree nodes"""

    def __init__(self, lhs: L | N, rhs: R | N):
        self.lhs = lhs
        self.rhs = rhs

    def compute(self): ...
