
import unittest
from hw1.assignment import main


class TestMain(unittest.TestCase):
	def test_multiples_of_5_returns_list(self):
		self.assertEqual(list, type(main.multiples_of_5()))

	def test_multiples_of_5_return_includes_upper_limit(self):
		response: list = main.multiples_of_5()
		exists: bool = any(i == 50 for i in response)
		self.assertTrue(exists)

	def test_multiples_of_5_output(self):
		expected = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
		response: list = main.multiples_of_5()
		self.assertEqual(expected, response)


if __name__ == "__main__":
	unittest.main()  # run all tests
