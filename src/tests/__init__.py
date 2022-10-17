from . import test_tree

from . import tests

def run_tests():
    print("Starting tests")

    tests.Tests.run_all()

    print("Tests finished")
