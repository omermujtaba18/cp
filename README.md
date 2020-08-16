# Crypto Python
A python package for Encryption/Decryption

### Crypto Algorithms
- Caeser Cipher
- Substitution Cipher
- Deffie-Hellman Key Exchange

### How to use

##### Caeser Cipher

```python

from cp.<caeser,substitution> import encrypt,decrypt

plaintext = "Hello World"

ciphertext = encrypt(plaintext,key=1)
plaintext = decrypt(ciphertext,key=1)

```

##### Substitution Cipher

```python

from cp.substitution import encrypt,decrypt,generate_key

plaintext = "Hello World"

key = generate_key()
ciphertext = encrypt(plaintext,key)
plaintext = decrypt(ciphertext,key)

```