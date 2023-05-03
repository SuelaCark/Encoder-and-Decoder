# import unittest
# from io import StringIO
# from unittest.mock import patch
# from src.ciphers.caesar_cipher import CaesarCipher
# from src.ciphers.atbash_cipher import AtbashCipher
# from src.ciphers.vignere_cipher import VignereCipher
# from src.file_management.file_output import process_input
#
#
# class TestProcessInput(unittest.TestCase):
#     def test_caesar_encrypt(self):
#         self.assertEquals()
#         # with patch('builtins.input', side_effect=['encrypt', 'caesar', '2', 'hello', 'output']):
#         #     process_input()
#         #     with open('output.txt') as f:
#         #         result = f.read()
#         #     self.assertEqual(result.strip(), 'jgnnq')
#
#     def test_caesar_decrypt(self):
#         with patch('builtins.input', side_effect=['decrypt', 'caesar', '2', 'jgnnq', 'output']):
#             process_input()
#             with open('output.txt') as f:
#                 result = f.read()
#             self.assertEqual(result.strip(), 'hello')
#
#     def test_atbash_encrypt(self):
#         with patch('builtins.input', side_effect=['encrypt', 'atbash', 'hello', 'output']):
#             process_input()
#             with open('output.txt') as f:
#                 result = f.read()
#             self.assertEqual(result.strip(), 'svool')
#
#     def test_atbash_decrypt(self):
#         with patch('builtins.input', side_effect=['decrypt', 'atbash', 'svool', 'output']):
#             process_input()
#             with open('output.txt') as f:
#                 result = f.read()
#             self.assertEqual(result.strip(), 'hello')
#
#     def test_vignere_encrypt(self):
#         with patch('builtins.input', side_effect=['encrypt', 'vignere', 'key', 'hello', 'output']):
#             process_input()
#             with open('output.txt') as f:
#                 result = f.read()
#             self.assertEqual(result.strip(), 'hfnlp')
#
#     def test_vignere_decrypt(self):
#         with patch('builtins.input', side_effect=['decrypt', 'vignere', 'key', 'hfnlp', 'output']):
#             process_input()
#             with open('output.txt') as f:
#                 result = f.read()
#             self.assertEqual(result.strip(), 'hello')
#
#     def test_invalid_operation(self):
#         with patch('builtins.input', side_effect=['invalid', 'encrypt', 'caesar', '2', 'hello', 'output']):
#             with self.assertRaises(SystemExit):
#                 process_input()
#
#     def test_invalid_cipher_name(self):
#         with patch('builtins.input', side_effect=['encrypt', 'invalid', 'caesar', '2', 'hello', 'output']):
#             with self.assertRaises(SystemExit):
#                 process_input()
#
#     def test_invalid_caesar_key(self):
#         with patch('builtins.input', side_effect=['encrypt', 'caesar', 'invalid', 'hello', 'output']):
#             with self.assertRaises(ValueError):
#                 process_input()
#
#     def test_invalid_vignere_key(self):
#         with patch('builtins.input', side_effect=['encrypt', 'vignere', '123', 'hello', 'output']):
#             with self.assertRaises(ValueError):
#                 process_input()
#
#     def test_empty_output_filename(self):
#         with patch('builtins.input', side_effect=['encrypt', 'caesar', '2', 'hello', '']):
#             with self.assertRaisesRegex(SystemExit, 'File name cannot be empty'):
#                 process_input()
#
#     def test_file_not_found(self):
#         with patch('builtins.input', side_effect=['encrypt', 'caesar', '2', 'hello', 'does_not_exist/output']):
#             with self.assertRaisesRegex(FileNotFoundError, 'File not found'):
#                 process_input()
#
#
# if __name__ == '__main__':
#     unittest.main()
