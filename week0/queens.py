#Raymond Hettingers algorithm

from itertools import permutations
import unittest

def queens_problem(no_queens):

	'''A function to determine the number of different
	wasys k queens that can be placed in a k * k board such
	that they don't attack one another'''
	if no_queens not in [2,3]:
		ways = 0
		for permutation in permutations(range(no_queens),no_queens):
			#make sure no queens are on the same diagonal
			set_a = len(set(permutation[i] + i for i in range(no_queens)))
			set_b = len(set(permutation[i] - i for i in range(no_queens)))	
			if no_queens == set_a == set_b:
				ways += 1
		return ways	
	return 0		


#a small test for some known results

class TestQueensProblem(unittest.TestCase):
	def test_queens(self):
		self.assertEquals(queens_problem(2),0)
		self.assertEquals(queens_problem(9),352)
		self.assertEquals(queens_problem(8),92)
		self.assertEquals(queens_problem(7),40)
		#self.assertEquals(queens_problem(12),14200)



if __name__ == '__main__':
	unittest.main()