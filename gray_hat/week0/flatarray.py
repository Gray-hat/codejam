#a python program to solve the flat array problem

import unittest

def get_elements_array(nested_array):
	total_elements = len(nested_array)
	number_of_arrays = 1
	#loop thru the array
	for element in nested_array:
		if isinstance(element, list): #check if element is a list
			total_elements += len(element)
			number_of_arrays += 1
	return (number_of_arrays, total_elements)	


#tests to confirm program works correctly

class TestFlatArray(unittest.TestCase):

	def setUp(self):
		self.test1 = get_elements_array([1,2,3,4,5,6,7])
		self.test2 = get_elements_array([1,[45,75],4,6])
		self.test3 = get_elements_array([1,[45,75],4,6,[4,4]])

	def test_results(self):
		self.assertEquals(self.test1, (1,7))
		self.assertEquals(self.test2,(2,6))	
		self.assertEquals(self.test3,(3,9))

if __name__ == '__main__':
	unittest.main()
