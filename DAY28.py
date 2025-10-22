
# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 

# Hints:

# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use tuple() to get a tuple from a list.

# Solution

def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(tuple(li))
		
printTuple()



# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 

# Hints:

# Use [n1:n2] notation to get a slice from a tuple.

# Solution

tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)



# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

# Hints:

# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.

# Solution

tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
	if tp[i]%2==0:
		li.append(tp[i])

tp2=tuple(li)
print(tp2)


# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

# Hints:

# Use if statement to judge condition.

# Solution

s = input()   
if s.lower() == "yes":
    print("Yes")
else:
    print("No")


# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

# Hints:

# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.

# Solution

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(evenNumbers)

