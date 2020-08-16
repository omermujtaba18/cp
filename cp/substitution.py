
def error_handling(text, key):

    # Error handling
    if type(text) is not str:
        raise TypeError('Plain text must be a string')

    if not all(x.isalpha() or x.isspace() for x in text):
        raise TypeError('Only alphabets or spaces are allowed in plain text')

    if type(key) is not str:
        raise TypeError('Key must be string')

    if not key.isalpha():
        raise TypeError('Key must be string of 26 alphabet characters only')


def encrypt(plaintext: str, key: int):

    # Error handling
    error_handling(plaintext, key)

    ciphertext = ""

    return ciphertext


def decrypt(ciphertext, key):

    # Error handling
    error_handling(ciphertext, key)

    plaintext = ""

    return plaintext
