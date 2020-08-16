
import random


def error_handling(text, key):

    # Error handling
    if type(text) is not str:
        raise TypeError('Plain text must be a string')

    if not all(x.isalpha() or x.isspace() for x in text):
        raise TypeError('Only alphabets or spaces are allowed in plain text')

    if type(key) is not str or len(key) != 26:
        raise TypeError('Key must be string of 26 characters')

    if len(list(key)) != len(set(key)):
        raise TypeError('Key cannot have duplicate characters')


def generate_key():
    char_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(char_list)
    return ''.join(char_list)


def encrypt(plaintext: str, key: str):

    # Error handling
    error_handling(plaintext, key)

    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            islower = True if char.islower() else False

            char = char.lower()
            alpha_index = (ord(char) - 19) % 26

            for i in range(0, 25):
                if(i == alpha_index):
                    cipher = key[i].lower()
                    ciphertext += cipher if islower else cipher.upper()
        else:
            ciphertext += char

    return ciphertext


def decrypt(ciphertext, key):

    # Error handling
    error_handling(ciphertext, key)

    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            islower = True if char.islower() else False

            char = char.lower()
            key = key.lower()

            for i in range(0, 25):
                if(char == key[i]):
                    plain = chr(i+97)
                    plaintext += plain if islower else plain.upper()

        else:
            plaintext += char

    return plaintext
