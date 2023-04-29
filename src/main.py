# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string

# from cipher import Cipher
from caesar_cipher import CaesarCipher


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    cipher = CaesarCipher(1, 3)
    encrypted_message = cipher.encrypt("HELLO, misterY!")

    decrypted_message = cipher.decrypt(encrypted_message)

    print(encrypted_message)
    print(decrypted_message)


