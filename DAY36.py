# Please write a program to randomly print a integer number between 7 and 15 inclusive.

# Hints:
# Use random.randrange() to a random integer in a given range.

# Solution:

import random
print(random.randrange(7,16))


# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

# Hints:
# Use zlib.compress() and zlib.decompress() to compress and decompress a string.

# Solution:

import zlib
s = b'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))


# Please write a program to print the running time of execution of "1+1" for 100 times.

# Hints:
# Use timeit() function to measure the running time.

# Solution:

from timeit import Timer
t = Timer("for i in range(100):1+1")
print(t.timeit())


# Please write a program to shuffle and print the list [3,6,7,8].

# Hints:
# Use shuffle() function to shuffle a list.

# Solution:

from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)


# Please write a program to shuffle and print the list [3,6,7,8].

# Hints:
# Use shuffle() function to shuffle a list.

# Solution:

from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)