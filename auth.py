import hashlib
import os

MASTER_FILE = "master.hash"

def set_master_password(password):

    hashed = hashlib.sha256(password.encode()).hexdigest()

    with open(MASTER_FILE, "w") as f:
        f.write(hashed)


def verify_master_password(password):

    if not os.path.exists(MASTER_FILE):
        set_master_password(password)
        return True

    with open(MASTER_FILE) as f:
        stored = f.read()

    return stored == hashlib.sha256(password.encode()).hexdigest()