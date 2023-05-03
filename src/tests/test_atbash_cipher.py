"""
    Filename: test_atbash_cipher.py
    This file holds the unittests for testing the AtbashCipher, its constructor,
    its encrypt() and decrypt() methods.
"""

import unittest
from src.ciphers.atbash_cipher import AtbashCipher


class TestAtbashCipher(unittest.TestCase):
    def setUp(self):
        self.obj = AtbashCipher()

    def test_atbash_encrypt_success(self):
        self.assertEqual(AtbashCipher.encrypt(AtbashCipher(), "Hello world!"), "Svool dliow!")
        self.assertEqual(AtbashCipher.encrypt(AtbashCipher(), "Python"), "Kbgslm")
        self.assertEqual(AtbashCipher.encrypt(AtbashCipher(), "Encrypt"), "Vmxibkg")

    def test_atbash_encrypt_fail(self):
        self.assertNotEqual(AtbashCipher.encrypt(AtbashCipher(), "Hello world!"), "Svool happy!")
        self.assertNotEqual(AtbashCipher.encrypt(AtbashCipher(), "Python"), "Java")
        self.assertNotEqual(AtbashCipher.encrypt(AtbashCipher(), "Encrypt"), "Decrypt")

    def test_atbash_decrypt_success(self):
        self.assertEqual(AtbashCipher.decrypt(AtbashCipher(), "Svool dliow!"), "Hello world!")
        self.assertEqual(AtbashCipher.decrypt(AtbashCipher(), "Kbgslm"), "Python")
        self.assertEqual(AtbashCipher.decrypt(AtbashCipher(), "Vmxibkg"), "Encrypt")

    def test_atbash_decrypt_fail(self):
        self.assertNotEqual(AtbashCipher.decrypt(AtbashCipher(), "Svool dliow!"), "Hello globe!")
        self.assertNotEqual(AtbashCipher.decrypt(AtbashCipher(), "Kbgslm"), "Zdraveite")
        self.assertNotEqual(AtbashCipher.decrypt(AtbashCipher(), "Vmxibkg"), "Flag")


if __name__ == '__main__':
    unittest.main()
