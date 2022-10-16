from dataclasses import dataclass
from .nodes import Node


class Tree:
    def __init__(self) -> None:
        self.nodes = []


@dataclass(slots=True)
class BaseNode(Node):
    lhs: Node
    rhs: Node
