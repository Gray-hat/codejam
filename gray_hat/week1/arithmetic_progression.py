#A program to get the sum of te multiples of specified numbers
#in a given range


def arithmetic_progression(numbers,upper_bound):
	'''Given an list of numbers the function gets the sum of their 
	multiples in the range provided'''
	total = 0
	if isinstance(numbers,list):
		for number in numbers:
			number_terms = (upper_bound/number) if upper_bound > number else 0
			temp = (number_terms/2.0)* (2 * number + ((number_terms -1) * number))
			total += temp

		return total	
	return False

print "The sum is", arithmetic_progression([7,11],9999)