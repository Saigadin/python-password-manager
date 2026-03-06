from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(master_password):
    password = master_password.encode()
    key = hashlib.sha256(password).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_data(data, master_password):
    key = generate_key(master_password)
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt_data(data, master_password):
    key = generate_key(master_password)
    f = Fernet(key)
    return f.decrypt(data.encode()).decode()