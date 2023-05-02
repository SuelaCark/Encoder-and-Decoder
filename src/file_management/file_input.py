# This file manages the file input file and handles it to the respective cipher for encryption
# of the file contents

# The input/output files can be managed and structure in 2 ways:
# 1. The main Cipher class can manage the file input and output, while the children classes access
#   and/or override these methods (better code optimization)
# 2. There can be a separate input and output file for file management before and after encryption

# from src/ciphers/main.py import __main__

class FileReader:
    def __init__(self, filename):
        self._filename = filename

    @staticmethod
    def read_file(filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    print(line)

        except FileNotFoundError:
            print("No such file")
