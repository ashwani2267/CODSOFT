import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for complexity."
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lower + upper + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)


