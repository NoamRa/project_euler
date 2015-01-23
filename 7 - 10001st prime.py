"""
10001st prime


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?



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

primes = {}

i = 2
the_nth_prime = 10001
while len(primes) <= the_nth_prime+1:
	if is_prime(i):
		primes[len(primes) + 1] = i
		#print "new prime: " + str(i)
	i = i + 1

print primes[the_nth_prime]

print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 104743
"""