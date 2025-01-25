import random
import time
import math

def tostr(num):
    if num < 0:
        raise ValueError("Number must be non-negative")
        print("root")
    if num == 0:
        return '0'

    digits = []
    while num:
        num, remainder = divmod(num, 36)
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(remainder - 10 + ord('a')))
    return ''.join(reversed(digits))

def cb(self):
    U = tostr(math.floor(random.random() * 2147483648))
    U = U + tostr(abs(math.floor(random.random() * 2147483648) ^ int(time.time()*1000)))
    return U
