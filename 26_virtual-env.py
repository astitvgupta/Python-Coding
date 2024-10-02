# Function created using an expression using 'lambda' keyword.
square = lambda x:x*x
print(square(6))

# Join method(string): Creates a string from iterable objects.
name = ["Harry", "Rohan", "Astitv", "Subham", "Deepak"]
print(result:= ", ".join(name))

# Format method(string): Formats the values inside the string into a desired output.
print("{} is a good {}".format("harry", "boy"))
print("{1} is learning {0}".format("Astitv", "Python"))

# Map method Example.
lst1 = [1, 2, 3, 4, 5]
square = lambda x: x*x

sqlist = list(map(square, lst1))
print(sqlist)


# Filter method: Works like if-else condition.
lst2 = [5, 4, 2, 3, 8, 6, 1]
def even(n):
    if(n%2 == 0): 
        return True
    return False

# result = list(filter(even, lst2))
result = filter(even, lst2)
print(type(result), list(result))


# Reduce method: Works like recursion implementation.
from functools import reduce

lst3 = [1, 2, 3, 4, 5, 6]
sum = lambda a, b: a * b

final = reduce(sum, lst3)
print(final)
# Sequence of execution for reduce() method.
# x = 1 + 2
# x1 = x + 3
# x2 = x1 + 4
# x3 = x2 + 5
# x4 = x3 + 6
# print(x4)
