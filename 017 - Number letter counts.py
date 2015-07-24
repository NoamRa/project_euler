"""
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.



"""

import time
start_time = time.time()

num = 1000

words = {
	0 : "",
	1 : "one",
	2 : "two",
	3 : "three",
	4 : "four",
	5 : "five",
	6 : "six",
	7 : "seven",
	8 : "eight",
	9 : "nine",
	10 : "ten",
	11 : "eleven",
	12 : "twelve",
	13 : "thirteen",
	14 : "fourteen",
	15 : "fifteen",
	16 : "sixteen",
	17 : "seventeen",
	18 : "eighteen",
	19 : "nineteen",
	20 : "twenty",
	30 : "thirty",
	40 : "forty",
	50 : "fifty",
	60 : "sixty",
	70 : "seventy",
	80 : "eighty",
	90 : "ninety",
	100 : "oneHundred",
	200 : "twoHundred",
	300 : "threeHundred",
	400 : "fourHundred",
	500 : "fiveHundred",
	600 : "sixHundred",
	700 : "sevenHundred",
	800 : "eightHundred",
	900 : "nineHundred",
	1000 : "oneThousand",
	"and" : "and"
}


def split_digits(num):
	num_list = []
	ten = 0
	for i in (str(num)[::-1]):
		#print i, int(i) * 10**ten
		if ten == 1 and i == "1":
			#print "NUMBER IS",num%100
			num_list = []
			num_list.append(num%100)
		else:
			num_list.append(int(i) * 10**ten)
		ten = ten + 1
	num_list = filter(None, num_list)
	if (ten > 2) and (len(num_list) >= 2):
		#print ten, len(num_list)
		num_list.append("and")
	
	return num_list

def nums_to_words(num_list):
	c = 0
	for i in num_list:
		#print words[i]
		c = c + len(words[i])
	

	
	for i in num_list[::-1]:
		if len(num_list) > 2:
			#print i
			print words[i]
	
	print
	return c

c = 0
for n in xrange(num):

	number_word_length = nums_to_words(split_digits(n+1))
	c = c + number_word_length

print "The sum of letters counting to", num, "is", c


print "Time elapsed: %5.3f" % (time.time() - start_time)

"""
answer is 21124
"""