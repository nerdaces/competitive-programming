import math

def is_prime(x):
    if x <= 1:
        return False
    for k in range(2, int(math.sqrt(x)) + 1):
        if x % k == 0:
            return False
    return True