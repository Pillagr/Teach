
def read_data_naive(filename):
	""" 
	this function takes a file such as scores.txt and turns it into
	a list of lists of each person's scores. 
	scores = [ [P1's scores], [P2's scores], ...]
	Python will read all numbers in as strings, so we must individually
	convert each to an integer 
	"""
	with open(filename, "r") as fp:
		#data is now a list strings of each line
		data = fp.readlines()
	# print(data)
	# create an empty list
	scores = []
	# each line is a person's scores
	for s in data: # s is a single string of numbers
		# split each line along the spaces, now list 1 should =
		# ['94', '73', '72', '88', '75', '62', '92', '74', '99']
		string_list = s.split(" ")
		# an empty list, reused each time
		person = []
		for t in string_list: # t is the string '94', then '73'...
			person.append(int(t)) # make t an int
		# add the person's scores list to the scores list
		scores.append(person) 

"""
since s.split(" ") returns a full list, we can use it in the for loop
"""

def read_data_better(filename):
	with open(filename, "r") as fp:
		#data is now a list strings of each line
		data = fp.readlines()
	scores = []
	for s in data: 
		person = []
		for t in s.split(" "): # a for loop with 1 command is lame. 2 lines for 1 command??
			person.append(int(t))
		scores.append(person) 

def read_data_efficient(filename):
	with open(filename, "r") as fp:
		data = fp.readlines()
	scores = []
	for s in data:
		# this line uses an in-line for loop. it just saves space. it does the a
		scores.append([int(t) for t in s.split(" ")])

def read_data_wicked_fast(filename):
	
	with open(filename, "r") as fp:
		data = fp.readlines()
	# DOUBLE IN-LINE FOR LOOP!!!!
	scores = [[int(t) for t in s.split(" ")] for s in data]
	print(scores)


read_data("Files/scores.txt")