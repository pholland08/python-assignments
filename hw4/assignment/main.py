"""
Phillip Holland
COSC 5340
Summer 2018
Assignment 4
"""

import random
import math
import turtle

"""
4.1 Create a list with the following five items: 7, 9, 'a', 'cat', False.
"""
ex4_1: list = [7, 9, 'a', 'cat', False]


def ex4_2():
	"""
	4.2 Write Python statements to do the following:
		1. Append 3.14 and 7 to the list.
		2. Insert the value 'dog' at position 3.
		3. Find the index of 'cat'.
		4. Count the number of 7’s in the list.
		5. Remove the first 7 from the list.
		6. Remove 'dog' from the list using pop and index.
		7. Sort the remaining items on the list. Can you explain why they are ordered the way they are?
	"""

	# 4.2.1
	result: list = ex4_1
	result.append(3.14)
	print(result)
	result.append(7)
	print(result)

	# 4.2.2
	result.insert(3, "dog")
	print(result)

	# 4.2.3
	cat_index: int = result.index("cat")
	print(cat_index)

	# 4.2.4
	count_7: int = result.count(7)
	print(count_7)

	# 4.2.5
	del result[result.index(7)]
	print(result)

	# 4.2.6
	result.pop(result.index("dog"))
	print(result)

	# 4.2.7
	result = sorted(result, key=str)
	print(result)


def ex4_7_shuffle(input_list: list):
	"""
	4.7 Write a function shuffle that takes a list and returns a new list with the elements shuffled into a random order.
	"""
	# Note: There is the unlikely, yet distinct, possibility that a truly random function could return the
	# same list it was given. For the sake of unit testing, I have not allowed this possibility in this function.

	result: list = []
	location: int = -1

	while len(result) < len(input_list):
		location = random.randint(0, len(input_list)-1)

		if input_list[location] not in result:
			result.append(input_list[location])

	if (input_list == result) and (len(input_list) != 0):
		result = ex4_7_shuffle(input_list)

	return result


def ex4_24_makeDictionary():
	"""
	4.24 You have been given the following lists of students and their test scores:
		names=['joe','tom','barb','sue','sally']
		scores=[10,23,13,18,12]
		Write a function, makeDictionary, that takes the two lists and returns a dictionary with the names as the key
		and the scores as the values. Assign the result of makeDictionary to scoreDict, which will be used in the
		exercises that follow.
	"""
	names: dict = ['joe', 'tom', 'barb', 'sue', 'sally']
	scores: dict = [10, 23, 13, 18, 12]

	return dict(zip(names, scores))


scoreDict: dict = ex4_24_makeDictionary()


def ex4_25():
	"""
	4.25 Using scoreDict, find the score for 'barb'.
	"""
	return scoreDict.get("barb", -1)


def ex4_26():
	"""
	4.26 Add a score of 19 for 'john'.
	"""
	scoreDict.update({"john": 19})
	print("John is a slacker.")


def ex4_27():
	"""
	4.27 Create a sorted list of all the scores in scoreDict.
	"""
	return sorted(scoreDict.values())


def ex4_28():
	"""
	4.28 Calculate the average of all the scores in scoreDict.
	"""
	return sum(scoreDict.values()) / float(len(scoreDict.values()))


def ex4_29():
	"""
	4.29 Update the score for 'sally' to be 13.
	"""
	scoreDict.update({"sally": 13})
	print("Sally is a slacker just like John, but worse.")


def ex4_30():
	"""
	4.30 Tom has just dropped this class. Delete 'tom' and his score from
	"""
	if "Tom" in scoreDict.keys():
		del scoreDict["Tom"]


def ex4_31():
	"""
	4.31 Print out a table of students and their scores with the students listed
	"""
	for student, score in scoreDict.items():
		print("{0}:\t{1}".format(student, score))


def ex4_32_getScore(name: str, dictionary: dict):
	"""
	4.32 Write a function called getScore that takes a name and a dictionary as a parameter and returns
		the score for that name if it is in the dictionary. If the name is not in the dictionary,
		print an error message and return −1.
	"""
	try:
		return dictionary[name]
	except Exception as e:
		print(str(e))
		return -1


def ex4_35(data: list):
	"""
	4.35 Suppose you have a list of key-score values like the following:
		[('john',10), ('bob',8), ('john',5), ('bob',17),...]
		Write a function that takes such a list as a parameter and prints out a table of average scores for each person.
	"""
	scores: dict = {}

	for item in data:
		if item[0] not in scores:
			scores[item[0]] = []
		scores[item[0]].append(item[1])

	for name, grades in scores.items():
		avg: float = sum(grades) / float(len(grades))
		print("{0}:\t{1}".format(name, avg))


def ex4_42_frequencyChart(alist: list):
	"""
	4.42 Modify the frequency chart function to include a graphical representation of the mean.
	"""
	countdict = {}

	for item in alist:
		if item not in countdict:
			countdict[item] = 0

		countdict[item] = countdict[item] + 1

	itemlist = sorted(list(countdict.keys()))
	minitem = 0
	maxitem = len(itemlist) - 1

	countlist = countdict.values()
	maxcount = max(countlist)

	wn = turtle.Screen()
	chartT = turtle.Turtle()
	wn.setworldcoordinates(-1, -1, maxitem + 1, maxcount + 1)
	chartT.hideturtle()

	chartT.up()
	chartT.goto(0, 0)
	chartT.down()
	chartT.goto(maxitem, 0)
	chartT.up()

	chartT.goto(-1, 0)
	font_specs = ("Helvetica", 16, "bold")
	chartT.write("0", font=font_specs)
	chartT.goto(-1, maxcount)
	chartT.write(str(maxcount), font=font_specs)

	for index in range(len(itemlist)):
		chartT.goto(index, -1)
		chartT.write(str(itemlist[index]), font=font_specs)

		chartT.goto(index, 0)
		chartT.down()
		chartT.goto(index, countdict[itemlist[index]])
		chartT.up()

	# Added graphical representation of mean
	average_occurence = round(sum(countlist)/float(len(countlist)), 2)
	chartT.up()
	chartT.goto(-1, average_occurence)
	chartT.down()
	chartT.write("Avg: {0}".format(average_occurence), font=font_specs)
	chartT.goto(max(itemlist)-1, average_occurence)

	wn.exitonclick()


def main():
	# ex4_35([('john',10), ('bob',8), ('john',5), ('bob',17)])
	ex4_42_frequencyChart([3,3,5,7,1,2,5,2,3,4,6,3,4,6,3,4,5,6,6])


if __name__ == '__main__':
	import time
	main()
