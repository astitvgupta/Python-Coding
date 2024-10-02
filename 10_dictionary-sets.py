# Dictionary is a collection of keys-value pairs.
d = {} # Empty dictionary.
dict = {"key": "value",
        "name": "astitv",
        "location":"india",
        "id": 101,
        'list': [1,2,3,4,5]} # Cannot contain duplicate keys.
print(len(dict), type(dict))
print(dict["list"], type(dict["list"]))

dict["id"] = 102 # Like lists, Dictionaries are also mutable.
dict.update({"location":"USA", "occupation": "coder"}) # Adds the new key:value pair like occupation.
dict.update("")
print(dict)

# print(dict.items())
# print(dict.keys())
print(dict.get("list")) # Prints None
# print(dict["marks"]) # Returns an Error
dict.clear()
print(dict)


# Set is a collection of non-repetitive elements.
s = set() # Don't use s = {} as it'll create an empty dictionary.
unique = {74, 35, 15, "Zebra", 345.06, "Astitv", 82, 29, 57}
print(unique, type(unique)) # Sets are unordered, unindexed and immutable.
print(len(unique))
print(unique.union({"Apple", 82}))
print(unique.intersection({57, 78, "Zebra"}))
print(set("HackerRank"))
