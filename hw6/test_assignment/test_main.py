
import unittest
import hw6.assignment.main as assignment


class TestMain(unittest.TestCase):
	def test_number_gen_yeilds_correct_numbers(self):
		num_list: list = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
		self.assertEqual(num_list, list(assignment.number_gen()))

	def test_count_spaces_handles_empty_string(self):
		self.assertTrue(assignment.count_spaces("") >= 0)

	def test_count_spaces_returns_int(self):
		self.assertEqual(int, type(assignment.count_spaces("")))

	def test_count_spaces_returns_1_for_blank(self):
		expected: int = 1
		response: int = assignment.count_spaces(" ")
		self.assertEqual(expected, response)

	def test_count_spaces_returns_0_for_hello(self):
		expected: int = 0
		response: int = assignment.count_spaces("hello")
		self.assertEqual(expected, response)

	def test_count_spaces_returns_0_for_tab(self):
		expected: int = 0
		response: int = assignment.count_spaces("	")
		self.assertEqual(expected, response)

	def test_count_spaces(self):
		expected: int = 7
		response: int = assignment.count_spaces("this is a string with spaces and tabs		")
		self.assertEqual(expected, response)


if __name__ == "__main__":
	unittest.main()
