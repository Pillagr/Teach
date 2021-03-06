
"""
A function is a collection of commands that can be collectively
executed. 

*******
HOW TO BUILD A FUNCTION:

def NAME(ARGS):
	COMMANDS
	return VALUE

start all functions with "def" (define), followed by a NAME, starting with
only letters (or underscore) and containing only letters, numbers, and underscore
Next, parantheses (with no spaces bettween the NAME) contain the ARGS (arguments)
passed to the function. After the closing ")" is a colon and newline with indent.

ARGS are inputs, and act as locally defined variables. They can be infinite, and 
are separated by commas.

COMMANDS any number of commands follow. All must be indented at least once more 
than the function. 

RETURN: some functions return a value using the keyword "return" followed by 
the value to be returned. This has no parantheses. You can return a single value,
multiple (separated by commas), or nothing at all. The return statement immediately
ends the function.
"""
def add(x, y):
	""" 
	this function takes 2 args and returns the sum of them as a single variable. 
	there are no commands except the return statement
	
	Note:
	since strings and lists can be added with the + sign as well, tthis function 
	works for strings, lists, etc. as well as numbers.

	"""
	return x + y

# Example calls:
# print(add(4,5)) #prints 9
# x = add(4,5) # x = 9

def say_hi(name):
	"""
	This function takes 1 argument, and adds it inside the predefined
	message string. Because it is adding the name to other strings, name 
	must be a string. passing an Integer will result in an error. 
	This function has no return. 

	"""
	msg = "Hello" + name + "! Wow are you doing?"
	print(msg)

#EX.
# 1) say_hi("Sachin")
# 2) myName = "Ahsan" # create a string variable 
# 	 say_hi(myName) # pass it to the function
# 3) say_hi(5) # this gives an error: cannot concatenate string with int

"""
WHY FUNCTIONS?
Using functions is critical to for several reasons:

-Readability: coders and testors can understand the flow and logic
of a particular piece of code, without understanding the entire program

-Efficiency: calling a function usually only takes one line of code,
and it executes any amount of code, so you can avoid rewriting code.

-Modularity: debugging (finding errors) is a lot easier when functions
are as specific and modular as possible. 

A function should do exactly 1 logical "thing". to acheive several logical
"things", have a function which calls several functions. 

EX. this set of functions divides each task into a function and uses the run()
function to assemble them all into a "program". since the "get functions"
return values, they can be used to set variables' values in run(). 
"""

def get_age():
	return input("What is your Age? ")

def get_name():
	return input("What is your name? ")

def get_color():
	return input("What is your favorite color? ")

def print_info(name, age, fav_color):
	# for more on the fstrings see Intro/intro.py
	fullstring = f"Name: {name}\nAge: {age}\nColor: {fav_color}"
	print(fullstring)

def run():
	# we use our functions to assign each variable a value (based on user input)
	age = get_age()
	name = get_name()
	color = get_color()
	# Now we pass each variable to the print_info function
	print_info(name, age, color)

"""
Recursive Function:
recursive functions call themselves. To understand them, try copy-pasting 
the entire function each time you see it call itself. 

"""
def recursiveFunc(y):
	"""
	this function will increment a given number then call itself, passing that same number. After
	the called function is done, it will print y. This results in it printing 
	he numbers in reverse order, because the innermost iteration finishes first
	before execution returns to upper iterations. Illustration:

	r = the addition function (y +=1 )
	p = the print part of the funtion (print(y, end=' '))
	y = the var (starting at 0)


	r0 -> r1 -> r2 -> r3 -> p3(4) -> p2(3) -> p(2) -> p0(1)
	y=1	  y=2	y=3	  y=4  
	"""
	y += 1
	print(y, end=' ')
	if y < 9:
		recursiveFunc(y)
	
def fibonacci(limit=15):
	"""
	Non-recursive fibonacci function
	"""
	a = 1
	b = 1
	for _ in range(limit):
		print(b)
		c = a 
		a += b
		b = c 

def recursiveFib(a, b, lim=15):
	"""
	recursive version of a fibonacci function
	"""
	if lim > 0:
		c = a 
		a += b
		b = c
		print(b)
		recursiveFib(a, b, lim=lim-1)

"""
Other functions
"""
def letter_count(sentence):	
	"""
	this function takes any string of english letters and 
	counts the number of occurences for each letter. It 
	starts by making the entire string lowercase. Does not
	count any non-letters, but can easily be changed to do 
	so.

	"""
	# first, make all letters in string lowercase
	sentence = sentence.lower()
	# this is a string of the alphabet.
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	# the list of counts, one for each letter. 
	counts = [0] * 26
	# for each letter in the sentence
	for l in sentence:
		try:
			# find the index of that letter in the alphabet
			idx = alphabet.index(l)
			# add 1 to the corresponding count
			counts[idx] += 1
		# if an error is thrown (because a character is not in the alphabet), 
		# we handle this error (by ignoring it).
		except ValueError: 
			pass
	# finally we return the whole list of counts
	return counts

def print_list(aList):
	"""
	A naive way to print each element in a list
	"""
	# the len() function returns the length of an object, such as
	# a list, string, etc.
	listLen = len(aList)
	for i in range(listLen):
		# using the brackets to index a list, and the variable i as the index.
		print(aList[i], end=' ')

def print_list_2(aList):
	"""
	much easier. 
	"""
	for i in aList:
		print(i)

def print_2d_list(aList):
	for i in aList:
		for j in i:
			# end=' ' overrules the print's default of ending with a newline
			print(j, end=' ') 
		print("") # this prints a newline


"""
Optional or default variables:

a function can pre-define or build in default values for arguments
by setting them equal to a value inside the function definition.
These arguments can be omitted while calling the value, or redefined.

"""

def multiply(x, y=2):
	"""	
	this function multiplies 2 values, but the second value defaults to 2
	if left blank. this means, if we want to, we can only pass in one value,
	and it will simply return that value times 2.
	"""
	return x * y

# EX.
# print(multiply(4,5)) # prints 20
# x = mutliply(4,5) # x = 20
# x = mutliply(5) # x = 10


def sum_of_5(a,b,c=0,d=0,e=0):
	"""
	returns sum of the five args passed in. last 3 default to 0
	
	** because the last 3 default to integers, if you want to add
	strings or a non-number objects, you must specify all values,
	even if empty
	"""
	return a + b + c + d + e
# EX. 
# print(sum_of_5(1,2,3,4,5)) # prints 15
# x = sum_of_5(1,2,3,4) # x = 10
# x = sum_of_5(1,2,3) # x = 6
# x = sum_of_5("a", "b", "c", "d", "e") # x = "abcde"
# x = sum_of_5("a", "b") # ERROR: cant add int and str

def insert_sort(l):
	''' Sort a list in descending order (max first)'''
	result = []
	for i in l:
		idx = 0 # where to place i in result
		for r in result:
			if r > i: # Flip this for ascending order
				idx += 1
		result.insert(idx, i)
	return result

def binary_search(l, val):
	''' 
	Search a sorted list l for value val. 
	return index of value in list
	return -1 if not found
	'''
	start = 0
	end = len(l)
	mid = (start + end) // 2
	while start <= end and mid < len(l):
		if l[mid] > val:
			end = mid-1
		elif l[mid] < val:
			start = mid+1
		else:
			return mid
		# print(mid)
		mid = (start + end) // 2
	return -1

def count_sorting(l):
	result = []
	for i in l:
		count = 0
		for r in result:
			if i > r:
				count += 1
		result.insert(count, i)
	return result

def bubble_sorting(l):
	""" Compares two values at a time and swaps them if in incorrect order"""
	for x in l: # iterates the number of times we need to go through the list
		for j in range(len(l)-1): # goes through the list and puts greatest number last
			if l[j] > l[j+1]:
				temp = l[j]
				l[j] = l[j+1]
				l[j+1] = temp
	return l

def selection_sorting(l):
	""" selects greatest value from list and adds it to result until complete """
	result = []
	length = len(l)
	for x in range(length):
		maximum = 0
		for j in range(len(l)):
			if l[j] > l[maximum]:
				maximum = j
		result.insert(0, l.pop(maximum))
	return result



def rec_bin_search(l, val):
	return recursive_bin_search(0, len(l), l, val)

def recursive_bin_search(start, end, l, val):
	if start <= end:
		mid = (start + end )// 2
		if mid >= len(l) or mid < 0:
			return -1
		if l[mid] > val:
			return recursive_bin_search(start, mid-1, l, val)
		elif l[mid] < val:
			return recursive_bin_search(mid+1, end, l, val)
		else:
			return mid
	else:
		return -1





if __name__ == "__main__":
	li = [1,2,3,4,5,6,7,8,12,14,16,18]
	l2 = [1,2,3,4]
	print(rec_bin_search(li, 1))
	print(rec_bin_search(li, 2))
	print(rec_bin_search(li, 3))
	print(rec_bin_search(li, 4))
	print(rec_bin_search(li, 5))
	print(rec_bin_search(li, 6))
	print(rec_bin_search(li, 7))
	print(rec_bin_search(li, 8))
	print(rec_bin_search(li, 12))
	print(rec_bin_search(li, 14))
	print(rec_bin_search(li, 16))
	print(rec_bin_search(li, 18))
	print(rec_bin_search(li, 22))
	print(rec_bin_search(li, 0))
	print(rec_bin_search(li, 9))
	print(rec_bin_search(li, 13))
	print(rec_bin_search(l2, 1))
	print(rec_bin_search(l2, 2))
	print(rec_bin_search(l2, 3))
	print(rec_bin_search(l2, 4))
	print(rec_bin_search(l2, 5))
	print(rec_bin_search(l2, 0))
	print(rec_bin_search(l2, 1.5))


