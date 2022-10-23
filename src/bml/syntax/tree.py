from __future__ import annotations

import textwrap
from dataclasses import dataclass

from .nodes import Node


@dataclass(slots=True)
class BaseNode(Node):
    lhs: Node
    rhs: Node


class SingleNodeTree:
    def __init__(self, node: Node):
        self.node = node

    def __repr__(self) -> str:
        return f"Tree(node={self.node})"

    def set_node(self, new_node: Node) -> None:
        self.node = new_node

    def simplify(self) -> None:
        self.node.compute()

    @property
    def lhs(self):
        return self.node.lhs

    @property
    def rhs(self):
        return self.node.rhs


class MultiNodeTree:
    def __init__(self) -> None:
        self.nodes: list[Node] = []

    def __repr__(self) -> str:
        x = f"""
             Tree(
             length={len(self.nodes)})"
             nodes={self.nodes}
             )"""

        return textwrap.dedent(x)

    def add_node(self, node: Node) -> None:
        self.nodes.append(node)

    def compile(self) -> SingleNodeTree:
        """
        Takes multi-node tree and returns a single-node tree
        """
        nodes = self.nodes

        current_node = None
        last_node = None

        # Run until nodes is exhausted
        while nodes:
            current_node = nodes.pop()
            last_node = BaseNode(current_node, last_node)

        new_tree = SingleNodeTree(last_node)

        return new_tree
