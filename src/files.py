import os
from os.path import isfile, join


def create_if_missing(path):
    if not os.path.exists(path):
        os.makedirs(path)


class FileWriter:
    path_to_read = ""
    path_to_write = ""

    def __init__(self, _base_path, input_dir, output_dir):
        self.base_path = _base_path

        self.path_to_read = join(_base_path, input_dir)
        self.path_to_write = join(_base_path, output_dir)

        create_if_missing(self.path_to_read)
        create_if_missing(self.path_to_write)

    def read_file(self, filename: str):
        path = join(self.path_to_read, filename)
        if isfile(path):
            with open(path) as f:
                return " ".join(f.readlines())
        else:
            print(f"No such a file on {path}")
            return None

    def write_file(self, payload: str, filename: str):
        path = join(self.path_to_write, filename)
        mode = "w" if isfile(path) else "x"

        try:
            with open(path, mode) as f:
                f.write(payload)
        except (FileNotFoundError, FileExistsError) as e:
            print(f"No such a file on {path}")
