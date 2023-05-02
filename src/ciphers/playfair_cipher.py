# """
#     This file holds the Playfair Cipher (Poly-alphabetic cipher) child class which
#     inherits the variables of abstract class Cipher and overrides its abstract methods
#     with the relevant implementation for the Playfair cipher.
#
# """
#
# from src.ciphers.cipher import Cipher
#
#
# class PlayfairCipher(Cipher):
#     def __init__(self, keys=""):
#         print(keys)
#         super().__init__(keys)  # this invokes the parent initializer
#
#     def encrypt(self, text, keys):
#         plain_text = text.upper()
#
#         # Remove non alphabetic chars from the text and the key
#         plain_text = ''.join(filter(str.isalpha, plain_text))
#
#         # Remove non-letter chars from the key
#         keys = ''.join(filter(str.isalpha, keys)).upper()
#
#         # Checks if the text is even or odd, if odd adds 'z' in the end of the text
#         if len(plain_text) % 2 == 1:
#             plain_text += 'z'
#
#         # Replace 'J' with 'I' (due to there being 26 letters in the alphabet and
#         # we have only 25 places for the matrix)
#         plain_text = plain_text.replace('J', 'I')
#         keys = keys.replace('J', 'I')
#
#         # Remove duplicate letters from the key
#         keys = ''.join(sorted(set(keys), key=keys.index))
#         print(keys)
#
#         # keys += ''.join(chr(i + 97) for i in range(26) if chr(i + 97) not in key + 'i')
#         # ascii_alphabet = [chr(i) for i in range(65, 90)]
#
#         for i in range(26):
#             if chr(i + 65) not in keys + 'I':
#                 keys += chr(i + 65)
#
#         print(keys)
#         print(len(keys))
#             # for ch in key:
#             #     if char == key[ch]:
#             #         print(char)
#             #         print(ch)
#
#         # for i in range(len(plain_text)):
#         #     char = plain_text[i]
#         #     if char in range(len(keys)):
#         #         # print(key[char])
#         #         print(char)
#         # char = plain_text[i]
#         # key_ch = key[i % len(key)]
#
#
#
#
#
#         # for i in range(0, 25, 5):
#         #     matrix = list(keys[i:i + 5].upper())
#         #     if i in matrix:
#         #         ...
#
#             # print(matrix)
#
#         # transposed_matrix = list(map(list, zip(*matrix)))
#         # for i in range(len(transposed_matrix)):
#         #     col = transposed_matrix[i]
#         #     col_without_duplicates = []
#         #     for char in col:
#         #         if char not in col_without_duplicates:
#         #             col_without_duplicates.append(char)
#         #     transposed_matrix[i] = col_without_duplicates
#
#         # print(transposed_matrix)
#
#         # for i in range(26):
#         #     if chr(i + 65) not in keys + 'i':
#         #         keys += chr(i + 65).upper()
#         #         print(keys)
#
#         # Create a 5x5 matrix to store the alphabet letters
#         # matrix = [list(keys[i:i + 5]) for i in range(0, 25, 5)]
#
#         # Replace any pairs of letters in the plain_text that are the same with 'X'
#         # for i in range(0, len(plain_text), 2):
#         #     if plain_text[i] == plain_text[i + 1]:
#         #         plain_text[i] + 'x'
#         #     else:
#         #         plain_text[i:i + 2]
#
#         # print(plain_text)
#
#         # Encrypt the plain_text using the matrix
#         cipher_text = ''
#         # for i in range(0, len(plain_text), 2):
#             # a, b = plain_text[i], plain_text[i + 1]
#             # a_row, a_col = next((r, c) for r in range(5) for c in range(5) if matrix[r][c] == a)
#             # b_row, b_col = next((r, c) for r in range(5) for c in range(5) if matrix[r][c] == b)
#             # if a_row == b_row:
#             #     ciphertext += matrix[a_row][(a_col + 1) % 5] + matrix[b_row][(b_col + 1) % 5]
#             # elif a_col == b_col:
#             #     ciphertext += matrix[(a_row + 1) % 5][a_col] + matrix[(b_row + 1) % 5][b_col]
#             # else:
#             #     ciphertext += matrix[a_row][b_col] + matrix[b_row][a_col]
#
#             # return ciphertext
#
#     def decrypt(self, text):
#         pass
#
#
# if __name__ == "__main__":
#     plaintext = "HELLO IKIGAIJA"
#     key = "SECRET KEJ"
#     cipher2 = PlayfairCipher(key)
#
#     ciphertext = cipher2.encrypt(plaintext, key)
#     print(ciphertext)  # Output: "MOFOTVSKZZ"
#
#
