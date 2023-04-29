import unittest

from src.ciphers.caesar_cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):

    def test_caesar_encrypt(self):
        self.assertEqual(CaesarCipher.encrypt(CaesarCipher(3), "Hello world!", 3), "Khoor zruog!")
        self.assertEqual(CaesarCipher.encrypt(CaesarCipher(7), "Hello world!", 7), "Olssv dvysk!")
        self.assertEqual(CaesarCipher.encrypt(CaesarCipher(13), "Hello world!", 13), "Uryyb jbeyq!")

    def test_caesar_decrypt(self):
        self.assertEqual(CaesarCipher.decrypt(CaesarCipher(3), "Khoor zruog!"), "Hello world!")
        self.assertEqual(CaesarCipher.decrypt(CaesarCipher(7), "Olssv dvysk!"), "Hello world!")
        self.assertEqual(CaesarCipher.decrypt(CaesarCipher(13), "Uryyb jbeyq!"), "Hello world!")


if __name__ == '__main__':
    unittest.main()
    # test_caesar_encrypt()
