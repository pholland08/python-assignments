
import unittest
import turtle
from hw2.assignment import main as other


class TestMain(unittest.TestCase):
	"""
	calculate_paycheck tests
	"""
	def test_calculate_paycheck(self):
		pay_rate = 10
		hours_worked = 0

		# Assert 0 (0 + 0)
		self.assertEqual(float(0), other.calculate_paycheck(pay_rate, hours_worked))

		# Assert 1 (10 + 0)
		hours_worked = 1
		self.assertEqual(float(10), other.calculate_paycheck(pay_rate, hours_worked))

		# Assert 10 (100 + 0)
		hours_worked = 10
		self.assertEqual(float(100), other.calculate_paycheck(pay_rate, hours_worked))

		# Assert 100 (400 + 900)
		hours_worked = 100
		self.assertEqual(float(1300), other.calculate_paycheck(pay_rate, hours_worked))

	"""
	inCircle tests
	"""
	def test_inCircle_NonNegativeRadius(self):
		self.assertFalse(other.inCircle((-1, -4), -5))

	def test_inCircle_CoordsNotGreaterThanRadius(self):
		self.assertFalse(other.inCircle((0, 0), -1))

	def test_inCircle_HypotenuseNotGreaterThanRadius(self):
		self.assertFalse(other.inCircle((4, 4), 5))

	def test_inCircle_PointOnRadius345(self):
		self.assertTrue(other.inCircle((3, 4), 5))

	def test_inCircle_PointInsideRadius125(self):
		self.assertTrue(other.inCircle((1, 2), 5))

	def test_inCircle_NegativePointOnRadius(self):
		self.assertTrue(other.inCircle((-3, -4), 5))


if __name__ == "__main__":
	unittest.main()  # run all tests
