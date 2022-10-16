from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class StackEmptyError(Exception):
    message: str


@dataclass
class StackFullError(Exception):
    message: str


class Stack(Generic[T]):
    def __init__(self, size: int = 0) -> None:
        self.max_size = size if size > 0 else None

        self.pile: list[T] = []

    def __repr__(self) -> str:
        return f"Stack({self.pile})"

    def push(self, item: T) -> None:
        if len(self.pile) == self.max_size and self.max_size is not None:
            raise StackFullError("Cannot push item onto full stack")

        self.pile.append(item)

    def pop(self) -> T:
        if len(self.pile) == 0:
            raise StackEmptyError("Cannot pop item off empty stack")

        return self.pile.pop()
