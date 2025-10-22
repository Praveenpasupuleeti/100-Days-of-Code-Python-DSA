# Write a function to compute 5/0 and use try/except to catch the exceptions.

# Hints:

# Use try/except to catch exceptions.

# Solution:

def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception as err:
    print("Caught an exception:", err)
finally:
    print("In finally block for cleanup")



# Define a custom exception class which takes a string message as attribute.

# Hints:

# To define a custom exception, we need to define a class inherited from Exception.

# Solution:


class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """
    
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")\



# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# john@google.com

# Then, the output of the program should be:

# john

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints:

# Use \w to match letters.

# Solution:

import re
emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print(r2.group(1))


# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# john@google.com

# Then, the output of the program should be:

# google

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints:

# Use \w to match letters.

# Solution:

import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(2))


# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

# Example:
# If the following words is given as input to the program:

# 2 cats and 3 dogs.

# Then, the output of the program should be:

# ['2', '3']

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints:

# Use re.findall() to find all substring using regex.

# Solution:

import re
s = input()
print(re.findall("\d+",s))