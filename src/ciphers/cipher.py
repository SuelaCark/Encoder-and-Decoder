"""
    This file holds the Cipher abstract class with the encrypt
    and decrypt abstract methods.
"""

from abc import ABC, abstractmethod


class Cipher(ABC):
    def __init__(self, key=0):
        self._key = key

    @abstractmethod
    def encrypt(self, plain_text, key):
        # After adding the file input, change the text parameter to file
        raise NotImplementedError("NotImplementedError")

    @abstractmethod
    def decrypt(self, text):
        raise NotImplementedError("NotImplementedError")


