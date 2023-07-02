import random
import string
from datetime import datetime, timedelta


def generate_string(length=5):
    alphabet = string.ascii_lowercase
    return ''.join(random.choice(alphabet) for i in range(length))


def get_date(offset_days=0):
    date = datetime.now() + timedelta(days=offset_days)
    return date
