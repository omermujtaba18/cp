# Crypto Python
A python package for Encryption/Decryption

### Crypto Algorithms
- Caeser Cipher
- Substitution Cipher

### Import package

```python

from cp.<caeser,substitution> import encrypt,decrypt

```

```python

plaintext = "Hello World"

# Caeser
ciphertext = encrypt(plaintext,key=1)
plaintext = decrypt(ciphertext,key=1)

# Substitution
key = generate_key()
ciphertext = encrypt(plaintext,key)
plaintext = decrypt(ciphertext,key)

```