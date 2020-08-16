# p,g are shared globally for alice and bob
# 1. alice use generate_key with its secret int
# 2. bob use generate_key with its secret int
# 3a. Alice send bob the generate_key value
# 3b. Bob use retrieve_key with its secret int to get shared secret
# 4a. Bob send alice the generate_key value
# 4b. Alice use retrieve_key with its secret int to get shared secret


def generate_key(p, g, secret_int):
    return (g ** secret_int) % p


def retrieve_key(p, key, secret_int):
    return (key ** secret_int) % p
