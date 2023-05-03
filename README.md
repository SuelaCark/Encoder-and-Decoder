# Encoder-and-Decoder
### Project description:
The Encoder and Decoder project creates a program which allows the user to encrypt plain text and/or 
decrypt encrypted text. The program encrypts and decrypts text by using different Ciphers. 
Currently, there are three ciphers available: Caesar Cipher, Atbash Cipher, and Vigenere Cipher.

The main aims of this program are the following:
* To help teach others about ciphers, encryption, and decryption
* To encrypt and decrypt messages and/or passwords which will allow to have an additional basic 
level of security
* To entertain new computer scientists, teach them that coding is fun, and motivate them to learn 
more about the real-life implementation of coding projects

### Future features:
In the future, I intend to implement:
- More complex ciphers
- Graphic User Interface
- Get file input for encrypting/decrypting


### Description of the problem and its solution:
Cybersecurity as a field is growing to be more crucial day-by-day. Our everyday usage of online sources 
with the security of our passwords lead to security vulnerabilities. While each password is encrypted by 
using hash mapping and other encryption/mapping methods, sometimes the passwords can still be breakable
due to the correlation of the password with the user's life, eg. password which holds the user's dog name.
Hence, to prevent this direct breaking of user passwords, I decided to create a cipher encoder and decoder
project which allows anyone to give an additional layer of security to their passwords. 


### Project structure:
```
Encoder-and-Decoder/
├── htmlcov
│ ├── index.html
│ └── ...
├── src
│ └── ciphers/
│   ├── __init__.py
│   ├── atbash_cipher.py
│   ├── caesar_cipher.py
│   ├── cipher.py
│   ├── main.py
│   └──vigenere_cipher.py
│ └── file_management/
│   ├── __init__.py
│   └── file_output.py
│ └── tests/
│   ├── __init__.py
│   ├── test_atbash_cipher.py
│   ├── test_caesar_cipher.py
│   ├── test_cipher.py
│   ├── test_file_output.py
│   └── test_vigenere_cipher.py
│
│ └── .coverage
│ └── __init__.py
│
├── .coverage
└──  README.md
```

## Class structure and  description
The OOP inheritance is used to create the implementation of the ciphers. The following is the inheritance structure:
- Abstract super class Cipher - initial constructor with an optional parameter (key). Getters and setters for the key.
Two abstract methods encrypt() and decrypt() which are not implemented (this will allow child classes to have their own 
implementation of the methods)
- Child class caesar_cipher - initial constructor which class the super class constructor. The implementation of the
encrypt() and decrypt() abstract methods from the superclass to suit the Caesar cipher. 
- Child class atbash_cipher - initial constructor which class the super class constructor. The implementation of the
encrypt() and decrypt() abstract methods from the superclass to suit the Atbash cipher. 
- Child class vigenere_cipher - initial constructor which class the super class constructor. The implementation of the
encrypt() and decrypt() abstract methods from the superclass to suit the Vigenere cipher. 

### Special functions and/or algorithms used:
### The Ciphers used:
1. Caesar Cipher - is a shift cipher which encrypts the data by replacing the original letters 
with “x” (key) number of characters ahead in the alphabet. Eg. The word "Hello world" with a key of 3
would encrypt to "Khoor zruog". 
2. Atbash Cipher - The Atbash Cipher is a monoalphabetic substitution cipher that, in comparison 
        to other ciphers e.g. Caesar Cipher, does not require an encryption key.
        The Atbash Cipher maps each letter of an alphabet it to its reverse, 
        so that the first letter (e.g. A) becomes the last letter (e.g. Z), 
        the second letter (B) becomes the second to last letter (Y), and so on.
3. Vigenere Cipher - Vigenere Cipher is an encryption and decryption algorithm. 
It is a type of polyalphabetic substitution cipher, which means that the cipher 
alphabet is changed regularly during the encryption process. The encryption key word is split
into single characters and become part of the beginning rows of the alphabet matrix.

### Getting started with the program:
First way:
1. In the git repository click the green button (Code)
2. Click the SSH button and copy the SSH key
3. Create an empty folder and open it with pycharm
4. On the pycharm, open the terminal, and write: git clone <SSH key>
5. After the project is copied, open the folders src > ciphers > main.py (file)
6. Run main.py

Second way:
1. In the git repository click the green button (Code)
2. Download Zip (which downloads the whole project into your computer)
3. Unzip the project's git folder
4. Open the unzipped project folder in pycharm
5. After opening the project, open the folders src > ciphers > main.py (file)
6. Run main.py

Testing commands:
- Test unittests in terminal (one of the following): 
  - python3 -m unittest discover -s tests -t src
  - python -m unittest discover
- Coverage:
  - Not include tests: coverage run --source . --omit=venv --omit=test* -m unittest discover 
  - coverage run -m unittest discover
  - coverage html
  - coverage report (same as coverage html but output in terminal)


