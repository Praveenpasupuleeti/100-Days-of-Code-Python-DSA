# ----------------------------------------------
#  Day 16 – Medium Level Python Problem Solving
# ----------------------------------------------

#  Question 1: First Non-Repeating Character in a String

def first_non_repeating_char(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return "None"


print("First non-repeating character:", first_non_repeating_char("praveen"))


# Question 2: Find All Pairs With a Given Sum

def find_pairs(nums, target):
    seen = set()
    output = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            output.add(tuple(sorted((num, diff))))
        seen.add(num)
    return list(output)


print("Pairs with sum 4:", find_pairs([1, 3, 2, 2, 4, 5], 4))


# Question 3: Longest Word in a Sentence

def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        clean = ''.join(char for char in word if char.isalnum())
        if len(clean) > len(longest):
            longest = clean
    return longest

print("Longest word:", longest_word("Python is a powerful programming language"))
