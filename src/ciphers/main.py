from caesar_cipher import CaesarCipher
from atbash_cipher import AtbashCipher
from vignere_cipher import VignereCipher
from src.file_management.file_input import FileReader

if __name__ == '__main__':
    print("Welcome to the Encoder and Decoder program!"
          "This program will allow you to encrypt and decrypt messages in existing files within the project directory.")

    file_name = str(input("Please input an existing file name: "))
    file_reader = FileReader(file_name)
    file_reader.read_file(file_name)

    # file_name = str(input("Please input your existing file name: "))
    # mode = str(input("Please enter 'encrypt' (e) if you wish to encrypt the file contents, or enter 'decrypt' (d) "
    #                  "if you wish to decrypt the file contents: "))
    # cipher_name = str(input("Please enter one of the following ciphers which you would like to use: "
    #                         "Caesar, Atbash, Vignere: "))



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
