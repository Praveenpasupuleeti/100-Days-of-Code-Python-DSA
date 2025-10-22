# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) 
# and the values are square of keys. The function should just print the keys only.

# Hints:

# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

# Solution
def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for k in d.keys():	
		print(k)

printDict()

# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# Hints:

# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.

# Solution
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li)

printList()

# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print the first 5 elements in the list.

# Hints:

# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

# Solution
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[:5])

printList()

# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print the last 5 elements in the list.

# Hints:

# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

# Solution

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[-5:])

printList()