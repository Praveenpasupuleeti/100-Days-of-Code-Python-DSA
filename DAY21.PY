# ----------------------------------------------
# 📅 Day 21 – Python Problem Solving (Medium Level)
# ----------------------------------------------

# 🔷 Question 1: Check if Two Strings Are Anagrams
# Two strings are anagrams if they contain the same characters in any order.

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# Test
print("Q1 - Are 'listen' and 'silent' anagrams?:", is_anagram("listen", "silent"))


# 🔷 Question 2: Find the Second Largest Number in a List

def second_largest(numbers):
    unique_nums = list(set(numbers))
    if len(unique_nums) < 2:
        return "No second largest number"
    unique_nums.sort()
    return unique_nums[-2]

# Test
print("Q2 - Second largest number:", second_largest([12, 45, 1, 45, 78, 34]))


# 🔷 Question 3: Count the Number of Words in a Sentence

def count_words(sentence):
    return len(sentence.strip().split())

# Test
print("Q3 - Word count:", count_words("Python is a great programming language"))
