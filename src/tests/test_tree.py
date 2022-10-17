import bml
from .tests import test


@test
def test_tree():
    tree = bml.syntax.Tree()
    tree.add_node(bml.syntax.nodes.AssignmentNode("a", 100))
    tree.add_node(bml.syntax.nodes.AssignmentNode("b", bml.syntax.nodes.SymbolNode("a")))

    print(tree)
