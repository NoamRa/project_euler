# coding: utf-8
"""
021 - Amicable numbers


Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

import time
start_time = time.time()

import math

def list_proper_divisors(n):
	# return a list of proper divisors (sorted for convenience)
	proper_divisors_set = set([1])
	for x in xrange(1, n):
		i = n/x
		f = n/float(x)
		if i == f and i < n:
			proper_divisors_set.add(i)
	return sorted(proper_divisors_set)


#print list_proper_divisors(220)
#print list_proper_divisors(284)

def is_amicable_pair(a):
	da = sum(list_proper_divisors(a))
	b = da
	db = sum(list_proper_divisors(b))
	
	if a!= b and da == b and db == a :
		return a , da
	else:
		return False

#print is_amicable_pair(220)

limit = 10000
s = set([])
for a in xrange(1, limit+1):
	pair = is_amicable_pair(a)
	if pair:
		a, b = pair[0], pair[1]
		s.add(a)
		s.add(b)

print s
print sum(s)

print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 31626
set([1184, 6368, 220, 5020, 2924, 6232, 1210, 5564, 284, 2620])

"""