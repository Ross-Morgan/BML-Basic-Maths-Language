from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Parser:
    tokens: list[str]

    def parse(self):
        pass
