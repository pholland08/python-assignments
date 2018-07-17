"""
Phillip Holland
COSC 5340
Summer 2018
Assignment 6
"""


def ex_7_1():
	"""
	7.1 Write a function that prints the numbers from 0 to 50 counting by 5.
		This function must use a while loop.
	"""
	print(list(number_gen()))


def number_gen():
	number: int = 0
	while number < 51:
		yield number
		number = number + 5


def ex_7_2(text: str) -> int:
	"""
	7.2 Write a function that takes a string as a parameter and returns the number of spaces in the string.
		This function must use a while loop.
	"""
	return count_spaces(text)


def count_spaces(text: str) -> int:
	letters: list = list(text)
	count: int = 0
	current_index: int = 0

	while current_index < len(letters):
		if letters[current_index] == " ":
			count += 1
		current_index += 1

	return count


def ex_7_3():
	"""
	7.3 Write a function that asks the user to enter exam scores one at a time until the word stop is entered.
		When stop is entered, the program should compute the average of the scores.
	"""
	test_scores: list = []
	line: str = ""

	print("Please enter each exam on a new line.\nWhen finished, type stop.")

	while line.strip().lower() != "stop":
		line = input()
		if line and line.isnumeric():
			test_scores.append(float(line))

	print(sum(test_scores)/len(test_scores))


def ex_7_8():
	"""
	7.8 Add another condition to createClusters function to make sure that
		no more than maxRepeats number of iterations occur.
	"""


def ex_7_10():
	"""
	7.10 Load and run the code for the visualizeQuakes function.
		How do your results compare with those in the book?
	"""


def ex_7_11():
	"""
	7.11 Try to change the number of clusters. Be sure to add more colors if you add more clusters.
		I need to see a screen shot of the output.
	"""


def ex_7_12():
	"""
	7.12 Go to https://earthquake.usgs.gov/static/lfs/nshm/afghanistan/data/downloads/AFF_GR_WUS.out_rev1.pga.txt
		and run visualizeQuakes against the data.

		Make all the necessary changes in order to run visualizeQuakes or change the readData function to match.
		(A plus will be to those who will read the file directly from the web using urlib.request module we covered earlier in chapter 5)
		The solutions are extensions of the basic code that already supplied to you in the course materials for this week.
	"""


def ex_7_13():
	"""
	7.13 Using the earthquake data, try to cluster the quakes by their depth instead of latitude and longitude.
		Now visualize the data on the map using this new clustering. The solutions are extensions of the basic code
		that already supplied to you in the course materials for this week.
	"""


def ex_7_16():
	"""
	7.16 Implement an alternative to random centroid selection where the user has some say in the process.
	"""


def main():
	ex_7_3()


if __name__ == "__main__":
	main()
