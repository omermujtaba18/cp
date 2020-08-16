
def error_handling(text, key):

    # Error handling
    if type(text) is not str:
        raise TypeError('Plain text must be a string')

    if not all(x.isalpha() or x.isspace() for x in text):
        raise TypeError('Only alphabets or spaces are allowed in plain text')

    if type(key) is not int:
        raise TypeError('Key must be an integer')


def encrypt(plaintext: str, key: int):

    # Error handling
    error_handling(plaintext, key)

    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            islower = True if char.islower() else False

            char = char.lower()
            alpha_index = (ord(char)-19) % 26
            cipher_index = (alpha_index + key) % 26

            if islower:
                ciphertext += chr(cipher_index + 97)
            else:
                ciphertext += chr(cipher_index + 65)
        else:
            ciphertext += " "

    return ciphertext


def decrypt(ciphertext, key):

    # Error handling
    error_handling(ciphertext, key)

    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            islower = True if char.islower() else False

            char = char.lower()
            alpha_index = (ord(char) - 19) % 26
            plain_index = (alpha_index - key) % 26

            if islower:
                plaintext += chr(plain_index + 97)
            else:
                plaintext += chr(plain_index + 65)

        else:
            plaintext += " "

    return plaintext
