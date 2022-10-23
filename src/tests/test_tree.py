from bml.syntax import MultiNodeTree, SingleNodeTree, nodes

import load_path  # noqa NOSONAR


def test_tree_compilation():
    tree = MultiNodeTree()

    a = nodes.AssignmentNode("a", 100)
    b = nodes.AssignmentNode("b", nodes.SymbolNode("a"))
    c = nodes.AssignmentNode("c", nodes.SymbolNode("b"))
    d = nodes.AssignmentNode("d", nodes.SymbolNode("c"))
    e = nodes.AssignmentNode("e", nodes.SymbolNode("d"))
    f = nodes.AssignmentNode("f", nodes.SymbolNode("e"))

    tree.add_node(a)
    tree.add_node(b)
    tree.add_node(c)
    tree.add_node(d)
    tree.add_node(e)
    tree.add_node(f)

    new_tree = tree.compile()

    assert isinstance(new_tree, SingleNodeTree)

    assert new_tree.lhs is a
    assert new_tree.rhs.lhs is b
    assert new_tree.rhs.rhs.lhs is c
    assert new_tree.rhs.rhs.rhs.lhs is d
    assert new_tree.rhs.rhs.rhs.rhs.lhs is e
    assert new_tree.rhs.rhs.rhs.rhs.rhs.lhs is f

