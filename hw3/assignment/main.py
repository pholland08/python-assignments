"""
Phillip Holland
COSC 5340
Summer 2018
Assignment 3
"""

import string


letters: {str: int} = {
	"a": 0,
	"b": 1,
	"c": 2,
	"d": 3,
	"e": 4,
	"f": 5,
	"g": 6,
	"h": 7,
	"i": 8,
	"j": 9,
	"k": 10,
	"l": 11,
	"m": 12,
	"n": 13,
	"o": 14,
	"p": 15,
	"q": 16,
	"r": 17,
	"s": 18,
	"t": 19,
	"u": 20,
	"v": 21,
	"w": 22,
	"x": 23,
	"y": 24,
	"z": 25}


"""
3.1 Create a string variable that is initialized to your entire name–first, middle, and last.
"""
fullname: str = "PhillipJamesHolland"


def e3_2():
	"""
	3.2 Using the slice operator, print your first name.
	"""
	print(fullname[:7])


def e3_3():
	"""
	3.3 Using the slice operator, print your last name.
	"""
	print(fullname[12:])


def e3_4():
	"""
	3.4 Using the slice and concatenation operators, print your name in the form “Lastname, Firstname.”
	"""
	print(fullname[12:] + ", " + fullname[:7])


def e3_5():
	"""
	3.5 Print the length of your first name.
	"""
	print(len("Phillip"))


def e3_6():
	"""
	3.6 Assume you have two variables: s='s', and p='p'.
		Using concatenation and repetition, write an expression that
		produces the string mississippi.
	"""
	s: str = 's'
	p: str = 'p'
	print("mi" + s*2 + "i" + s*2 + "i" + p*2 + "i")


def e3_7():
	"""
	3.7 Modify the prefix example in Session 3.5 to print all prefixes of “Roy G Biv”, including the entire string.
	"""
	roy_fullname: str = "Roy G Biv"
	for i in range(len(roy_fullname)+1):
		print(roy_fullname[:i])


def e3_8():
	"""
	3.8 Using the count method, find the number of occurrences of the character ‘s’ in the string 'mississippi'.
	"""
	print("mississippi".count("s"))


def e3_9():
	"""
	3.9 Replace all occurrences of the substring 'iss' with 'ox'.
	"""
	print("mississippi".replace("iss", "ox"))


def e3_10():
	"""
	3.10 Find the index of the first occurrence of 'p' in 'mississippi'.
	"""
	print("mississippi".find("p"))


def e3_11():
	"""
	3.11 Make the word 'python' centered and all capital letters in a string of length 20.
	"""
	print("python".center(20))


def e3_12():
	"""
	3.12 What is the difference between ord('A') and ord('a')?
	"""
	print(ord('A') - ord('a'))


def e3_13(digit: chr):
	"""
	3.13 Write a function that takes a single character digit and returns its integer value.
	"""
	return ord(digit)


def e3_16(exam_score: float):
	"""
	3.16 Write a function that takes an exam score from 0–100 and returns the corresponding letter grade.
		Use the same grading scale your professor does for this class.
	"""

	exam_score: int = int(round(exam_score, 2))

	grade_a: int() = range(90, 101)
	grade_b: int() = range(80, 90)
	grade_c: int() = range(70, 80)
	grade_d: int() = range(60, 70)

	letter_grade: str = ""

	if exam_score in grade_a:
		letter_grade = "A"
	elif exam_score in grade_b:
		letter_grade = "B"
	elif exam_score in grade_c:
		letter_grade = "C"
	elif exam_score in grade_d:
		letter_grade = "D"
	else:
		letter_grade = "F"

	return letter_grade


def e3_19(plain_text: str, number_rails: int) -> [str]:
	"""
	3.19 The transposition cipher can be generalized to any number of rails.
		Write a function to implement a three-rail fence cipher that takes every
		third character and puts it on one of the three rails.
	"""

	current_rail: int = 0
	cipher_rails: [str] = [""] * number_rails

	for index, letter in enumerate(plain_text):
		current_rail = index % number_rails
		cipher_rails[current_rail] = cipher_rails[current_rail] + letter

	return cipher_rails


def e3_23_remove_char(string: str, idx: int) -> str:
	"""
	3.23 Write the removeChar function using for loops rather than slice operators.
	"""

	return_string: str = ""

	for index, letter in enumerate(string):
		if index is not idx:
			return_string = return_string + letter

	return return_string


def e3_26_rot13(plain_text: str) -> str:
	"""
	3.26 Encryption often involves the Caesar cipher, named after Julius Caesar, who used the system to encrypt
		military messages. Many early Internet users also adopted this cipher. Called rot13, the cipher encrypts
		a message by rotating the plaintext character by 13 positions in the alphabet. For example, “a” becomes “n”
		and likewise “n” becomes “a”. The nice thing about rot13 is that the same function can be used to encrypt
		and decrypt a message. Write a function called rot13 that takes a message as a parameter and rotates all
		the characters by 13 places.
	"""
	char_list = list(plain_text)
	lower_range: int() = range(ord("a"), ord("z")+1)
	upper_range: int() = range(ord("A"), ord("Z")+1)

	for index, letter in enumerate(char_list):
		new_ordinal = ord(letter)

		if ord(letter) in lower_range:
			new_ordinal = ord(letter) + 13
			if new_ordinal not in lower_range:
				new_ordinal = new_ordinal - 26
		elif ord(letter) in upper_range:
			new_ordinal = ord(letter) + 13
			if new_ordinal not in upper_range:
				new_ordinal = new_ordinal - 26
		new_letter = chr(new_ordinal)
		char_list[index] = new_letter

	return "".join(char_list)


def e3_27_encrypt(plain_text: str, shift_amount: int) -> str:
	return e3_27_driver(plain_text, shift_amount)


def e3_27_decrypt(cipher_text: str, shift_amount: int) -> str:
	return e3_27_driver(cipher_text, -shift_amount)


def e3_27_driver(plain_text: str, shift_amount: int) -> str:
	"""
	3.27 Rewrite the Caesar cipher so that it takes the number of places to rotate as a parameter. You will have
		to write separate encrypt and decrypt functions.
	"""
	plain_text = list(plain_text)
	shifted_text: str() = list("")

	for letter in plain_text:
		if letter in list(string.ascii_letters):
			is_upper = letter in list(string.ascii_uppercase)

			li = (letters[letter.lower()] + shift_amount) % 26
			letter = chr(97+li)
			letter = letter.upper() if is_upper else letter

		shifted_text.append(letter)

	return "".join(shifted_text)


def e3_29_decryptVigenere(cipher_text: str, keyword: str) -> str:
	"""
	BONUS Question
	3.29 Write a function decryptVignere that takes a keyword, the cipher text for the message,
		and returns the plaintext message.
	"""
	# This function currently accepts ONLY alphabetical characters and spaces.

	plain_text: str() = list("")
	words: str() = cipher_text.split(" ")
	offset: int = 0

	for w_index, word in enumerate(words):
		plain_word: str() = list("")

		for l_index, letter in enumerate(list(word)):
			key_index = (l_index + offset) % len(keyword)
			key_ord = letters[keyword[key_index]]
			plain_word.append(e3_27_decrypt(letter, key_ord))
		plain_text.append("".join(plain_word))
		offset = offset + len(word)
	return " ".join(plain_text)


def main():
	# print(e3_19("It_was_a_dark_and_stormy_night", 2))
	print(e3_27_encrypt("hello", 1))


if __name__ == '__main__':
	main()
