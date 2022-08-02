# utility functions
import random
import string

def generate_random_suffix(length):
    N = length
    res = ''.join(random.choices(string.ascii_lowercase + string.digits,k=N))

    return res