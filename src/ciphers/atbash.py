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
        text = text.lower()

        alphabet = list(string.ascii_lowercase)
        reversed_alphabet = list(reversed(alphabet))
        combined_alphabet = dict(zip(alphabet, reversed_alphabet))

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
        text = text.lower()

        alphabet = list(string.ascii_lowercase)
        reversed_alphabet = list(reversed(alphabet))
        combined_alphabet = dict(zip(reversed_alphabet, alphabet))

        for letter in text:
            if letter.isalpha():
                decrypted_text += combined_alphabet[letter]
            else:
                decrypted_text += letter

        return decrypted_text


if __name__ == "__main__":
    plaintext = "HELLO World"
    cipher3 = AtbashCipher()

    text1 = cipher3.encrypt(plaintext)
    print(cipher3.encrypt("SVOOL Dliow"))
