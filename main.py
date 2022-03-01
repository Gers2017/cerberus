import os
from src.cli import CLI


def main():
    cli = CLI(os.getcwd())
    cli.get_operation_type()
    cli.get_filename()
    cli.perform_operation()


if __name__ == '__main__':
    main()
