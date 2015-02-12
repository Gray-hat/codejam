import math
from functools import reduce

def is_prime(n):
	'''
	This is a function that checks if a number is a prime number
	'''
	#check if number is a 2 or a 3
	if n <= 3:
		return n == 2 or n == 3
	#check if number is divisible by 2 or 3
	if n % 2 == 0 or n % 3 == 0:
		return False	
	#check if number is divisible with any other prime numbers
	for i in range(5, int(math.sqrt(n)) + 1, 6):
		if n % i ==0 or n % (i +2) == 0:
			return False
	return True		

def get_prime(upper_bound):
	'''
	Returns the first prime number encountered in a given sequence
	'''
	while True:

		if is_prime(upper_bound):
			prime = upper_bound
			return prime
		upper_bound -= 1

def sci_big_pow(upper_bound, number):
	'''
	A function to get the sci big pow of a number from a set or range of numbers 
	provided
	'''
	powers  = []
	for i in range(2, upper_bound):
		powers.append(int(math.log(number,i)))

	return powers

def factorial_product(numbers):
	'''
	A function that takes a list of numbers and computes
	the product of their factorials
	'''
	factorials = []
	for number in numbers:
		factorials.append(math.factorial(number))

	product = reduce(lambda x, y: x * y,factorials)

	return product

if __name__ == '__main__':

	prime_number = get_prime(2000000000)
	print('The prime number is {0}'.format(prime_number))
	list_of_powers = sci_big_pow(1000,prime_number)
	result = str(factorial_product(list_of_powers))
	result = result[-12:]
	print('The last 12 digits of the product of the factorials of the scibigpow of all numbers < 1000 that give a result  < largest prime below 2 billion is,{0}'.format(result))





