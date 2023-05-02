# This file manages the file input file and handles it to the respective cipher for encryption
# of the file contents

# The input/output files can be managed and structure in 2 ways:
# 1. The main Cipher class can manage the file input and output, while the children classes access
#   and/or override these methods (better code optimization)
# 2. There can be a separate input and output file for file management before and after encryption

from src.ciphers.caesar_cipher import CaesarCipher


def write_file(file_name, result=""):
    try:
        with open(file_name, 'w') as file:
            file.write(result)

    except FileNotFoundError:
        print("No such file")


def process_input():
    message = str(input("Enter a message you would like to encrypt or decrypt: "))
    operation = str(input("Do you want to encrypt or decrypt the message? (encrypt/decrypt): "))

    if operation == "encrypt" and isinstance(CaesarCipher(), object):
        key = int(input('Enter the encryption key: '))
    elif operation == "decrypt" and isinstance(CaesarCipher(), object):
        key = int(input('Enter the decryption key: '))
    else:
        key = None
        raise ValueError("The available action modes are only encrypt and decrypt.")

    if operation == 'encrypt':
        cipher = CaesarCipher(key)
        result = cipher.encrypt(message, key)
    else:
        cipher = CaesarCipher(key)
        result = cipher.decrypt(message)

    filename = input('Enter the name of the output file: ')
    write_file(filename, result)


    # file_name = str(input("Please input an existing file name: "))
    #
    # if type(file_name) == str and file_name == "*.txt":
    #     ...
    # else:
    #     raise TypeError("The file_name should be a string")