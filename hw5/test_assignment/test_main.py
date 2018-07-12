
import unittest
from hw5.assignment import main as other
import decimal


class TestMain(unittest.TestCase):
	def test_format_line_returns_str(self):
		line: str = "Akron 25.81"
		self.assertEqual(type(other.format_line(line)), str)

	def test_format_line_processes_empty_string(self):
		line: str = ""
		self.assertEqual(other.format_line(line), " "*30)

	def test_format_line_positions_correctly(self):
		line: str = "Akron 25.8"
		response: str = other.format_line(line)
		expected: str = "                    Akron 25.8 "
		self.assertEqual(expected, response)

	def test_format_line_formats_decimal_properly(self):
		line: str = "Akron 25.81"
		response: str = other.format_line(line)
		expected: str = "                    Akron 25.8 "
		self.assertEqual(expected, response)

	def test_format_temp_returns_str(self):
		temp: float = 98.6
		self.assertEqual(str, type(other.format_temp(temp)))

	def test_format_temp_gives_correct_decimals_to_ints(self):
		temp: int = 74
		response: str = other.format_temp(temp)
		expected: str = "74.000"
		self.assertEqual(expected, response)

	def test_convert_to_celsius_returns_Decimal(self):
		temp: float = 98.6
		self.assertEqual(decimal.Decimal, type(other.convert_to_celsius(temp)))

	def test_convert_to_celsius_handles_ints(self):
		temp: int = 98
		response: decimal.Decimal = other.convert_to_celsius(temp)
		self.assertEqual(decimal.Decimal, type(response))

	def test_convert_to_celsius_returns_0_for_32(self):
		temp: int = 32
		response: int = int(other.convert_to_celsius(temp))
		expected: int = 0
		self.assertEqual(expected, response)

	def test_convert_to_celsius_returns_100_for_212(self):
		temp: int = 212
		response: int = int(other.convert_to_celsius(temp))
		expected: int = 100
		self.assertEqual(expected, response)

	def test_format_temp_line_returns_correct_length(self):
		temp1: str = "1.000"
		temp2: str = "1.000"
		response: str = other.format_temp_line(temp1, temp2)
		self.assertTrue(len(response) == 21)

	def test_format_temp_line_returns_expected(self):
		temp1: str = "1.000"
		temp2: str = "1.000"
		response: str = other.format_temp_line(temp1, temp2)
		expected: str = "     1.000      1.000"
		self.assertEqual(expected, response)


if __name__ == "__main__":
	unittest.main()  # run all tests
