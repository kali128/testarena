import random
import string


def generate_string(length=5):
    alphabet = string.ascii_lowercase
    return ''.join(random.choice(alphabet) for i in range(length))
