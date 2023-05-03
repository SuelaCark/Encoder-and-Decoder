"""
    Filename: cipher.py
    This file holds the abstract class Cipher (parent class) with its abstract methods encrypt() and decrypt().
"""


from abc import ABC, abstractmethod


class Cipher(ABC):
    def __init__(self, key=0):
        """
            Constructor of the abstract class Cipher (super class)
            which holds the optional parameter key, used for encryption.
        """
        self._key = key

    # Getters and setters
    def set_key(self, key):
        self._key = key

    def get_key(self):
        return self._key

    @abstractmethod
    def encrypt(self, file_text, key):
        """
            Abstract method encrypt() which holds the parameters file_text and key.
            This method is not implemented in the super class.
            :param file_text: string
            :param key: int/string
            :return: NotImplementedError
        """
        raise NotImplementedError("NotImplementedError")

    @abstractmethod
    def decrypt(self, file_text, key=""):
        """
            Abstract method decrypt() which holds the parameters file_text and key.
            This method is not implemented in the super class.
            :param file_text: string
            :param key: int/string
            :return: NotImplementedError
        """
        raise NotImplementedError("NotImplementedError")
