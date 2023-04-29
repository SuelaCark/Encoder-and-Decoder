"""
    This file holds the Cipher abstract class with the encrypt and decrypt abstract methods. AAAAAAAAAAAAAAAAAAAAAAAAAAA

"""


from abc import ABC, abstractmethod


class Cipher(ABC):
    def __init__(self, key, shift):
        self._key = key
        self._shift = shift

    @abstractmethod
    def encrypt(self, plain_text):
        # After adding the file input, change the text parameter to file
        raise NotImplementedError("NotImplementedError")

    @abstractmethod
    def decrypt(self, text):
        raise NotImplementedError("NotImplementedError")

    def get_key(self):
        return self._key

    def get_shift(self):
        return self._shift
