import string
import random

def generate_random_string():
    TAM = 10
    chars = string.ascii_letters + string.digits + string.punctuation + "-_"
    random_string = ''.join(random.choice(chars) for _ in range(TAM))

    return random_string

def generate_url_to_redirect(end_point: str):
    BASE = "http://127.0.0.1:8000/redirect/"
    return BASE + end_point