import hashlib
import os

def generate_secure_hash():
    random_data = os.urandom(16)
    return hashlib.sha256(random_data).hexdigest()
