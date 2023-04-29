"""
    This file holds the Caesar Cipher child class which inherits the variables
    of abstractclass Cipher and overrides its abstract methods with the
    relevant implementation for the Caesar cipher.

"""


from cipher import Cipher


class CaesarCipher(Cipher):
    def __init__(self, key, shift):
        super().__init__(key, shift)  # this invokes the parent initializer

    def encrypt(self, text):
        encrypted_text = ""
        # transverse the plain text
        for char in text:
            if char.isalpha():
                shift_code = 65 if char.isupper() else 97
                ascii_code = ord(char)

                new_ascii_code = (ascii_code - shift_code + self._shift) % 26 + shift_code

                encrypted_char = chr(new_ascii_code)
                # encrypted_char = chr(ascii_code - shift_code + self._shift) % 26 + shift_code
                # encrypted_text += encrypted_char
            else:
                encrypted_char = char
            encrypted_text += encrypted_char

        return encrypted_text

    def decrypt(self, text):
        decrypted_text = ""

        for char in text:
            if char.isalpha():
                # Shift the character by the inverse of the key
                shifted_char = chr((ord(char) - 65 - self._shift) % 26 + 65)
                decrypted_text += shifted_char
            else:
                decrypted_text += char

        return decrypted_text

    def set_key(self, key):
        self._key = key

    def set_shift(self, shift):
        self._shift = shift
