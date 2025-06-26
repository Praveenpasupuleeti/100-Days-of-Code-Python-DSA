# ------------------------------------------
# Day 4 - Problem 1: Count Vowels in a String
# ------------------------------------------

text = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)


# ------------------------------------------
# Day 4 - Problem 2: Check Palindrome String
# ------------------------------------------

text = input("Enter a string to check palindrome: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# ------------------------------------------
# Day 4 - Problem 3: Remove Spaces from a String
# ------------------------------------------

text = input("Enter a string with spaces: ")
no_space = text.replace(" ", "")
print("String without spaces:", no_space)
