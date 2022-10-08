from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ModNode:
    lhs: int | float | complex
