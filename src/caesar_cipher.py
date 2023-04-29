"""
    This file holds the Caesar Cipher child class which inherits the variables
    of abstract class Cipher and overrides its abstract methods with the
    relevant implementation for the Caesar cipher.

"""


from cipher import Cipher


class CaesarCipher(Cipher):
    def __init__(self, key, shift):
        super().__init__(key, shift)  # this invokes the parent initializer

    # For now, the encrypt func only encrypts text
    # Might be able to expand it to also include numbers with shifting
    # for a better encryption of the text
    def encrypt(self, text):
        encrypted_text = ""
        # transverse the plain text
        for char in text:
            if char.isalpha():
                shift_code = 65 if char.isupper() else 97
                ascii_code = ord(char)

                new_ascii_code = (ascii_code - shift_code + self._shift) % 26 + shift_code
                encrypted_char = chr(new_ascii_code)
            else:
                encrypted_char = char

            encrypted_text += encrypted_char

        return encrypted_text

    def decrypt(self, text):
        decrypted_text = ""

        for char in text:
            if char.isalpha():
                shift_code = 65 if char.isupper() else 97
                ascii_code = ord(char)

                new_ascii_code = (ascii_code - self._shift - shift_code) % 26 + shift_code
                decrypted_char = chr(new_ascii_code)
            else:
                decrypted_char = char

            decrypted_text += decrypted_char

        return decrypted_text

    def set_key(self, key):
        self._key = key

    def set_shift(self, shift):
        self._shift = shift
