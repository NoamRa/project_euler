"""
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
start_time = time.time()

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

limit = 2000000

def sum_primes(limit):
	sum_of_primes = 0
	for i in xrange(2, limit):
		if is_prime(i):
			sum_of_primes = sum_of_primes + i
	return sum_of_primes

print sum_primes(limit)







print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 
"""