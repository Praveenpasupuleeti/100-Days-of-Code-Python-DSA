# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints
# Use map() to generate a list.
# Use lambda to define anonymous functions.

# Solution

li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print(squaredNumbers)


# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints
# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

# Solution

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(evenNumbers)


# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# Hints:

# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

# Solution

evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)



# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# Hints
# Use map() to generate a list.
# Use lambda to define anonymous functions.

# Solution

squaredNumbers = map(lambda x: x**2, range(1,21))
print(squaredNumbers)


# Define a class named American which has a static method called printNationality.

# Hints:
# Use @staticmethod decorator to define class static method.

# Solution

class American(object):
    @staticmethod
    def printNationality():
        print("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()


# Define a class named American and its subclass NewYorker. 

# Hints:

# Use class Subclass(ParentClass) to define a subclass.

# Solution:

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)