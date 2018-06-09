
import unittest
from hw1.assignment import main


class TestMain(unittest.TestCase):
	def test_multiples_of_5(self):
		sequence = range(5, 50, 5)
		self.assertEqual(sequence, main.multiples_of_5())


if __name__ == "__main__":
	unittest.main()  # run all tests
