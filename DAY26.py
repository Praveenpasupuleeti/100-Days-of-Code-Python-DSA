# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

# Hints:

# Use len() function to get the length of a string

# Solution

def printValue(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1>len2:
        print(s1)
    elif len2>len1:
        print(s2)
    else:
        print(s1)
        print(s2)
        
printValue("one","three")


# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

# Hints:

# Use % operator to check if a number is even or odd.

# Solution


def checkValue(n):
    if n%2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
        
checkValue(7)


# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

# Hints:

# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.

# Solution

def printDict():
    d=dict()
    d[1]=1
    d[2]=2**2
    d[3]=3**2
    print(d)
        
printDict()


# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and
# the values are square of keys.

# Hints:

# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.

# Solution

def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print(d)

printDict()


# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) 
# and the values are square of keys. The function should just print the values only.

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
	for (k,v) in d.items():	
		print(v)

printDict()
