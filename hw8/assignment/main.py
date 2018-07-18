"""
Phillip Holland
COSC 5340
Summer 2018
Assignment 7 Ch. 8
"""


def createWordList():
	"""
	8.1 Write a createWordList function to create a list of words from the wordlist file.
	"""


def ex_8_3():
	"""
	8.3 Devise an experiment to measure performance of createWordList, createWordSet, and createWordDictionary. You can
		use the time module with the function time.time to get the current clock time, which may be accurate to several
		milliseconds. Getting the clock time before you start a task and after you complete a task allows you to estimate how
		long the task takes. This is very straightforward to call time.time() before calling one of the create functions and
		time.time() again afterward. the difference between these two gives the wall-clock time needed to build the
		list/set/dictionary. You could extend this experiment to show how one of the data structures makes the rest of the
		program run more quickly as well.
	"""


def ex_8_10():
	"""
	8.10 Evaluate the following statements:
	"""

	l1 = [4, 5, 3, 9, 1, 6, 7]
	l1 = l1.sort()  # l1 will be None, because sort() doesn't return anything.

	"""
	What is the value of l1 when you are done?
	"""
	return l1  # The return is None


def ex_8_11():
	"""
	8.11 Write a compare function that accepts two frequency dictionary tuples as parameters and compares the tuples
		using the second element.
	"""


def ex_8_15():
	"""
	8.15 Write a function that returns the most popular ending letter for words. Your program will take a list of
		words, count the ending letter of each word and return the letter whose count is the largest.
	"""


def ex_8_19():
	"""
	8.19 Write a regular expression pattern to match all words ending in "ing"
	"""


def ex_8_20():
	"""
	8.20 Write a regular expression pattern to match all words with ss anywhere in the string.
	"""


def ex_8_22():
	"""
	8.22 Write a regular expression pattern to match all the words that start with st.
	"""


def ex_8_23():
	"""
	8.23 Write a regular expression to match all the four-letter words where the middle two letters are vowels.
	"""


def ex_8_24():
	"""
	8.24 Write a function that can extract the host name from a URL. The host name is the part of the URL that
		comes after http:// but before the next /. Here is a simple one that matches hostnames that
		consist of letters and the dot character.
	"""


def main():
	pass


if __name__ == "__main__":
	main()
