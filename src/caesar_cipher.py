"""
    This file holds the Caesar Cipher child class which inherits the variables of abstract
    class Cipher and overrides its abstract methods with the relevant implementation for the
    Caesar cipher.

"""


from cipher import Cipher


class CaesarCipher(Cipher):
    def __init__(self, flag=True):
        super().__init__(flag)  # this invokes the parent initializer
        # self._radius = radius if radius > 0 else 1

    def encrypt(self, text, s):
        result = ""
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters in plain text

            if char.isupper():
                result += chr((ord(char) + s - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
            return result

    def decrypt(self):
        pass

    def set_key(self, key):
        self._key = key

    def set_shift(self, shift):
        self._shift = shift
