"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


import math 

import time
start = time.time()

prime_to_check = 600851475143
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def find_largest_factor(prime_to_check):
	i = math.trunc(math.sqrt(prime_to_check))
	#print i
	largest_factor = 2
	while largest_factor < i:
		if is_prime(i) and (prime_to_check % i) == 0:
			largest_factor = i
			break
		i = i - 1

	return largest_factor
		
print find_largest_factor(prime_to_check)
print "Time elapsed: %5.2f" % (time.time() - start)

"""
answer is 6857
"""