# Encoder-and-Decoder
### Project description:
The Encoder and Decoder project creates a program which allows the user to encrypt plain text and/or 
decrypt encrypted text. The program encrypts and decrypts text by using different Ciphers. 
Currently, there are three ciphers available: Caesar Cipher, Atbash Cipher, and Vignere Cipher.

The main aims of this program are the following:
* To help teach others about ciphers, encryption, and decryption
* To encrypt and decrypt messages and/or passwords which will allow to have an additional basic 
level of security
* To entertain new computer scientists, teach them that coding is fun, and motivate them to learn 
more about the real-life implementation of coding projects

### Future features:
In the future, I intend to implement more complex ciphers such as poly


### Description of the problem:
•	Short (one or two paragraph) description of the problem.

### The solution:


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
│   ├── vignere_cipher.py
│   └── welcome.txt
│ └── file_management/
│   ├── __init__.py
│   ├── file_output.py
│   └── main.py
│ └── tests/
│   ├── __init__.py
│   ├── test_caesar_cipher.py
│   ├── test_vignere_cipher.py
│   ├── test_atbash_cipher.py
│   ├── test_cipher.py
│   ├── test_file_input.py
│   ├── test_file_output.py
│   └── test_main.py (ciphers main?)
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
- Child class atbash_cipher - 
- Child class vignere_cipher - 

### Special functions and/or algorithms used:
### The Ciphers:
1. Caesar Cipher - is a shift cipher which encrypts the data by replacing the original letters 
with “x” (key) number of characters ahead in the alphabet. Eg. The word "Hello world" with a key of 3
would encrypt to "Khoor zruog". 
2. Atbash Cipher - 
3. Vignere Cipher - 

### Getting started with the program:
•	Instructions how to start and work with the program
