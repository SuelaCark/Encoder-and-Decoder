"""
    The main method of the whole Encoder-and-Decoder program which prints a welcoming
    message and a short description of the use of the program. The main method calls the
    file_output() method which asks the user for input, manages and checks the user inputs,
    directs to the respective ciphers and encrypt/decrypt method, and finally it outputs
    the encrypted/decrypted message in the newly created file.
"""

from src.file_management.file_output import file_output


if __name__ == '__main__':
    print("Welcome to the Encoder and Decoder program! This program will allow you to "
          "encrypt and decrypt messages in existing files within the project directory.")
    file_output()
