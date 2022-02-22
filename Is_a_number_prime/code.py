# code
'''python'''

import math

def is_prime(num):
    listi = []
    if num < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                listi.append(i)
        if len(listi) == 0:
            return True
        else:
            return False
