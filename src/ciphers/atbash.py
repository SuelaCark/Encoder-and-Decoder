"""
    This file holds the Atbash Cipher child class which inherits the variables
    of abstract class Cipher and overrides its abstract methods with the
    relevant implementation for the Atbash cipher.

"""

import string
from src.ciphers.cipher import Cipher


class AtbashCipher(Cipher):
    def __init__(self):
        super().__init__()  # this invokes the parent initializer

    def encrypt(self, text, key=0):
        encrypted_text = ""

        # Lists of lower and upper case alphabet (regular order)
        alphabet_lower = list(string.ascii_lowercase)
        alphabet_upper = list(string.ascii_uppercase)

        # Create dictionaries which use the reversed order alphabet and the regular order alphabet
        combined_alphabet_lower = dict(zip(list(reversed(alphabet_lower)), alphabet_lower))
        combined_alphabet_upper = dict(zip(list(reversed(alphabet_upper)), alphabet_upper))

        # Create a joined dictionary out of two other dictionaries
        combined_alphabet = {**combined_alphabet_lower, **combined_alphabet_upper}

        for char in text:
            if char.isalpha():
                encrypted_text += combined_alphabet[char]
            else:
                encrypted_text += char

        return encrypted_text

    def decrypt(self, text):
        if not isinstance(text, str):
            raise TypeError("Input message must be a string")

        decrypted_text = ""
        # Lists of lower and upper case alphabet (regular order)
        alphabet_lower = list(string.ascii_lowercase)
        alphabet_upper = list(string.ascii_uppercase)

        # Create dictionaries which use the reversed order alphabet and the regular order alphabet
        combined_alphabet_lower = dict(zip(list(reversed(alphabet_lower)), alphabet_lower))
        combined_alphabet_upper = dict(zip(list(reversed(alphabet_upper)), alphabet_upper))

        # Create a joined dictionary out of two other dictionaries
        combined_alphabet = {**combined_alphabet_lower, **combined_alphabet_upper}

        for letter in text:
            if letter.isalpha():
                decrypted_text += combined_alphabet[letter]
            else:
                decrypted_text += letter

        return decrypted_text


if __name__ == "__main__":
    plaintext = "HELLO World"
    cipher3 = AtbashCipher()

    print(cipher3.encrypt(plaintext))
    print(cipher3.decrypt("SVOOL Dliow53212   ??!"))
