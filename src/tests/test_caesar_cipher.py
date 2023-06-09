"""
    Filename: test_caesar_cipher.py
    This file holds the unittests for testing the CaesarCipher, its constructor,
    its encrypt() and decrypt() methods.
"""

import unittest
from src.ciphers.caesar_cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.obj = CaesarCipher(3)

    def test_get_key(self):
        self.assertEqual(self.obj.get_key(), 3)

    def test_set_key(self):
        self.assertEqual(self.obj.get_key(), 3)

    def test_caesar_encrypt_success(self):
        self.assertEqual(CaesarCipher.encrypt(CaesarCipher(3), "Hello world!", 3), "Khoor zruog!")
        self.assertEqual(CaesarCipher.encrypt(CaesarCipher(7), "Hello world!", 7), "Olssv dvysk!")
        self.assertEqual(CaesarCipher.encrypt(CaesarCipher(13), "Hello world!", 13), "Uryyb jbeyq!")

    def test_caesar_encrypt_fail(self):
        self.assertNotEqual(CaesarCipher.encrypt(CaesarCipher(3), "Hello world!", 3), "Hi zruog!")
        self.assertNotEqual(CaesarCipher.encrypt(CaesarCipher(7), "Hello world!", 7), "Olssv htfd!")
        self.assertNotEqual(CaesarCipher.encrypt(CaesarCipher(13), "Hello world!", 13), "Uryyb htbuju!")

    def test_is_alpha(self):
        self.assertEqual(self.obj.encrypt("text", 3).isalpha(), True)

    def test_is_not_alpha(self):
        self.assertEqual(self.obj.encrypt("text35!", 3).isalpha(), False)

    def test_caesar_decrypt_success(self):
        self.assertEqual(CaesarCipher.decrypt(CaesarCipher(3), "Khoor zruog!"), "Hello world!")
        self.assertEqual(CaesarCipher.decrypt(CaesarCipher(7), "Olssv dvysk!"), "Hello world!")
        self.assertEqual(CaesarCipher.decrypt(CaesarCipher(13), "Uryyb jbeyq!"), "Hello world!")

    def test_caesar_decrypt_fail(self):
        self.assertNotEqual(CaesarCipher.decrypt(CaesarCipher(3), "Khoor zruog!"), "Hi world!")
        self.assertNotEqual(CaesarCipher.decrypt(CaesarCipher(7), "Olssv dvysk!"), "Hello people!")
        self.assertNotEqual(CaesarCipher.decrypt(CaesarCipher(13), "Uryyb jbeyq!"), "Python 123!")


if __name__ == '__main__':
    unittest.main()
