"""
    This file holds the Cipher abstract class with the encrypt
    and decrypt abstract methods.
"""

from abc import ABC, abstractmethod
from src.file_management.file_input import FileReader


class Cipher(ABC):
    def __init__(self, key=0):
        self.__key = key

    def set_key(self, key):
        self.__key = key

    def get_key(self):
        return self.__key

    @abstractmethod
    def encrypt(self, file_text, key):
        raise NotImplementedError("NotImplementedError")

    @abstractmethod
    def decrypt(self, file_text, key=""):
        raise NotImplementedError("NotImplementedError")
