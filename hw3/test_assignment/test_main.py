
import unittest
from hw3.assignment import main as other


class TestMain(unittest.TestCase):
	def test_e3_23_remove_char(self):
		input_string: str = "hello"

		return_string: str = other.e3_23_remove_char(input_string, 1)

		self.assertEqual(return_string, "hllo")

	def test_e3_26_rot13_returnsString(self):
		self.assertTrue(type(rotate_hello()) is str)

	def test_e3_26_rot13_OutputIsNotInput(self):
		message: str = "hello"
		result: str = other.e3_26_rot13(message)

		self.assertNotEqual(message, result)

	def test_e3_26_rot13_allowsEmptyString(self):
		message: str = ""
		result: str = other.e3_26_rot13(message)

		self.assertEqual(result, message)

	def test_e3_26_rot13_RotatesFirstLetter(self):
		self.assertEqual(rotate_hello()[0], "u")

	def test_e3_26_rot13_RotatesHello(self):
		h = "u"
		e = "r"
		l = "y"
		o = "b"
		hello: str = "".join([h, e, l, l, o])

		self.assertEqual(rotate_hello(), hello)

	def test_e3_26_rot13_RotatesLowercaseAlphabet(self):
		alphabet: str = "abcdefghijklmnopqrstuvwxyz"
		rotated_alphabet: str = "nopqrstuvwxyzabcdefghijklm"

		self.assertEqual(other.e3_26_rot13(alphabet), rotated_alphabet)

	def test_e3_26_rot13_RotatesUppercaseAlphabet(self):
		alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		rotated_alphabet: str = "NOPQRSTUVWXYZABCDEFGHIJKLM"

		self.assertEqual(other.e3_26_rot13(alphabet), rotated_alphabet)

	def test_e3_26_rot13_RotatesMixedCaseAlphabet(self):
		alphabet: str = "AbCdEfGhIjKlMnOpQrStUvWxYz"
		rotated_alphabet: str = "NoPqRsTuVwXyZaBcDeFgHiJkLm"

		self.assertEqual(other.e3_26_rot13(alphabet), rotated_alphabet)

	def test_e3_26_rot13_OnlyRotatesLetters(self):
		message: str = "h e l l o!@#$%^&*()_+-={}|[]\\;':\",./<>?`~"
		rotated_message: str = "u r y y b!@#$%^&*()_+-={}|[]\\;':\",./<>?`~"

		self.assertEqual(other.e3_26_rot13(message), rotated_message)

	def test_e3_27_driver_HandlesEmptyStrings(self):
		self.assertEqual(other.e3_27_encrypt("", 0), "")

	def test_e3_27_driver_ShiftsDifferentAmounts(self):
		output_0: str = other.e3_27_encrypt("hello", 0)
		output_1: str = other.e3_27_encrypt("hello", 1)

		self.assertNotEqual(output_0, output_1)

	def test_e3_27_driver_WrapsAround(self):
		output: str = other.e3_27_encrypt("z", 1)

		self.assertEqual("a", output)

	def test_e3_27_driver_HandlesUppercase(self):
		output: str = other.e3_27_encrypt("A", 1)

		self.assertEqual("B", output)

	def test_e3_27_driver_IgnoresPunctuation(self):
		message: str = "H e l l o!@#$%^&*()_+-={}|[]\\;':\",./<>?`~"
		shifted_message: str = "I f m m p!@#$%^&*()_+-={}|[]\\;':\",./<>?`~"

		self.assertEqual(other.e3_27_encrypt(message, 1), shifted_message)

	def test_e3_27_encrypt(self):
		self.assertEqual("Ifmmp", other.e3_27_encrypt("Hello", 1))

	def test_e3_27_decrypt(self):
		self.assertEqual("Hello", other.e3_27_decrypt("Ifmmp", 1))

	def test_e3_29_decryptVigenere_WithoutSpaces(self):
		self.assertEqual("theeaglehaslanded", other.e3_29_decryptVigenere("whzmnithhvaycvgey", "davinci"))

	def test_e3_29_decryptVigenere_WithSpaces(self):
		self.assertEqual("the eagle has landed", other.e3_29_decryptVigenere("whz mnith hva ycvgey", "davinci"))


def rotate_hello():
	return other.e3_26_rot13("hello")


if __name__ == "__main__":
	unittest.main()  # run all tests
