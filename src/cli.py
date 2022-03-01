from src.files import FileWriter
from os.path import join, isfile
from src.cerberus import cerberus_cipher, cerberus_decipher

INPUT_DIR = "tokens"
OUTPUT_DIR = "output"

OPERATIONS = {
    1: "encode",
    2: "decode",
}

BASE_OUT_DIR = "out"


class CLI:
    operation_type = ""  # it can be 'encode' or 'decode'
    base_out_path = ""
    user_filename = ""
    fw = None

    def __init__(self, _base_path):
        self.base_out_path = join(_base_path, BASE_OUT_DIR)

    def get_operation_type(self):
        while True:
            print("What kind of operation do you wish to perform?")
            for key, value in OPERATIONS.items():
                print(f"type ({key}) to {value}")

            _operation_value = int(input())
            if _operation_value not in OPERATIONS.keys():
                print("Please enter the index a valid operation")
            else:
                self.operation_type = OPERATIONS[_operation_value]
                break

    def get_filename(self):
        while True:
            filename = input("What's the name of the file?: ")

            if self.operation_type == OPERATIONS[1]:  # encode operation
                self.fw = FileWriter(self.base_out_path, INPUT_DIR, OUTPUT_DIR)
                self.user_filename = filename
                break

            elif self.operation_type == OPERATIONS[2]:  # decode operation
                path = join(self.base_out_path, OUTPUT_DIR, filename)
                if not isfile(path):
                    print(f"[X] The supplied filename doesn't exists in {OUTPUT_DIR}")
                else:  # set fw and exit loop
                    self.user_filename = filename
                    # decode operation does not use the output path
                    self.fw = FileWriter(self.base_out_path, OUTPUT_DIR, "")
                    break

    def perform_operation(self):

        filename = self.user_filename

        print(f"Operation: {self.operation_type.upper()} on {filename.upper()}")
        print(f"reading data from {self.fw.path_to_read}")
        if self.operation_type == OPERATIONS[1]:
            print(f"writing data to   {self.fw.path_to_write}")

        if self.operation_type == OPERATIONS[1]:  # encode
            # encode
            message = self.fw.read_file(filename)
            cipher, seed = cerberus_cipher(message)
            self.fw.write_file(cipher, filename)

            print("\nAll was setup successfully!")
            print("[WARNING]:")
            print(f"Your SEED for {filename.upper()} is {seed}")
            print("Make sure to save your SEED in a safe place, otherwise you'll loose all access to your data")
        elif self.operation_type == OPERATIONS[2]:  # decode
            # decode
            print("Please enter your seed separated by spaces, like: 1 2 3")
            _user_seed = []

            while True:
                _user_seed = input("Your seed: ").strip().replace(",", "").split(" ")
                if len(_user_seed) > 0:
                    break
                else:
                    print("No seed was provided")

            seed = [int(x) for x in _user_seed]
            cipher = self.fw.read_file(filename)
            message = cerberus_decipher(cipher, seed)
            print(f"Your message is: {message}")
