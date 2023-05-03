"""
    This file manages the file input file and handles it to the respective cipher for encryption
    of the file contents
"""

from src.ciphers.caesar_cipher import CaesarCipher
from src.ciphers.atbash_cipher import AtbashCipher
from src.ciphers.vignere_cipher import VignereCipher


def process_input():
    # Choose operation/action: "encrypt" or "decrypt"
    while True:
        operation = input("Do you want to encrypt or decrypt the message? (encrypt/decrypt): ")

        if operation not in ["encrypt", "decrypt"]:
            print("Please enter a valid operation (encrypt/decrypt). Check for grammar mistakes!")
        else:
            break

    # Write the name of the cipher the user wants to use
    while True:
        cipher_name = input('Enter the cipher name ("caesar", "atbash", or "vignere"): ')

        # Defining a list of all allowed cipher classes
        ALLOWED_CIPHERS = ["caesar", "Caesar", "CAESAR", "atbash", "Atbash", "ATBASH", "vignere", "Vignere", "VIGNERE"]

        if cipher_name not in ALLOWED_CIPHERS:
            print("Please enter a valid cipher name (caesar, atbash, or vignere). Check for grammar mistakes! ")
        else:
            # Map cipher name to a cipher class and ask for the encryption/decryption key for each cipher respectively
            if cipher_name == "caesar":
                key_prompt = 'Enter the encryption key (integer expected): ' \
                    if operation == "encrypt" else 'Enter the decryption key (integer expected): '

                key = int(input(key_prompt))
                cipher = CaesarCipher(key)

                input_text = str(input("Enter the message you would like to encrypt or decrypt: "))
                output_text = cipher.encrypt(input_text, key) if operation == "encrypt" \
                    else cipher.decrypt(input_text, key)
                break

            elif cipher_name == "atbash":   # The AtbashCipher does not need a key
                cipher = AtbashCipher()

                input_text = str(input("Enter the message you would like to encrypt or decrypt: "))
                output_text = cipher.encrypt(input_text, key="") \
                    if operation == "encrypt" else cipher.decrypt(input_text, key="")
                break

            elif cipher_name == "vignere":
                key_prompt = 'Enter the encryption key (string expected): ' \
                    if operation == "encrypt" else 'Enter the decryption key (string expected): '

                key = input(key_prompt)
                cipher = VignereCipher(key)

                input_text = str(input("Enter the message you would like to encrypt or decrypt: "))
                output_text = cipher.encrypt(input_text, key) if operation == "encrypt" \
                    else cipher.decrypt(input_text, key)
                break

    if output_text.strip() == "":
        raise ValueError("Output text cannot be empty")

    while True:
        filename = input('Enter the name of the output file: ')
        if filename.strip() == "":
            print("File name cannot be empty. Please enter a valid filename.")
        else:
            break

        try:
            with open(filename + ".txt", 'w') as file:
                file.write(output_text)
                print(f"Encrypted/Decrypted message has been written to {filename}.txt.")
            break

        except FileNotFoundError:
            print("File not found. Please enter a valid filename.")

"""
TODO:   1. Check if key is int or string respectively and ask again when its wrong

"""


