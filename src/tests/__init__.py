from . import test_tree, test_lexer

from . import tests

def run_tests():
    print("Starting tests")

    tests.Tests.run_all()

    print("Tests finished")
