
import unittest
from hw4.assignment import main as other


class TestMain(unittest.TestCase):
	def test_ex4_7_shuffle_acceptsEmptyList(self):
		thing: list = list()
		self.assertEqual(other.ex4_7_shuffle(thing), [])

	def test_ex4_7_shuffle_preservesElements(self):
		thing: list = ["a1", "b2", "c3", "d4"]
		result: list = other.ex4_7_shuffle(thing)
		self.assertTrue(sorted(thing) == sorted(result))

	def test_ex4_7_shuffle_changesOrder(self):
		thing: list = ["a1", "b2", "c3", "d4"]
		result: list = other.ex4_7_shuffle(thing)
		self.assertNotEqual(thing, result)


if __name__ == "__main__":
	unittest.main()  # run all tests
