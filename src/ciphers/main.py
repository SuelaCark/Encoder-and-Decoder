'''
TODO:   1. Comments of all files and what they do
        2. DocString method documentation
        3. README.md (include instructions on how to run the project)
        4. Video
'''

from src.ciphers.caesar_cipher import CaesarCipher
from src.file_management.file_output import process_input


if __name__ == '__main__':
    print("Welcome to the Encoder and Decoder program!"
          "This program will allow you to encrypt and decrypt messages in existing files within the project directory.")
    process_input()


    # # Testing Caesar Cipher
    # cipher = CaesarCipher(7)
    # encrypted_message = cipher.encrypt("Hello world!", 7)
    # decrypted_message = cipher.decrypt(encrypted_message)
    #
    # print(encrypted_message)
    # print(decrypted_message)
    #
    # # Testing Playfair Cipher
    # cipher2 = PlayfairCipher("Gravity")
    # encrypted_message2 = cipher2.encrypt("HELLO WORLD", "Gravity")
    #
    # # Testing Atbash Cipher
    # plaintext = "HELLO World"
    # cipher3 = AtbashCipher()
    #
    # print(cipher3.encrypt(plaintext))
    # print(cipher3.decrypt("SVOOL Dliow53212   ??!"))
    #
    # # Testing Vignere Cipher
    # plain_text = "sunday"
    # key = "michigan"
    # cipher4 = VignereCipher("michigan")
    # text = cipher4.encrypt(plain_text, key)
    # print(text)
    # print(cipher4.decrypt(text, key))
