from __future__ import annotations

from typing import Callable


class Tests:
    test_cases: list[Test] = []

    @classmethod
    def run_all(cls):
        for i, test in enumerate(cls.test_cases):
            test.run(_id=i, _total=len(cls.test_cases))


class Test:
    def __init__(self, func: Callable):
        self.f = func

    def run(self, _id=None, _total=None):
        if _id is not None:
            print(f"[{_id}", end="")
            if _total is not None:
                print(f"/{_total}", end="")
            print("]", end="")

        try:
            self.f()
            print("Test Passed")
        except AssertionError as err:
            print(f"Test Failed: {err.args}")


def test(func: Callable[[], None]):
    Tests.test_cases.append(Test(func))

    return func
