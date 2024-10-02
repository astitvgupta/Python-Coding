# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
dict = {"khana": "food",
        "padhna": "Read",
        "likhna": "write",
        "sona": "sleep"}

word = input("Enter the word, you want the meaning of: ")
print(dict.get(word))


# Write a program to input eight numbers from the user and display all the unique numbers(once).
nums = set()
print("Enter any 8 numbers: ")
for i in range(8):
    # s = input()
    nums.add(input())
print(nums)


# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s, len(s)) # In python, 1 == 1.0


# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
lang = {} # Empty dictionary
for i in range(4):
    a = input("Enter your name: ")
    b = input("Enter your language: ")
    lang.update({a:b})
print(lang)


# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
# No, you cannot include a list inside a set in Python because lists are mutable (they can be changed), and sets require all their elements to be hashable and immutable. Elements in a set must be immutable to maintain the unique, unordered nature of sets.
# This will raise a TypeError: unhashable type: 'list' because a list ([1, 2]) is mutable and cannot be hashed, and thus cannot be added to the set.


