"""
Sum square difference



The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


"""

import time
start_time = time.time()

def square_sum(num):
	s = 0
	for i in xrange(num+1):
		s = s + i
	s = s**2
	print s
	return s


def sum_of_squares(num):
	s = 0
	for i in xrange(num+1):
		s = s + i**2
	print s
	return s


num = 100

print square_sum(num) - sum_of_squares(num)




print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 25164150
"""