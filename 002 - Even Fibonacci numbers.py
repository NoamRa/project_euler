"""
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""
# fibo = {term: value}

fibo = {1: 1,
		2: 2,
		3: 3}
		
def calc_fibonachi(limit):
	term = 3
	while fibo[term - 1] < limit :
		fibo[term] = fibo[term - 1] + fibo[term - 2]
		term = term + 1
	return fibo

def sum_even_fibos(fibo):
	sum = 0
	for term in fibo:
		if fibo[term] % 2 == 0:
			sum = sum + fibo[term]
	return sum
fibo = calc_fibonachi(4000000)
print sum_even_fibos(fibo)


"""
answer is 4613732
"""
