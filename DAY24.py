# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield

# Solution:


def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reversed(100):
    print(i)



# Question
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))

# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

freq = {}   # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort()

for w in words:
    print("%s:%d" % (w,freq[w]))

# Question:
# Write a method which can calculate square value of number

# Hints:
# Using the ** operator

# Solution:

def square(num):
    return num ** 2

print(square(2))
print(square(3))