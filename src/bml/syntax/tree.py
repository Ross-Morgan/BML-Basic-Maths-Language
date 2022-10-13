from dataclasses import dataclass
from . import Node


class Tree:
    def __init__(self) -> None:
        self.nodes = []


@dataclass(slots=True)
class BaseNode(Node):
    lhs: Node
    rhs: Node
