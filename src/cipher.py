"""
    This file holds the Cipher abstract class with the encrypt and decrypt abstract methods.

"""


from abc import ABC, abstractmethod


class Cipher(ABC):
    def __init__(self, flag, key, shift):
        self._flag = flag
        self._key = key
        self._shift = shift

    @abstractmethod
    def encrypt(self, plain_text, shift):
        # After adding the file input, change the text parameter to file
        raise NotImplementedError("NotImplementedError")

    @abstractmethod
    def decrypt(self):
        raise NotImplementedError("NotImplementedError")

    def get_flag(self):
        return self._flag

    def get_key(self):
        return self._key

    def get_shift(self):
        return self._shift
