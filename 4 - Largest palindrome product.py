"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 90 * 91 .

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time
start_time = time.time()

 


def is_palindrome(pali_int):
	pali_str = str(pali_int)
	if pali_str == pali_str[::-1]:
		return True
	else:
		return False

def largest_palindrome(num_of_digits):
	largest = 0
	x_max, y_max = 0, 0
	for x in reversed(xrange(10 ** num_of_digits)):
		for y in reversed(xrange(10 ** num_of_digits)):
			if is_palindrome(x*y) and x*y > largest:
				largest = x*y
				x_max, y_max = x, y

	print "The largest palindrome is: " + str(largest)
	print "The nultipliers are " + str(x_max) + " and " + str(y_max) 
	return 

largest_palindrome(4)


print "Time elapsed: %5.5f" % (time.time() - start_time)

"""
answer is 906609
made from 993 and 913
"""