# Lists nd Tuples can store values of any datatype.

items = ["Guava", "Zebra", 73, 345.06, "Astitv", "Deepak"]
items[0] = "Grapes" # Unlike strings, Lists are mutable.
print(items[0])
print(items[1:5])

l1 = [1, 8, 7, 2, 21, 15]
l2 = [3, 24, 85]
# l1.index(8)
# l1.insert(1, 4) # Inserts 4 at the index(1).
# l1.sort()
# l1.reverse()
l1.remove(15)
l1.extend(l2) # Extend list by appending elements from the iterable.
print(l1)


elements = (74, 35, 15, "Zebra", 345.06, "Astitv", 82, 29, 61)
val = (74, 35, 15, 82, 29, 61)
print(sum(val))
# print(type(elements)) 
# elements[1] = 26 # Like strings, Tuples are immutable.
print(elements[3])

print(elements.count(24))
print(elements.index("Astitv"))
print(len(elements))
print(max(val)) # Only valid for integer valued tuple.
print(elements[1: 7])