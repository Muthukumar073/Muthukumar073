import hashlib

def hashlib_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password="HEY HI"
hashed=hashlib_password(password)
print(hashed)