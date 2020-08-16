# Crypto Python
A python package for Encryption/Decryption

### Crypto Algorithms
- Caeser Cipher
- Substitution Cipher

### How to use

```python
from cp.caeser import encrypt,decrypt

plaintext = "Hello World"
ciphertext = encrypt(plaintext,1)

ciphertext = "Hello World"
plaintext = decrypt(ciphertext,1)

```