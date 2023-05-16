import hashlib
h = hashlib.sha3_512(b"1").hexdigest()
print(h)