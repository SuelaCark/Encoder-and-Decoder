'''
    This file holds the Cipher abstract class with the encrypt and decrypt abstract methods.

'''


from abc import ABC, abstractmethod


class Cipher(ABC):
    def __init__(self, flag):
        self._flag = flag

    @abstractmethod
    def encrypt(self):
        raise NotImplementedError("NotImplementedError")

    @abstractmethod
    def decrypt(self):
        raise NotImplementedError("NotImplementedError")

    def get_flag(self):
        return self._flag
