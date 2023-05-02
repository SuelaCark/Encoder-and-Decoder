'''
TODO:   2. File writer + connect it to the ciphers
        3. Unit Testing!!!
        4. Coverage report!! (without tests)
        5. Check for exceptions and verifications of parameters!
        6. Comments of all files and what they do
        7. DocString method documentation
        8. PEP8
        9. README.md (include instructions on how to run the project)
        10. Video
'''

# from src.ciphers.file_output import FileReader
from src.ciphers.caesar_cipher import CaesarCipher
from src.file_management.file_output import process_input


if __name__ == '__main__':
    print("Welcome to the Encoder and Decoder program!"
          "This program will allow you to encrypt and decrypt messages in existing files within the project directory.")

    process_input()

    """
        Note: To store the file names you could use either constants or configuration file ( configparser to parse it). 
        Or you could pass them when you run the python script and use argparse for that.
    """


    # cipher_name = str(input("Please enter one of the following ciphers which you would like to use: "
    #                         "Caesar, Atbash, Vignere: "))
    #
    # if cipher_name == "Caesar":
    #     ...
    # elif cipher_name == "Atbash":
    #     ...
    # elif cipher_name == "Vignere":
    #     ...
    # else:
    #     raise ValueError("The available ciphers are: Caesar, Atbash, and Vignere")

    # file_reader = FileReader(file_name)
    # file_reader.read_file(file_name)

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
