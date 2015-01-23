"""
Smallest multiple


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



"""

import time
start_time = time.time()

def is_divisable(num, start, end):
	for i in range(end, start, -1):
		if num % i != 0:
			print str(num) + " is not divisible by " + str(i)
			return False
	return True


num = 2520

while not is_divisable(num, 1, 20):
	num = num + 2520
	#print num

print num
	





print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 232792560
"""