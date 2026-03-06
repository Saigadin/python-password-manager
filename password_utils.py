import secrets
import string
import re

def generate_password(length=12):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for i in range(length))

    return password

def check_strength(password):

    length = len(password) >= 8
    digit = re.search(r"\d", password)
    upper = re.search(r"[A-Z]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([bool(length), bool(digit), bool(upper), bool(special)])

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    else:
        return "Strong"
