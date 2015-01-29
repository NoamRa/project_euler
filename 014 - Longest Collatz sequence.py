"""
Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


"""

import time
start_time = time.time()

def collatz(n):
	# returns number of steps it takes to get from n to 1.
	steps = 1
	while n > 1:
		if (n % 2) == 0:
			n = n / 2
		else:
			n = n * 3 + 1
		steps += 1
	return steps

limit = 1000000

def most_collatz_steps(limit):
	most_steps_number = 1
	max_steps = 1
	for i in xrange(limit):
		steps = collatz(i)
		if steps > max_steps:
			most_steps_number = i
			max_steps = steps

	print most_steps_number
	print max_steps

most_collatz_steps(limit)


print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 837799
it has 525 steps
"""