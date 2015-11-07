# coding: utf-8
"""
020 - Factorial digit sum

n! means n x (n − 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


"""

import time
start_time = time.time()

import math

n = 100

def sum_factorial_digits(n):
	x = math.factorial(n)
	s = 0
	while x:
		s += x % 10
		x /= 10
	return s

print sum_factorial_digits(n)








print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 
"""