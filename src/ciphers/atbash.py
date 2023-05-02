"""
    This file holds the Atbash Cipher child class which inherits the variables
    of abstract class Cipher and overrides its abstract methods with the
    relevant implementation for the Atbash cipher.

"""
import string

from src.ciphers.cipher import Cipher


class AtbashCipher(Cipher):
    def __init__(self):
        super().__init__()  # this invokes the parent initializer

    # It doesn't need a key, so...?
    def encrypt(self, text, key=0):
        text = text.lower()
        alphabet_lower = list(string.ascii_lowercase)

        # print(alphabet_lower)
        print(text)
        for char in text:
            if char.isalpha():
                print(char)

    def decrypt(self, text):
        ...


if __name__ == "__main__":
    plaintext = "HELLO IKIGAIJA"
    cipher3 = AtbashCipher()

    print(cipher3.encrypt(plaintext))

