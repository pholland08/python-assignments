import math

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


def e3_12(digit: chr):
	"""
	3.13 Write a function that takes a single character digit and returns its integer value.
	"""
	return ord(digit)


def e3_16(exam_score: float):
	"""
	3.16 Write a function that takes an exam score from 0–100 and returns the corresponding letter grade.
		Use the same grading scale your professor does for this class.
	"""

	exam_score: int = int(math.round(exam_score))

	grade_a: range(int) = range(90, 101)
	grade_b: range(int) = range(80, 90)
	grade_c: range(int) = range(70, 80)
	grade_d: range(int) = range(60, 70)

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


def e3_23():
	"""
	3.23 Write the removeChar function using for loops rather than slice operators.
	"""
	# page 104


"""
3.26 Encryption often involves the Caesar cipher—named after Julius Caesar, who used the system to encrypt
	military messages. Many early Internet users also adopted this cipher. Called rot13, the cipher encrypts
	a message by rotating the plaintext character by 13 positions in the alphabet. For example, “a” becomes “n”
	and likewise “n” becomes “a”. The nice thing about rot13 is that the same function can be used to encrypt
	and decrypt a message. Write a function called rot13 that takes a message as a parameter and rotates all
	the characters by 13 places.
"""


"""
3.27 Rewrite the Caesar cipher so that it takes the number of places to rotate as a parameter. You will have to write separate encrypt and decrypt functions.
"""

"""
BONUS Question
3.29 Write a function decryptVignere that takes a keyword, the ciphter- text for the message, and returns the plaintext message.
"""


def main():
	print(e3_19("It_was_a_dark_and_stormy_night", 2))


if __name__ == '__main__':
	main()
