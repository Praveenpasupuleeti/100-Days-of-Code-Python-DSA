# Please write a program which accepts basic mathematic expression from console and print the evaluation result.

# Example:
# If the following string is given as input to the program:35+3
# Then, the output of the program should be:38
# Hints:
# Use eval() to evaluate an expression.

# Solution:

expression = input()
print(eval(expression))


# Please write a binary search function which searches an item in a sorted list. The function should return the 
# index of element to be searched in the list.

# Hints:
# Use if/elif to deal with conditions.

# Solution:

import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))



# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

# Hints:
# Use if/elif to deal with conditions.

# Solution:

import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))


# Please generate a random float where the value is between 10 and 100 using Python math module.

# Hints:
# Use random.random() to generate a random float in [0,1].

# Solution:

import random
print(random.random()*100)


# Please generate a random float where the value is between 5 and 95 using Python math module.

# Hints:
# Use random.random() to generate a random float in [0,1].

# Solution:

import random
print(random.random()*100-5)