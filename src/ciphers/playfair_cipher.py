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
#     def __init__(self, key):
#         super().__init__(key)  # this invokes the parent initializer
#
#     def encrypt(self, text, key):
#         plaintext = text.lower()
#
#         # Remove non alphabetic chars from the text
#         plaintext = ''.join(filter(str.isalpha, plaintext))
#
#         # Checks if the text is even or odd, if odd adds 'z' in the end of the text
#         if len(plaintext) % 2 == 1:
#             plaintext += 'z'
#
#         # Remove non-letter chars from the key
#         key = ''.join(filter(str.isalpha, key)).lower()
#
#         # for char in plaintext:
#         #     for ch in key:
#         #         if char == key[ch]:
#         #             print(char)
#         #             print(ch)
#
#         for i in range(len(plaintext)):
#             char = plaintext[i]
#             if char in range(len(key)):
#                 # print(key[char])
#                 print(char)
#
#             # char = plaintext[i]
#             # key_ch = key[i % len(key)]
#             # print(char)
#             # print(key_ch)
#
#
#         # Replace 'J' with 'I' (due to there being 26 letters in the alphabet and
#         # we have only 25 places for the matrix)
#         plaintext = plaintext.replace('j', 'i')
#         key = key.replace('j', 'i')
#
#
#
#         key += ''.join(chr(i + 65) for i in range(26) if chr(i + 65) not in key + 'i').lower()
#         print(key)
#
#         for i in range(0, 25, 5):
#             matrix = list(key[i:i + 5].lower())
#             if i in matrix:
#                 ...
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
#         #     if chr(i + 65) not in key + 'i':
#         #         key += chr(i + 65).lower()
#         #         print(key)
#
#
#         print(key)
#
#         # Create a 5x5 matrix to store the alphabet letters
#         # matrix = [list(key[i:i + 5]) for i in range(0, 25, 5)]
#
#
#
#         # Replace any pairs of letters in the plaintext that are the same with 'X'
#         for i in range(0, len(plaintext), 2):
#             if plaintext[i] == plaintext[i + 1]:
#                 plaintext[i] + 'x'
#             else:
#                 plaintext[i:i + 2]
#
#         # print(plaintext)
#
#         # Encrypt the plaintext using the matrix
#         ciphertext = ''
#         for i in range(0, len(plaintext), 2):
#             # a, b = plaintext[i], plaintext[i + 1]
#             # a_row, a_col = next((r, c) for r in range(5) for c in range(5) if matrix[r][c] == a)
#             # b_row, b_col = next((r, c) for r in range(5) for c in range(5) if matrix[r][c] == b)
#             # if a_row == b_row:
#             #     ciphertext += matrix[a_row][(a_col + 1) % 5] + matrix[b_row][(b_col + 1) % 5]
#             # elif a_col == b_col:
#             #     ciphertext += matrix[(a_row + 1) % 5][a_col] + matrix[(b_row + 1) % 5][b_col]
#             # else:
#             #     ciphertext += matrix[a_row][b_col] + matrix[b_row][a_col]
#
#             return ciphertext
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
