# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from cipher import Cipher
from caesar_cipher import CaesarCipher

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    c1 = Cipher
    print(c1)

    text = "CEASER CIPHER DEMO"
    s = 4

    c2 = CaesarCipher
    c2.encrypt(text, s)

