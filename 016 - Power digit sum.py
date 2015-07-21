"""
Power digit sum
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?



"""

import time
start_time = time.time()

num = 2**1000
num_to_sum = str(num)
c = 0
for i in num_to_sum:
	c = c + int(i)

print c

print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 1366
"""