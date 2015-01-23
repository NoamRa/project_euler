
"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiples(naturals, below_num):
	# Return a list of integers that are the multiples of 
	# naturals and are smaller than below_num.
	# Using set to discard duplicates.
	set_to_sum = set()
	for nat in naturals:
		for i in range(below_num):
			if (i!= 0) and (i % nat) == 0:
				#print i
				set_to_sum.add(i)
	set(set_to_sum)
	return 	set_to_sum		

def sum_list(set_to_sum):
	# sums a list of integers
	s = 0
	for i in set_to_sum:
		#print i
		s = s + i
	return s	

set_to_sum = multiples([3, 5], 1000)
print set_to_sum
print sum_list(set_to_sum)

"""
answer is 233168

"""