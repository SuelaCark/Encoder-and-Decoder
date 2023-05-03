"""
    This file manages the file input file and handles it to the respective cipher for encryption
    of the file contents
"""

from src.ciphers.caesar_cipher import CaesarCipher
from src.ciphers.atbash_cipher import AtbashCipher
from src.ciphers.vignere_cipher import VignereCipher


def process_input():
    # Choose operation/action: "encrypt" or "decrypt"
    operation = input("Do you want to encrypt or decrypt the message? (encrypt/decrypt): ")

    # Exclude operations which do not match the
    if operation not in ["encrypt", "decrypt"]:
        raise ValueError(f"Invalid operation: {operation}")

    # Write the name of the cipher the user wants to use
    cipher_name = input('Enter the cipher name ("caesar", "atbash", or "vignere"): ')

    # Map the cipher name to a cipher class and ask for the encryption/decryption key for each cipher respectively
    if cipher_name == "caesar":
        key_prompt = 'Enter the encryption key (integer expected): ' \
            if operation == "encrypt" else 'Enter the decryption key (integer expected): '
        key = int(input(key_prompt))
        cipher = CaesarCipher(key)
        input_text = str(input("Enter the message you would like to encrypt or decrypt: "))
        output_text = cipher.encrypt(input_text, key) if operation == "encrypt" else cipher.decrypt(input_text, key)
    elif cipher_name == "atbash":   # The AtbashCipher does not need a key
        cipher = AtbashCipher()
        input_text = str(input("Enter the message you would like to encrypt or decrypt: "))
        output_text = cipher.encrypt(input_text, key="") \
            if operation == "encrypt" else cipher.decrypt(input_text, key="")
    elif cipher_name == "vignere":
        key_prompt = 'Enter the encryption key (string expected): ' \
            if operation == "encrypt" else 'Enter the decryption key (string expected): '
        key = input(key_prompt)
        cipher = VignereCipher(key)
        input_text = str(input("Enter the message you would like to encrypt or decrypt: "))
        output_text = cipher.encrypt(input_text, key) if operation == "encrypt" else cipher.decrypt(input_text, key)
    else:
        raise ValueError(f"Invalid cipher name: {cipher_name}")

    # Defining a list of all allowed cipher classes
    ALLOWED_CIPHERS = [CaesarCipher, AtbashCipher, VignereCipher]

    if not isinstance(cipher, tuple(ALLOWED_CIPHERS)):
        raise ValueError(f"Invalid cipher: {cipher.__class__.__name__}")

    filename = input('Enter the name of the output file: ')

    try:
        with open(filename + ".txt", 'w') as file:
            file.write(output_text)

    except FileNotFoundError:
        print("File not found. There is no such file")
