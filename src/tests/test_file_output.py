"""
    Filename: test_file_output.py
    This file holds the unittests for testing the file_output() method.
"""

import unittest
from unittest.mock import patch
from src.file_management.file_output import file_output


class TestFileOutput(unittest.TestCase):
    def test_caesar_decrypt(self):
        with patch('builtins.input', side_effect=['decrypt', 'caesar', '2', 'jgnnq', 'output']):
            file_output()
            with open('output.txt') as file:
                result = file.read()
            self.assertEqual(result.strip(), 'hello')

    def test_atbash_encrypt(self):
        with patch('builtins.input', side_effect=['encrypt', 'atbash', 'hello', 'output']):
            file_output()
            with open('output.txt') as file:
                result = file.read()
            self.assertEqual(result.strip(), 'svool')

    def test_atbash_decrypt(self):
        with patch('builtins.input', side_effect=['decrypt', 'atbash', 'svool', 'output']):
            file_output()
            with open('output.txt') as file:
                result = file.read()
            self.assertEqual(result.strip(), 'hello')

    def test_vigenere_encrypt(self):
        with patch('builtins.input', side_effect=['encrypt', 'vigenere', 'key', 'hello', 'output']):
            file_output()
            with open('output.txt') as file:
                result = file.read()
            self.assertEqual(result.strip(), 'rijvs')

    def test_vigenere_decrypt(self):
        with patch('builtins.input', side_effect=['decrypt', 'vigenere', 'key', 'rijvs', 'output']):
            file_output()
            with open('output.txt') as file:
                result = file.read()
            self.assertEqual(result.strip(), 'hello')


if __name__ == '__main__':
    unittest.main()
