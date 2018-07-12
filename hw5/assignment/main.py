"""
Phillip Holland
COSC 5340
Summer 2018
Assignment 5
"""

import decimal
import requests
from html.parser import HTMLParser
import statistics
import random


def ex_5_1():
	"""
	5.1 Write a program to read the rainfall.txt file and then write out a new file called rainfallfmt.txt The new
	file should format each line so that the city is right-justified in a field that is 25 characters wide, and the
	rainfall data should be printed in a field that is 5 characters wide with 1 digit to the right of the decimal point.
	"""
	with open("../rainfall.txt", "r") as rainfall_file, open("../rainfall_fmt.txt", "w+") as formatted_file:
		for line in rainfall_file.readlines():
			formatted_line = format_line(line)
			formatted_file.write(formatted_line + "\n")


def format_line(line: str) -> str:
	formatted: str = " "*30

	if line:  # is not null or empty
		line = line.split(" ")
		line[0] = line[0].rjust(25, " ")
		line[1] = round(float(line[1]), 1)
		line[1] = str(line[1]).ljust(5, " ")
		formatted = " ".join(line)

	return formatted


def ex_5_2():
	"""
	5.2 Write a function that writes a temperature conversion table called tempconv.txt. The table should include
	temperatures from −300 to 212 degrees Fahrenheit and their Celsius equivalents, presented in two columns with
	appropriate headings. Each column should be 10 characters wide, and each temperature should have 3 digits to the
	right of the decimal point.
	"""

	with open("../temp_conv.txt", "w+") as output_file:
		formatted_line = format_temp_line("Fahrenheit", "Celsius")
		output_file.write(formatted_line + "\n")

		for temp in range(-300, 212+1):
			c_temp = convert_to_celsius(temp)

			f_temp = format_temp(temp)
			c_temp = format_temp(c_temp)

			formatted_line = format_temp_line(f_temp, c_temp)
			output_file.write(formatted_line + "\n")


def format_temp(temp: float) -> str:
	decimal_temp = decimal.Decimal(str(temp))
	rounded_temp: float = round(decimal_temp, 3)
	return str(rounded_temp)


def convert_to_celsius(temp: float) -> decimal.Decimal:
	f_temp: decimal.Decimal = decimal.Decimal(temp) - decimal.Decimal(32)
	c_temp: decimal.Decimal = f_temp * (decimal.Decimal(5) / decimal.Decimal(9))
	return c_temp


def format_temp_line(temp1: str, temp2: str) -> str:
	temp1 = temp1.rjust(10)
	temp2 = temp2.rjust(10)
	return " ".join([temp1, temp2])


def ex_5_3():
	"""
	5.3 Open a file during a Python session. Call the readline method twice on that file, then call the readlines
	method. What lines does the list returned by readlines include?
	"""
	# readlines() will return all lines that occur after the first 2 calls to readline()
	with open("../temp_conv.txt", "r") as input_file:
		scrap = input_file.readline()
		scrap = input_file.readline()
		content = input_file.readlines()
		for line in content:
			print(line)


def ex_5_5():
	"""
	5.5 Write a program that reads in the contents of a file and writes a new file where all the characters are in
	uppercase.
	"""
	with open("../rainfall.txt", "r") as input_file, open("../rainfall_upper.txt", "w+") as output_file:
		content: str = input_file.read()
		output_file.write(content.upper())


def ex_5_8():
	"""
	5.8 Frequency tables are often created by placing data items in a range. Implement a function that will group the
	earthquake data by the following criteria:
	Micro (0–3), Minor (3–3.9), Light (4–4.9), Moderate (5–5.9), Major (6–6.9), Strong (7–7.9), and Great (>=8)
	"""
	severities: dict = {"micro": [], "minor": [], "light": [], "moderate": [], "major": [], "strong": [], "great": []}

	with open("../earthquakes.txt", "r") as input_file:
		lines = input_file.readlines()

	[categorize_by_severity(x, severities) for x in lines]

	print("{0}\t{1}".format("Category".rjust(9), "Count (out of {0})".format(len(lines))))
	for key, value in severities.items():
		print("{0}\t{1}".format(key.rjust(9), len(value)))


def categorize_by_severity(string: str, severity_dict: dict):
	split_string = string.split("\t")
	list_name = ""
	severity = float(split_string[0])

	if severity >= 8:
		list_name = "great"
	elif severity >= 7:
		list_name = "string"
	elif severity >= 6:
		list_name = "major"
	elif severity >= 5:
		list_name = "moderate"
	elif severity >= 4:
		list_name = "light"
	elif severity >= 3:
		list_name = "minor"
	else:
		list_name = "micro"

	severity_dict[list_name].append(string)


def ex_5_10():
	"""
	5.10 Write a function to process the earthquake data file and create lists of earthquake magnitudes, one for each
	date. Your function should return a list of lists that looks something like this:
	[[date1, magnitude1, magnitude2, ..., magnitude n],
	[date2, magnitude1, magnitude2, ..., magnitude n], ...]
	"""
	date_magnitudes: dict = {}
	lines: list = []

	with open("../earthquakes.txt", "r") as input_file:
		lines = input_file.readlines()

	for line in lines:
		split_line: list = line.split("\t")
		date = split_line[11].split("T")[0]
		if date not in date_magnitudes:
			date_magnitudes[date] = [date]

		date_magnitudes[date].append(split_line[0])

	return date_magnitudes.values()


def ex_5_12():
	"""
	5.12 Start up a Python session and use urllib to read the source for your favorite web page. There was a late
	change to the Python3.0 specification for urllib. The urllib module was broken into three new modules. You need
	to import urllib.request instead of just urllib. Also, the read(), readline(), and readlines() methods return
	byte arrays instead of strings.
	"""
	url_response = get_web_response("https://thedevneedscoffee.com")
	return url_response.content.decode("utf-8")


def ex_5_13_savePage(url: str, filename: str):
	"""
	5.13 Write a function called savePage that takes a string representing a URL, and a file name as a parameter and
	then saves the contents of the web page to the file.
	"""
	url_response = get_web_response(url)
	with open(filename, "wb+") as output_file:
		output_file.write(url_response.content)


def get_web_response(url: [str]):
	my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
	response = requests.get(url, headers=my_headers)
	return response


def ex_5_16():
	"""
	5.16 Write a function that opens a web page and returns a dictionary of all the links and their text on that page.
	A link is defined by an HTML tag that looks like <a href="http://my.computer.com/some/file.html">link text</a>
	The link is everything in quotes after the href=, and the text is everything between the > and the </a>.
	"""
	page_text = ex_5_12()
	parser = LinkGrabber()
	parser.feed(page_text)
	for key, value in parser.links.items():
		print(key, ": ", value)


class LinkGrabber(HTMLParser):
	links = {}
	current_link = ""

	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for thing in attrs:
				if thing[0] == 'href':
					self.current_link = thing[1]

	def handle_endtag(self, tag):
		if self.current_link:
			if self.current_link not in self.links.keys():
				self.links[self.current_link] = ""

	def handle_data(self, data):
		if self.current_link:
			if self.current_link not in self.links.keys():
				self.links[self.current_link] = data
				self.current_link = ""

	def handle_startendtag(self, tag, attrs):
		if tag == "a":
			if self.current_link:
				if self.current_link not in self.links.keys():
					self.links[self.current_link] = ""
			for thing in attrs:
				if thing[0] == 'href' and thing[1] not in self.links.keys():
					self.links[thing[1]] = ""


def ex_5_25():
	"""
	5.25 Write a function that will determine the correlation between two stocks for a given date range
	* The url http://ichart.yahoo.com used in the book is broken. I will appreciate if you can find a url that works
	"""
	# Couldnt find data. I found some free api's, but there wasn't enough time to learn them.
	stock1 = get_closing_prices("symbl1")
	stock2 = get_closing_prices("symbl2")
	return correlation(stock1, stock2)


def correlation(xlist, ylist):
	xbar: float = statistics.mean(xlist)
	ybar: float = statistics.mean(ylist)
	xstd: float = statistics.stdev(xlist)
	ystd: float = statistics.stdev(ylist)
	num: float = 0.0

	for i in range(len(xlist)):
		num = num + (xlist[i] - xbar) * (ylist[i] - ybar)
	corr = num / ((len(xlist) - 1) * xstd * ystd)

	return corr


def get_closing_prices(symbol: str):
	return [random.randint(0, 200) for i in range(30)]


def main():
	pass


if __name__ == '__main__':
	main()
