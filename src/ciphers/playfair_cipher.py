"""
    This file holds the Playfair Cipher (Poly-alphabetic cipher) child class which
    inherits the variables of abstract class Cipher and overrides its abstract methods
    with the relevant implementation for the Playfair cipher.

"""

from src.ciphers.cipher import Cipher
import re


class PlayfairCipher(Cipher):
    def __init__(self, key, shift):
        super().__init__(key, shift)  # this invokes the parent initializer

    def encrypt(self, text, key):
        encrypted_text = ""
        text = "HIDE MONEY"

        plaintext = ""
        # Remove non alphabetic chars from the text
        plaintext = ''.join(filter(str.isalpha, plaintext)).upper()

        # for char in text:
        #     if char.isalpha():
        #         plaintext += char
        #     print(plaintext)

        # Checks if the text is even or odd, if odd adds Z in the end of the text
        if len(plaintext) % 2 == 1:
            plaintext += 'Z'
            print(plaintext)

        # Remove non-letter chars from the key
        key = ''.join(filter(str.isalpha, key)).upper()

        # Step 3: Create a 5x5 matrix to store the alphabet letters

        # Step 4: Replace 'J' with 'I' (due to there being 26 letters in the
        # alphabet and we have only 25 places for the matrix)
        key = key.replace('J', 'I')

        # matrix = generate_playfair_matrix(key)

        plaintext = re.sub(r'[^A-Z]', '', text.upper())

        # # Create a 5x5 matrix of the letters in the key (with 'J' replaced by 'I')

        # key += ''.join(chr(i + 65) for i in range(26) if chr(i + 65) not in key + 'I')
        # matrix = [list(key[i:i + 5]) for i in range(0, 25, 5)]
        #
        # # Replace any pairs of letters in the plaintext that are the same with 'X'
        # plaintext = ''.join(
        #     plaintext[i] + 'X' if plaintext[i] == plaintext[i + 1] else plaintext[i:i + 2] for i in
        #     range(0, len(plaintext), 2))
        #
        # # Encrypt the plaintext using the matrix
        # ciphertext = ''
        # for i in range(0, len(plaintext), 2):
        #     a, b = plaintext[i], plaintext[i + 1]
        #     a_row, a_col = next((r, c) for r in range(5) for c in range(5) if matrix[r][c] == a)
        #     b_row, b_col = next((r, c) for r in range(5) for c in range(5) if matrix[r][c] == b)
        #     if a_row == b_row:
        #         ciphertext += matrix[a_row][(a_col + 1) % 5] + matrix[b_row][(b_col + 1) % 5]
        #     elif a_col == b_col:
        #         ciphertext += matrix[(a_row + 1) % 5][a_col] + matrix[(b_row + 1) % 5][b_col]
        #     else:
        #         ciphertext += matrix[a_row][b_col] + matrix[b_row][a_col]
        #
        # return ciphertext

    def decrypt(self, text):
        pass


if __name__ == "__main__":
    c1 = PlayfairCipher(1, 2)
    c1.encrypt("HIDE MONEY", 3)

