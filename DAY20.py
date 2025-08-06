# ----------------------------------------------
# 📅 Day 20 – Python Problem Solving (Medium Level)
# ----------------------------------------------

# 🔷 Question 1: Count the Frequency of Each Character in a String

def character_frequency():
    s = input("Enter a string: ")
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    print("Character Frequency:", freq)

# Test
character_frequency()


# 🔷 Question 2: Check if a List is a Palindrome

def check_list_palindrome():
    lst = input("Enter list items (comma-separated): ").split(",")
    print("Is Palindrome:", lst == lst[::-1])

# Test
check_list_palindrome()


# 🔷 Question 3: Print Numbers with Digit Sum Divisible by 5

def digit_sum_divisible_by_5():
    result = []
    for i in range(100, 201):
        digit_sum = sum(int(d) for d in str(i))
        if digit_sum % 5 == 0:
            result.append(str(i))
    print("Numbers with digit sum divisible by 5:")
    print(", ".join(result))

# Test
digit_sum_divisible_by_5()