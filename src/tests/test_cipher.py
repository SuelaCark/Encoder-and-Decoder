"""
    Filename: test_cipher.py
    This file holds the unittests for testing the Cipher (superclass), its constructor,
    its encrypt() and decrypt() methods.
"""

import unittest
from mock import patch
from src.ciphers.cipher import Cipher


class TestCipher(unittest.TestCase):
    @patch.multiple(Cipher, __abstractmethods__=set())
    def test_constructor(self):
        self.instance = Cipher()

    def test_get_key(self):
        self.assertEqual(self.instance.get_key(), 5)

    def test_set_key(self):
        self.assertEqual(self.instance.get_key(), 5)

    def test_encrypt_not_implemented(self):
        self.assertRaises(NotImplementedError)

    def test_decrypt_not_implemented(self):
        self.assertRaises(NotImplementedError)


if __name__ == '__main__':
    unittest.main()
