import unittest
from abc import ABC, abstractmethod
from src.ciphers.cipher import Cipher


class TestCipher(unittest.TestCase):
    def setUp(self) -> None:
        self.cipher = Cipher()

    # def test_abstract_methods(self):
    #     with self.assertRaises(TypeError):
    #         self.cipher.encrypt("test")
    #     with self.assertRaises(TypeError):
    #         self.cipher.decrypt("test")

    def test_set_key(self):
        self.cipher.set_key("hi")
        self.assertTrue(self.cipher.get_key() == "hi")

    # def test_encrypt(self, file_text, key):
    #     return file_text[::-1] + str(key)
    #
    # def test_decrypt(self, file_text, key=""):
    #     return file_text[:-1][::-1]

        # cipher = TestCipherImpl()
        # file_text = "hello world"
        # key = 5
        #
        # encrypted_text = cipher.encrypt(file_text, key)
        # decrypted_text = cipher.decrypt(encrypted_text, key)
        #
        # self.assertEqual(decrypted_text, file_text[::-1])


if __name__ == '__main__':
    unittest.main()
