from dataclasses import dataclass


class Complex(complex):
    def __mod__(self, other: int | float | complex):
        if isinstance(other, int | float):
            re = self.real % other
            im = self.imag % other

            return self.__class__(re, im)

        if isinstance(other, complex):
            min_div = min(
                self.real // other.real,
                self.imag // other.imag,
            )

            other_copy = other * min_div

            re = self.real % other_copy.real
            im = self.imag % other_copy.imag

            return self.__class__(re, im)

        return NotImplemented


@dataclass(slots=True)
class SetExpr:
    e: str
