# Program to count frequency of each word in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
freq = {word: words.count(word) for word in set(words)}
print(freq)


# Program to filter prime numbers from a given list.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

li = [2,3,4,5,6,7,8,9,10,11]
primes = [x for x in li if is_prime(x)]
print(primes)


# Define a class Student with name & marks list, and a method to compute average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks)/len(self.marks)

s1 = Student("John", [85, 90, 78])
print(f"{s1.name}'s average marks: {s1.average()}")


# Program to merge two dictionaries.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}
print(merged)


# Program to reverse each word in a string.

text = input("Enter text: ")
reversed_words = " ".join(word[::-1] for word in text.split())
print(reversed_words)