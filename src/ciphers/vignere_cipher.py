"""
    This file holds the Vignere Cipher child class which inherits the variables of
    abstract class Cipher and overrides its abstract methods with the relevant implementation for
    the Vignere cipher.

"""


from src.ciphers.cipher import Cipher


class VignereCipher(Cipher):
    """
    Simple class docstring
    """
    def __init__(self, key=""):
        super().__init__(key)

    def encrypt(self, plain_text, key):
        """
        Takes the plain_text and the key (which is a string word), evaluates ...
        Finally, it returns the string encrypted_text.
        :param plain_text: str
        :param key: str
        :return: encrypted_text: str
        """

        ciphertext = ""
        key = key.upper()
        index = 0

        for char in plain_text:
            if char.isalpha():
                shift = ord(key[index % len(key)]) - 65  # get shift amount from corresponding letter in key
                shifted_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)  # shift using modular arithmetic
                ciphertext += shifted_char
                index += 1
            else:
                ciphertext += char

        return ciphertext

    def decrypt(self, text, key=""):
        decrypted_text = ""
        key = key.upper()
        index = 0

        for char in text:
            if char.isalpha():
                shift = ord(key[index % len(key)]) - 65
                shifted_char = chr((ord(char.upper()) - shift - 65) % 26 + 65)
                decrypted_text += shifted_char
                index += 1
            else:
                decrypted_text += char

        return decrypted_text
