"""
    Filename: vigenere_cipher.py

    This file holds the Vigenere Cipher child class which inherits the variables of abstract class
    Cipher and overrides its abstract methods encrypt() and decrypt() with the relevant
    implementation for the Vigenere cipher.
"""


from src.ciphers.cipher import Cipher


class VigenereCipher(Cipher):
    """
    Child class of the abstract parent class Cipher.
    """
    def __init__(self, key=""):
        """
            Constructor of the VigenereCipher class which is a child class of the abstract class Cipher.
            This constructor calls the initial constructor of the super class Cipher.
        """
        super().__init__(key)

    def encrypt(self, file_text, key):
        """
            Encrypts a file text using the polyalphabetic Vigenere cipher.
            Vigenere Cipher encryption uses an encryption key and a 25x25 matrix
            of the alphabet (excluding one letter from the alphabet).

            :param file_text: string
            :param key: string
            :return: string
        """

        ciphertext = ""
        key = key.lower()
        index = 0

        for char in file_text:
            if char.isalpha():
                # Get shift amount from corresponding letter in key
                shift = ord(key[index % len(key)]) - 97

                # Shift using modular arithmetic
                shifted_char = chr((ord(char.lower()) + shift - 97) % 26 + 97)
                ciphertext += shifted_char
                index += 1
            else:
                ciphertext += char

        return ciphertext

    def decrypt(self, file_text, key=""):
        """
            Decrypts a file text using the polyalphabetic Vigenere cipher.
            Vigenere Cipher decryption uses a decryption key and a 25x25 matrix
            of the alphabet (excluding one letter from the alphabet).
            To decrypt, it takes the first letter of the ciphertext and the first letter of the key,
            and subtract their values (letters have a value equal to their position in the alphabet
            starting from 0). If the result is negative, it adds 26 (the nr of letters in the alphabet),
            the result gives the rank of the plain letter.

            :param file_text: string
            :param key: None (predefined within the function)
            :return: string
        """
        decrypted_text = ""
        key = key.lower()
        index = 0

        for char in file_text:
            if char.isalpha():
                shift = ord(key[index % len(key)]) - 97
                shifted_char = chr((ord(char.lower()) - shift - 97) % 26 + 97)
                decrypted_text += shifted_char
                index += 1
            else:
                decrypted_text += char

        return decrypted_text
