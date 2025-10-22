# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

# Hints:
# Use list comprehension to make an array.

# Solution:

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)


# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.

# Solution:

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)


# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

# Hints:
# Use list's remove method to delete a value.

# Solution:

li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)

# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

# Hints:
# Use set() and "&=" to do set intersection operation.

# Solution:

set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print(li)


# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

# Hints:
# Use set() to store a number of values without duplicate.

# Solution:

def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))


# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

# Hints:
# Use Subclass(Parentclass) to define a child class.

# Solution:

class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print(aMale.getGender())
print(aFemale.getGender())