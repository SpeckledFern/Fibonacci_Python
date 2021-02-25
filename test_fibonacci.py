import unittest
import fibonacci


class TestCalculator(unittest.TestCase):
	def test_sequence(self):
   		# Returns the correct fibonacci number given the index of the output starting at 0
		self.assertEqual(fibonacci.get_num_at(5), 5)
	
		self.assertEqual(fibonacci.get_num_at(8), 21)

		self.assertEqual(fibonacci.get_num_at(0), 0)

	def test_add(self):
		self.assertEqual(fibonacci.factorial(4), 24)
		self.assertEqual(fibonacci.factorial(5), 120)
		self.assertEqual(fibonacci.factorial(2), 2)


if __name__ == "__main__":
	unittest.main()
