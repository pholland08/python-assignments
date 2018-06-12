
import unittest
from hw2.assignment import main as other


class TestMain(unittest.TestCase):
	def test_calculate_paycheck(self):
		pay_rate: float = 10
		hours_worked: float = 0

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


if __name__ == "__main__":
	unittest.main()  # run all tests
