"""
    Filename: caesar_cipher.py

    This file holds the Caesar Cipher child class which inherits the variables of abstract class
    Cipher and overrides its abstract methods encrypt() and decrypt() with the relevant
    implementation for the Caesar cipher.
"""

from src.ciphers.cipher import Cipher


class CaesarCipher(Cipher):
    def __init__(self, key=0):
        """
            Constructor of the CaesarCipher class which is a child class of the abstract class Cipher.
            This constructor calls the initial constructor of the super class Cipher.
        """
        super().__init__(key)  # this invokes the parent initializer

    def get_key(self):
        return self._key

    # Caesar Cipher encrypt function
    def encrypt(self, file_text, key):
        """
            Encrypts a file text using the monoalphabetic rotation Caesar cipher.

            The Caesar cipher uses a substitution method where letters in the alphabet are
            shifted by some fixed number of spaces (using the encryption key) to yield an
            encoding alphabet.
            A Caesar cipher with a shift of 1 would encode an A -> B, Z -> A, and so on.

            :param file_text: string
            :param key: int
            :return: string
        """

        encrypted_text = ""
        # transverse the plain text
        for char in file_text:
            if char.isalpha():
                key_code = 65 if char.isupper() else 97
                ascii_code = ord(char)

                new_ascii_code = (ascii_code - key_code + self._key) % 26 + key_code
                encrypted_char = chr(new_ascii_code)
            else:
                encrypted_char = char

            encrypted_text += encrypted_char

        return encrypted_text

    # Caesar Cipher decrypt function
    def decrypt(self, file_text, key=""):
        """
            Decrypts a file text using the monoalphabetic rotation Caesar cipher.

            The Caesar cipher decryption uses a substitution method it takes the value of 26
            minus the shift (encryption key) value. Then it applies that new value to shift
            the encoded message back to its original form.

            :param file_text: string
            :param key: None (predefined within the function)
            :return: string
        """
        decrypted_text = ""

        for char in file_text:
            if char.isalpha():
                key_code = 65 if char.isupper() else 97
                ascii_code = ord(char)

                new_ascii_code = (ascii_code - self._key - key_code) % 26 + key_code
                decrypted_char = chr(new_ascii_code)
            else:
                decrypted_char = char

            decrypted_text += decrypted_char

        return decrypted_text
