"""
    Filename: test_vigenere_cipher.py
    This file holds the unittests for testing the VigenereCipher, its constructor,
    its encrypt() and decrypt() methods.
"""

import unittest
from src.ciphers.vigenere_cipher import VigenereCipher


class TestVigenereeCipher(unittest.TestCase):
    def setUp(self):
        self.obj = VigenereCipher()

    def test_get_key(self):
        self.assertEqual(self.obj.get_key(), 3)

    def test_set_key(self):
        self.assertEqual(self.obj.get_key(), 3)

    def test_vigenere_encrypt_success(self):
        self.assertEqual(VigenereCipher.encrypt(VigenereCipher(), "Hello world!", "HI"), "omstv evzsl!")
        self.assertEqual(VigenereCipher.encrypt(VigenereCipher(), "hallooooo", "bye"), "iypmmspms")
        self.assertEqual(VigenereCipher.encrypt(VigenereCipher(), "University", "encrypt"), "yakmcglmga")
        
    def test_vigenere_encrypt_fail(self):
        self.assertNotEqual(VigenereCipher.encrypt(VigenereCipher(), "Hello world!", "hi"), "Hi zruog!")
        self.assertNotEqual(VigenereCipher.encrypt(VigenereCipher(), "Hello world!", "merci"), "Olssv htfd!")
        self.assertNotEqual(VigenereCipher.encrypt(VigenereCipher(), "Hello world!", "abcd"), "Uryyb htbuju!")
        
    def test_vigenere_decrypt_success(self):
        self.assertEqual(VigenereCipher.decrypt(VigenereCipher(), "omstv evzsl!", "HI"), "hello world!")
        self.assertEqual(VigenereCipher.decrypt(VigenereCipher(), "iypmmspms", "bye"), "hallooooo")
        self.assertEqual(VigenereCipher.decrypt(VigenereCipher(), "yakmcglmga", "encrypt"), "university")

    def test_vigenere_decrypt_fail(self):
        self.assertNotEqual(VigenereCipher.decrypt(VigenereCipher(), "Khoor zruog!"), "Hi world!")
        self.assertNotEqual(VigenereCipher.decrypt(VigenereCipher(), "Olssv dvysk!"), "Hello people!")
        self.assertNotEqual(VigenereCipher.decrypt(VigenereCipher(), "Uryyb jbeyq!"), "Python 123!")


if __name__ == '__main__':
    unittest.main()
