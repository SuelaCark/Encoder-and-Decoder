# This file manages the file input file and handles it to the respective cipher for encryption
# of the file contents

# The input/output files can be managed and structure in 2 ways:
# 1. The main Cipher class can manage the file input and output, while the children classes access
#   and/or override these methods (better code optimization)
# 2. There can be a separate input and output file for file management before and after encryption

from src.ciphers.caesar_cipher import CaesarCipher
from src.ciphers.atbash_cipher import AtbashCipher
from src.ciphers.vignere_cipher import VignereCipher


def process_input():
    # Choose operation/action: "encrypt" or "decrypt"
    operation = str(input("Do you want to encrypt or decrypt the message? (encrypt/decrypt): "))

    if operation == "encrypt":
        key_prompt = 'Enter the encryption key: '
    elif operation == "decrypt":
        key_prompt = 'Enter the decryption key: '
    else:
        raise ValueError(f"Invalid operation: {operation}")

    # Write the name of the cipher the user wants to use
    cipher_name = input('Enter the cipher name ("caesar", "atbash", or "vignere"): ')

    if cipher_name == "caesar":
        cipher = CaesarCipher()
    elif cipher_name == "atbash":
        cipher = AtbashCipher()
    elif cipher_name == "vignere":
        cipher = VignereCipher()
    else:
        raise ValueError(f"Invalid cipher name: {cipher_name}")

    # Defining a list of all allowed cipher classes
    ALLOWED_CIPHERS = [CaesarCipher, AtbashCipher, VignereCipher]

    if isinstance(AtbashCipher(), object):
        pass
    if isinstance(cipher, tuple(ALLOWED_CIPHERS)):
        key = int(input(key_prompt))
    else:
        raise ValueError(f"Invalid cipher: {cipher.__class__.__name__}")

    input_text = str(input("Enter the message you would like to encrypt or decrypt: "))

    if operation == 'encrypt':
        cipher = CaesarCipher(key)
    else:
        cipher = CaesarCipher(key)

    filename = input('Enter the name of the output file: ')
    output_text = cipher.encrypt(input_text, key) if operation == "encrypt" else cipher.decrypt(input_text, key)

    try:
        with open(filename, 'w') as file:
            file.write(output_text)

    except FileNotFoundError:
        print("No such file")
