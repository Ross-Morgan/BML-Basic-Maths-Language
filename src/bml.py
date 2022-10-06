from argparse import ArgumentParser, Namespace


class Args:
    def __init__(self, namespace: Namespace) -> None:
        self.filepath: str = namespace.filepath
        self.verbose: bool = namespace.verbose

    def __repr__(self) -> str:
        return f"Args(filepath: {self.filepath}, verbose: {self.verbose})"


arg_parser = ArgumentParser()

arg_parser.add_argument("filepath", required=True, help="file to interpret")
arg_parser.add_argument("-v", "--verbose", type=bool, default=False)

args = Args(arg_parser.parse_args())

print(args)