import math

def sieve_of_eratosthenes(upperlimit, lowerbound = 0):
	'''A program to calculate prime 
		numbers of a given range
	'''
	store = []
	number_set = [True] * (upperlimit+1)
	number_set[0] = number_set[1] = False
	
	loop_ubound = int(math.ceil(math.sqrt(upperlimit))) #sqrt(n) max time loop requires to run

	for i in range(2,loop_ubound + 1):
		if number_set[i] == True:
			for j in range(i*i,upperlimit+1, i):
				number_set[j] = False
	#get the numbers
	for (index, isprime) in enumerate(number_set):
		if isprime and index > lowerbound: 
			store.append(index)			
	 
	return store

def divisible_prime(prime_numbers, upperbound):
	'''A function that gets all the numbers in a certain
	range that are divisible by all the prime numbers provided to it.'''

	total = 0
	temp = set ()
	largest_prime = max(prime_numbers) #just for efficiency. No number below this can be considered
	all_numbers = set(list(range(largest_prime,upperbound + 1,2)))
	for i in range(largest_prime, upperbound + 1,2):
		for number in prime_numbers:
			if (i % number) != 0:
				temp.add(i)
				break #dont check any more numbers since one has already failed

	divisible_numbers = all_numbers.difference(temp)	
	#print(divisible_numbers)
	return divisible_numbers	



#step1 get all primes 
primes = sieve_of_eratosthenes(9,2)

#step2 perform test
total = sum(divisible_prime(primes, 100000)) 

print("The sum is {0}".format(total))


