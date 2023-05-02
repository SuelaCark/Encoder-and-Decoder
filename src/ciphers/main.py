# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string

# from cipher import Cipher
from caesar_cipher import CaesarCipher
from playfair_cipher import PlayfairCipher

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ...
    # Testing Caesar Cipher
    cipher = CaesarCipher(7)
    encrypted_message = cipher.encrypt("Hello world!", 7)
    decrypted_message = cipher.decrypt(encrypted_message)

    print(encrypted_message)
    print(decrypted_message)

    # Testing Playfair Cipher
    # cipher2 = PlayfairCipher("Gravity")
    # encrypted_message2 = cipher2.encrypt("HELLO WORLD", "Gravity")
