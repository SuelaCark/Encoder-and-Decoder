"""
    This file holds the Caesar Cipher child class which inherits the variables of
    abstract class Cipher and overrides its abstract methods with the relevant
    implementation for the Caesar cipher.

"""

from src.ciphers.cipher import Cipher


class CaesarCipher(Cipher):
    def __init__(self, key=0):
        super().__init__(key)  # this invokes the parent initializer

    def get_key(self):
        return self._key

    # Caesar Cipher encrypt function
    def encrypt(self, file_text, key):
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
