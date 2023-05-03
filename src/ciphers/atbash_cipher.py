"""
    Filename: atbash_cipher.py
    This file holds the Atbash Cipher child class which inherits the variables of abstract class
    Cipher and overrides its abstract methods encrypt() and decrypt() with the relevant
    implementation for the Atbash cipher.
"""

import string
from src.ciphers.cipher import Cipher


class AtbashCipher(Cipher):
    """
        Child class of the abstract parent class Cipher.
    """
    def __init__(self):
        """
            Constructor of the AtbashCipher class which is a child class of the abstract class Cipher.
            This constructor calls the initial constructor of the super class Cipher.
        """
        super().__init__()  # this invokes the parent initializer

    def encrypt(self, file_text, key=None):
        """
        Encrypts a file text using the monoalphabetic substitution Atbash cipher (no encryption key required)

        The Atbash Cipher encrypter maps each letter of an alphabet it to its reverse,
        so that the first letter (e.g. A) becomes the last letter (e.g. Z),
        the second letter (B) becomes the second to last letter (Y), and so on.

        :param file_text: string
        :param key: None
        :return: string
        """
        encrypted_text = ""

        # Lists of lower and upper case alphabet (regular order)
        alphabet_lower = list(string.ascii_lowercase)
        alphabet_upper = list(string.ascii_uppercase)

        # Create dictionaries which use the reversed order alphabet and the regular order alphabet
        combined_alphabet_lower = dict(zip(list(reversed(alphabet_lower)), alphabet_lower))
        combined_alphabet_upper = dict(zip(list(reversed(alphabet_upper)), alphabet_upper))

        # Create a joined dictionary out of two other dictionaries
        combined_alphabet = {**combined_alphabet_lower, **combined_alphabet_upper}

        for char in file_text:
            if char.isalpha():
                encrypted_text += combined_alphabet[char]
            else:
                encrypted_text += char

        return encrypted_text

    def decrypt(self, file_text, key=None):
        """
        Decrypts a file text using the monoalphabetic substitution Atbash cipher (no encryption key required)

        The Atbash Cipher decrypter maps each letter of an alphabet it to its reverse,
        so that the first letter (e.g. A) becomes the last letter (e.g. Z),
        the second letter (B) becomes the second to last letter (Y), and so on.

        :param file_text:
        :param key: None
        :return: string
        """
        encrypted_text = ""
        if not isinstance(file_text, str):
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

        for letter in file_text:
            if letter.isalpha():
                decrypted_text += combined_alphabet[letter]
            else:
                decrypted_text += letter

        return decrypted_text
