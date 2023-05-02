"""
    This file holds the Cipher abstract class with the encrypt
    and decrypt abstract methods.
"""

from abc import ABC, abstractmethod


class Cipher(ABC):
    def __init__(self, key=0):
        self._key = key

    def set_key(self, key):
        self._key = key

    def get_key(self):
        return self._key

    @abstractmethod
    def encrypt(self, file_text, key):
        raise NotImplementedError("NotImplementedError")

    @abstractmethod
    def decrypt(self, file_text, key=""):
        raise NotImplementedError("NotImplementedError")

    # @abstractmethod
    # def write_file_output(self, file_name, result=""):
    #     raise  NotImplementedError("NotImplementedError")
