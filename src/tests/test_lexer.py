import textwrap

import bml

from .tests import test


@test
def test_symbol_parsing():
    source = textwrap.dedent("""\
    `symbol = 20
    `symbol_2 = `symbol * 2
    """)

    print(source)
