# """
#     This file holds the Mono-alphabetic Cipher child class which inherits the variables of abstract
#     class Cipher and overrides its abstract methods with the relevant implementation for the
#     Mono-alphabetic cipher.
#
# """
#
#
# from src.ciphers.cipher import Cipher
#
#
# class MonoAlphabeticCipher(Cipher):
#     def __init__(self, key):
#         super().__init__(key)  # this invokes the parent initializer
#         self._key = key
#
#     def encrypt(self, plaintext, key=0):
#         ciphertext = ""
#
#         for char in plaintext:
#             if char.isalpha():
#                 idx = ord(char.lower()) - 97
#                 ciphertext += self._key[idx]
#             else:
#                 ciphertext += char
#         return ciphertext
#
#     def decrypt(self, text):
#         pass
#
#
# if __name__ == "__main__":
#     cipher = MonoAlphabeticCipher("phqgiumeaylnofdxjkrcvstzwb")
#
#     plaintext = "this is a secret message"
#     ciphertext = cipher.encrypt(plaintext)
#     print(ciphertext)  # output: "gtkn kn p xknzkn tkyykz"
#
#
