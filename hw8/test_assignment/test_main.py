
import unittest
import hw8.assignment.main as other


class TestMain(unittest.TestCase):
	def test_createWordList_return_list(self):
		response: list = other.createWordList()
		self.assertTrue(type(response) is list)

	def test_ex_8_15_returns_str(self):
		words = ["first", "second", "third", "fourth", "fifth"]
		expected = type('h')
		response = other.ex_8_15(words)

		self.assertEqual(expected, type(response))

	def test_ex_8_15_returns_one_letter(self):
		words = ["first", "second", "third", "fourth", "fifth"]
		expected = 1
		response = other.ex_8_15(words)

		self.assertEqual(expected, len(response))

	def test_ex_8_15_returns_ending_letter(self):
		words = ["first", "second", "third", "fourth", "fifth"]
		expected = ['t', 'd', 'h']
		response = other.ex_8_15(words)

		self.assertTrue(response in expected)

	def test_ex_8_15_returns_most_common_ending_letter(self):
		words = ["first", "second", "third", "fourth"]
		expected = 'd'
		response = other.ex_8_15(words)

		self.assertEqual(expected, response)

	def test_ex_8_19_returns_list(self):
		text = ""
		expected = list(text)
		response = other.ex_8_19(text)

		self.assertEqual(type(expected), type(response))

	def test_ex_8_19_matches_ing(self):
		text: str = "ing"
		expected = [text, ]
		response = other.ex_8_19(text)

		self.assertEqual(expected, response)

	def test_ex_8_19_matches_multiple_ing(self):
		text: str = "ing ing"
		expected = ["ing", "ing"]
		response = other.ex_8_19(text)

		self.assertEqual(expected, response)

	def test_ex_8_19_matches_something(self):
		text: str = "something"
		expected = [text, ]
		response = other.ex_8_19(text)

		self.assertEqual(expected, response)

	def test_ex_8_19_doesnt_match_other_stuff(self):
		text: str = "other stuff"
		expected = []
		response = other.ex_8_19(text)

		self.assertEqual(expected, response)

	def test_ex_8_19_doesnt_match_other_stuff(self):
		text: str = "other stuff"
		expected = []
		response = other.ex_8_19(text)

		self.assertEqual(expected, response)

	def test_ex_8_19_matches_other_stuffing(self):
		text: str = "other-stuffing"
		expected = [text, ]
		response = other.ex_8_19(text)

		self.assertEqual(expected, response)

	def test_ex_8_19_thanksgiving(self):
		text: str = "For Thanksgiving dinner, we had turkey, gravy, stuffing, and special-something pie."
		expected = ["Thanksgiving", "stuffing", "special-something"]
		response = other.ex_8_19(text)

		self.assertEqual(expected, response)

	def test_ex_8_20_returns_emptylist_for_blank(self):
		text: str = ""
		response: list = other.ex_8_20(text)

		self.assertTrue(type(response) is list)

	def test_ex_8_20_matches_single_ss(self):
		text: str = "ss"
		response: list = other.ex_8_20(text)

		self.assertTrue([text, ] == response)

	def test_ex_8_20_matches_missing_only(self):
		text: str = "not missing"
		expected: list = ["missing", ]
		response: list = other.ex_8_20(text)

		self.assertEqual(expected, response)

	def test_ex_8_20_matches_pass_hissing_only(self):
		text: str = "As you pass, the cat will be hissing."
		expected: list = ["pass", "hissing"]
		response: list = other.ex_8_20(text)

		self.assertEqual(expected, response)

	def test_ex_8_22_matches(self):
		text: str = "Stop after the first one."
		expected: list = ["Stop", ]
		response: list = other.ex_8_22(text)

		self.assertEqual(expected, response)

	def test_ex_8_23_matches(self):
		text: str = "All your bases are belong to me."
		expected: list = ["your", ]
		response: list = other.ex_8_23(text)

		self.assertEqual(expected, response)

	def test_ex_8_24_matches(self):
		text: str = "http://www.thedevneedscoffee.com?asdf"
		expected: str = "www.thedevneedscoffee.com"
		response: list = other.ex_8_24(text)

		self.assertEqual(expected, response)


if __name__ == "__main__":
	unittest.main()
