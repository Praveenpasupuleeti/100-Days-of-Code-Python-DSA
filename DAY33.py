# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program to compute the value of f(n) with a given n input by console.

# Example:
# If the following n is given as input to the program:7

# Then, the output of the program should be:13

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints:
# We can define recursive function in Python.


# Solution:

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print(f(n))


# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

# Example:
# If the following n is given as input to the program:7

# Then, the output of the program should be:0,1,1,2,3,5,8,13


# Hints:
# We can define recursive function in Python.
# Use list comprehension to generate a list from an existing list.
# Use string.join() to join a list of strings.

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))



# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

# Example:
# If the following n is given as input to the program:10

# Then, the output of the program should be:0,2,4,6,8,10

# Hints:
# Use yield to produce the next value in generator.

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))


# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

# Example:
# If the following n is given as input to the program:100

# Then, the output of the program should be:0,35,70

# Hints:
# Use yield to produce the next value in generator.

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Solution:

def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print(",".join(values))


# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

# Hints:
# Use "assert expression" to make assertion.

# Solution:

li = [2,4,6,8]
for i in li:
    assert i%2==0