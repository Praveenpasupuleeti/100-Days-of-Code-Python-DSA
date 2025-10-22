# Print a unicode string "hello world".

# Hints:

# Use u'strings' format to define unicode string.

# Solution:

unicodeString = "hello world!"
print(unicodeString)


# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

# Hints:

# Use unicode() function to convert.

# Solution:

b = b"hello"           
u = b.decode("utf-8")  
print(u)               



# Write a special comment to indicate a Python source code file is in unicode.

# Hints:

# Solution:


# -*- coding: utf-8 -*-

#----------------------------------------#



# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

# Example:
# If the following n is given as input to the program: 5

# Then, the output of the program should be: 3.55

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints:
# Use float() to convert an integer to a float

# Solution:

n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)



# Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=1

# with a given n input by console (n>0).

# Example:
# If the following n is given as input to the program:

# 5

# Then, the output of the program should be:

# 500

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints:
# We can define recursive function in Python.

# Solution:

def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print(f(n))
