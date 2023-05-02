from caesar_cipher import CaesarCipher
from atbash import AtbashCipher
from vignere_cipher import VignereCipher

if __name__ == '__main__':

    # Testing Caesar Cipher
    cipher = CaesarCipher(7)
    encrypted_message = cipher.encrypt("Hello world!", 7)
    decrypted_message = cipher.decrypt(encrypted_message)

    print(encrypted_message)
    print(decrypted_message)

    # Testing Playfair Cipher
    cipher2 = PlayfairCipher("Gravity")
    encrypted_message2 = cipher2.encrypt("HELLO WORLD", "Gravity")

    # Testing Atbash Cipher
    plaintext = "HELLO World"
    cipher3 = AtbashCipher()

    print(cipher3.encrypt(plaintext))
    print(cipher3.decrypt("SVOOL Dliow53212   ??!"))

    # Testing Vignere Cipher
    plain_text = "sunday"
    key = "michigan"
    cipher4 = VignereCipher("michigan")
    text = cipher4.encrypt(plain_text, key)
    print(text)
    print(cipher4.decrypt(text, key))