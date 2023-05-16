import hashlib
h = hashlib.pbkdf2_hmac('sha512', b'damipass', b'salt', 100000).hex()
print(h)