"""
Phillip Holland
COSC 5340
Summer 2018
Assignment 7 Ch. 8
"""

import re
import time


def createWordList() -> list:
	"""
	8.1 Write a createWordList function to create a list of words from the wordlist file.
	"""
	with open("../resources/wordlist.txt", "r") as word_file:
		return word_file.readlines()


def createWordSet() -> set:
	return set(createWordList())


def createWordDict() -> dict:
	d = {}
	with open("../resources/wordlist.txt", "r") as word_file:
		for line in word_file.readlines():
			d[line] = None

	return d


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

	# On my computer, the execution results are as follows:
	#
	# createWordList:  0.008999109268188477
	# createWordSet:  0.010995626449584961
	# createWordDict:  0.010996580123901367
	#
	# While createWordList has slightly faster performance in creation, any benefit is lost as soon as a single
	# value lookup is performed. Not much difference is seen between createWordSet and createWordDict.

	start = time.time()
	createWordList()
	finish = time.time()
	print("createWordList: ", (finish - start))

	start = time.time()
	createWordSet()
	finish = time.time()
	print("createWordSet: ", (finish - start))

	start = time.time()
	createWordDict()
	finish = time.time()
	print("createWordDict: ", (finish - start))


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


def ex_8_11(t1: tuple, t2: tuple) -> bool:
	"""
	8.11 Write a compare function that accepts two frequency dictionary tuples as parameters and compares the tuples
		using the second element.
	"""
	# Not sure what is being asked on this question.
	return t1[1] > t2[1]


def ex_8_15(words: list) -> str:
	"""
	8.15 Write a function that returns the most popular ending letter for words. Your program will take a list of
		words, count the ending letter of each word and return the letter whose count is the largest.
	"""
	endings: dict = {}

	for word in words:
		ending = word[-1]

		if endings.get(ending) is None:
			endings[ending] = 0

		endings[ending] = endings[ending] + 1

	items = list(endings.items())
	items.sort(key=lambda x: x[1], reverse=True)

	return items[0][0]


def ex_8_19(text: str) -> list:
	"""
	8.19 Write a regular expression pattern to match all words ending in "ing"
	"""

	return match_in_text(text, r"((\w|-)*ing)\b")


def match_in_text(text: str, regex: str) -> list:
	matches: list = []

	if text:
		words: list = text.split()

		matches = match_from_list(words, regex)

	return matches


def match_from_list(words: list, regex: str) -> list:
	matches: list = []

	for word in words:
		m = re.match(regex, word, re.IGNORECASE)
		if m:
			matches.append(m.group(1))

	return matches


def ex_8_20(text: str) -> list:
	"""
	8.20 Write a regular expression pattern to match all words with ss anywhere in the string.
	"""
	return match_in_text(text, r"(\w*ss\w*)\b")


def ex_8_22(text: str) -> list:
	"""
	8.22 Write a regular expression pattern to match all the words that start with st.
	"""
	return match_in_text(text, r"\b(st\w*)\b")


def ex_8_23(text: str) -> list:
	"""
	8.23 Write a regular expression to match all the four-letter words where the middle two letters are vowels.
	"""
	return match_in_text(text, r"\b([A-z][AEIOUaeiou]{2}[A-z])\b")


def ex_8_24(url: str) -> str:
	"""
	8.24 Write a function that can extract the host name from a URL. The host name is the part of the URL that
		comes after http:// but before the next /. Here is a simple one that matches hostnames that
		consist of letters and the dot character.
	"""
	return match_in_text(url, r"\bhttps?://((\w|\.)+)\b")[0]


def main():
	ex_8_3()


if __name__ == "__main__":
	main()
