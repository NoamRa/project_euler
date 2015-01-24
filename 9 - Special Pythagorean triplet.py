"""
Special Pythagorean triplet



A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.



"""

import time
start_time = time.time()

triplet_sum = 1000

def find_triplet(triplet_sum):
	for c in xrange(triplet_sum/2, 1, -1):
		for b in xrange(c-1, 1, -1):
			for a in xrange(b-1, 1, -1):
				if a+b+c == triplet_sum:
					if (a**2) + (b**2) == (c**2):
						#print a, b, c
						return a*b*c
	print "There's no triplet who's sum is " + str(triplet_sum)
	return None

print find_triplet(triplet_sum)			



print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 31875000
the triplet are 200 375 425
"""