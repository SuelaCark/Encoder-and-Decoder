"""
    This file manages the file input file and handles it to the respective cipher for encryption
    of the file contents
"""

from src.ciphers.caesar_cipher import CaesarCipher
from src.ciphers.atbash_cipher import AtbashCipher
from src.ciphers.vignere_cipher import VignereCipher


def process_input():
    # Choose operation/action: "encrypt" or "decrypt"
    operation = str(input("Do you want to encrypt or decrypt the message? (encrypt/decrypt): "))

    # Exclude operations which do not match the
    if operation not in ["encrypt", "decrypt"]:
        raise ValueError(f"Invalid operation: {operation}")

    # Write the name of the cipher the user wants to use
    cipher_name = input('Enter the cipher name ("caesar", "atbash", or "vignere"): ')

    # Map the cipher name to a cipher class and ask for the encryption/decryption key for each cipher respectively
    if cipher_name == "caesar":
        key_prompt = 'Enter the encryption key: ' if operation == "encrypt" else 'Enter the decryption key: '
        key = int(input('Enter the encryption key: '))
        cipher = CaesarCipher(key)
    elif cipher_name == "atbash":   # The AtbashCipher does not need a key
        cipher = AtbashCipher()
    elif cipher_name == "vignere":
        key_prompt = 'Enter the encryption key: ' if operation == "encrypt" else 'Enter the decryption key: '
        key = input('Enter the encryption key: ')
        cipher = VignereCipher(key)
    else:
        raise ValueError(f"Invalid cipher name: {cipher_name}")

    # If the warning key does not effect the code logic, the following commented code can be deleted

    # Defining a list of all allowed cipher classes
    # ALLOWED_CIPHERS = [CaesarCipher, AtbashCipher, VignereCipher]

    # if isinstance(AtbashCipher(), object):
    #     pass
    # if isinstance(cipher, tuple(ALLOWED_CIPHERS)):
    #     key = int(input(key_prompt))
    #     print(key_prompt)
    # else:
    #     raise ValueError(f"Invalid cipher: {cipher.__class__.__name__}")

    input_text = str(input("Enter the message you would like to encrypt or decrypt: "))

    filename = input('Enter the name of the output file: ')
    output_text = cipher.encrypt(input_text, key) if operation == "encrypt" else cipher.decrypt(input_text, key)

    try:
        with open(filename, 'w') as file:
            file.write(output_text)

    except FileNotFoundError:
        print("File not found. There is no such file")
