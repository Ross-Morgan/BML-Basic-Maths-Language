from __future__ import annotations

from dataclasses import dataclass
import textwrap
from .nodes import Node


class Tree:
    def __init__(self) -> None:
        self.nodes: list[Node] = []

    def __repr__(self) -> str:
        x = f"""
             Tree(
             length={len(self.nodes)})"
             nodes={self.nodes}
             )
             """

        return textwrap.dedent(x)

    def add_node(self, node: Node) -> None:
        self.nodes.append(node)

    def compile(self) -> Tree:
        cls = self.__class__

        last_node = self.nodes.pop()

        for node in reversed(self.nodes):
            last_node = Node(node, last_node)

        new_tree = cls()
        new_tree.add_node(last_node)

        return new_tree


@dataclass(slots=True)
class BaseNode(Node):
    lhs: Node
    rhs: Node

