"""
    This file manages the user inputs and handles it to the respective cipher for encryption/decryption
    of the file contents, checks the user input if it holds the expected value type. After all the
    successful input from the user, the method outputs the encrypted/decrypted text in a separate file.
"""

from src.ciphers.caesar_cipher import CaesarCipher
from src.ciphers.atbash_cipher import AtbashCipher
from src.ciphers.vigenere_cipher import VigenereCipher


def file_output():
    """
    The file_output() method manages the user inputs and handles it to the respective
    cipher for encryption/decryption of the file contents, checks the user input if it
    holds the expected value type. After all the successful input from the user,
    the method outputs the encrypted/decrypted text in a separate file.

    :return: void
    """
    # Choose operation/action: "encrypt" or "decrypt"
    while True:
        operation = input("Do you want to encrypt or decrypt the message? (encrypt/decrypt): ")

        if operation not in ["encrypt", "decrypt"]:
            print("Please enter a valid operation (encrypt/decrypt). Check for grammar mistakes!")
        else:
            break

    # Write the name of the cipher the user wants to use
    while True:
        cipher_name = input('Enter the cipher name ("caesar", "atbash", or "vigenere"): ')

        # Defining a list of all allowed cipher classes
        allowed_ciphers = ["caesar", "Caesar", "CAESAR", "atbash", "Atbash", "ATBASH",
                           "vigenere", "Vigenere", "VIGENERE"]

        if cipher_name not in allowed_ciphers:
            print("Please enter a valid cipher name "
                  "(caesar, atbash, or vigenere). Check for grammar mistakes! ")
        else:
            # Map cipher name to a cipher class and ask for the
            # encryption/decryption key for each cipher respectively
            if cipher_name == "caesar":
                key_prompt = 'Enter the encryption key (integer expected): ' \
                    if operation == "encrypt" else 'Enter the decryption key (integer expected): '

                try:
                    key = int(input(key_prompt))
                    cipher = CaesarCipher(key)

                    input_text = str(input("Enter the message you would like to encrypt/decrypt: "))

                    output_text = cipher.encrypt(input_text, key) if operation == "encrypt" \
                        else cipher.decrypt(input_text, key)
                    break
                except ValueError:
                    print("Invalid input. Caesar cipher uses an integer key.")

            elif cipher_name == "atbash":   # The AtbashCipher does not need a key
                cipher = AtbashCipher()

                input_text = str(input("Enter the message you would like to encrypt or decrypt: "))
                output_text = cipher.encrypt(input_text, key="") \
                    if operation == "encrypt" else cipher.decrypt(input_text, key="")
                break

            elif cipher_name == "vigenere":
                key_prompt = 'Enter the encryption key (string expected): ' \
                    if operation == "encrypt" else 'Enter the decryption key (string expected): '

                # check that the key for vigenere cipher is only alphabetic [a-zA-Z]
                try:
                    while True:
                        key = input(key_prompt)
                        if key.isalpha():
                            break
                        print("The key can only contain alphabetic characters. Try again.")

                    cipher = VigenereCipher(key)

                    input_text = str(input("Enter the message you would like to encrypt/decrypt: "))
                    output_text = cipher.encrypt(input_text, key) if operation == "encrypt" \
                        else cipher.decrypt(input_text, key)
                    break
                except ValueError:
                    print("Invalid input. vigenere cipher uses a string (word) as a key.")

    if output_text.strip() == "":
        raise ValueError("Output text cannot be empty")

    # Ask and check for filename from the user
    filename = input('Enter the name of the output file: ')
    if filename.strip() == "":
        print("File name cannot be empty. Please enter a valid filename.")

    # Create file and write the output_text (encrypted/decrypted text) in the file
    try:
        with open(filename + ".txt", 'w') as file:
            file.write(output_text)
            print(f"Encrypted/Decrypted message has been written to the file: {filename}.txt.")

    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
