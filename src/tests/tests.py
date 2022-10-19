from __future__ import annotations

from typing import Callable


class Tests:
    test_cases: list[Test] = []
    test_names: list[str] = []

    @classmethod
    def run_all(cls):
        n = len(cls.test_cases)

        for i, test in enumerate(cls.test_cases):
            print(f"Testing \033[36m\[{i + 1}/{n}]\033[0m", end=" ")
            test.run()


class Test:
    def __init__(self, func: Callable):
        self.f = func

    def run(self):
        try:
            self.f()
            print("\033[33Test Passed\033[0m")
        except AssertionError as err:
            print(f"Test Failed: {err.args}")


def test(func: Callable[[], None]):
    Tests.test_cases.append(Test(func))
    Tests.test_names.append(func.__name__)

    return func
