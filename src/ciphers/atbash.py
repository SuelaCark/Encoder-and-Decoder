"""
    This file holds the Atbash Cipher child class which inherits the variables
    of abstract class Cipher and overrides its abstract methods with the
    relevant implementation for the Atbash cipher.

"""

from src.ciphers.cipher import Cipher


class AtbashCipher(Cipher):
    def __init__(self, key):
        super().__init__(key)  # this invokes the parent initializer

    def set_key(self, key):
        self._key = key

    def get_key(self):
        return self._key

    def encrypt(self, text, key):
        ...

    def decrypt(self, text):
        ...

