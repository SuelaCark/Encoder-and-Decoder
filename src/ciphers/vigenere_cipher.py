"""
    This file holds the Vigenere Cipher child class which inherits the variables of
    abstract class Cipher and overrides its abstract methods with the relevant
    implementation for the Vigeneree cipher.

"""


from src.ciphers.cipher import Cipher


class VigenereCipher(Cipher):
    """
    Simple class docstring
    """
    def __init__(self, key=""):
        super().__init__(key)

    def encrypt(self, file_text, key):
        """
        Takes the file_text and the key (which is a string word), evaluates ...
        Finally, it returns the string encrypted_text.
        :param file_text: str
        :param key: str
        :return: encrypted_text: str
        """

        ciphertext = ""
        key = key.lower()
        index = 0

        for char in file_text:
            if char.isalpha():
                # Get shift amount from corresponding letter in key
                shift = ord(key[index % len(key)]) - 97

                # Shift using modular arithmetic
                shifted_char = chr((ord(char.lower()) + shift - 97) % 26 + 97)
                ciphertext += shifted_char
                index += 1
            else:
                ciphertext += char

        return ciphertext

    def decrypt(self, file_text, key=""):
        decrypted_text = ""
        key = key.lower()
        index = 0

        for char in file_text:
            if char.isalpha():
                shift = ord(key[index % len(key)]) - 97
                shifted_char = chr((ord(char.lower()) - shift - 97) % 26 + 97)
                decrypted_text += shifted_char
                index += 1
            else:
                decrypted_text += char

        return decrypted_text
