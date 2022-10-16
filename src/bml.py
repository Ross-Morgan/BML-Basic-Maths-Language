import sys


def parse_args():
    if len(sys.argv) < 2:
        raise ValueError("At least 1 argument required: ")

    cli_args = sys.argv[1:]

    print(cli_args)

    match cli_args:
        case ["compile", filename, *args]:
            print("Compiling...")

        case ["repl", *args]:
            print("Running repl")

        case _:
            print("No case matched")


parse_args()