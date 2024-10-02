num = int(input("Enter a number: "))

# Exception handling in Python.
try:
    num = int(input("Enter a number: "))
except ValueError as v:
    print(f"ValueError: {v}")
except:
    print("This is a custom error.")

print("Enter a valid number!")


# Raising Exception: We can raise custom exceptions using the 'raise' keyword in python.
a = int(input("a = "))
b = int(input("b = "))

if(b == 0):
    raise ZeroDivisionError("Division by zero is not valid.")
else:
    print(f"The division a/b is {a/b}")


# Try with Else clause: Sometimes we want to run a piece of code when try was successful.
try:
    x = int(input("Enter your age: "))
except ValueError as v:
    print(f"ValueError: {v}")
else:
    print("This is the else block.")

# Try with Finally: It ensures the execution of code regardless of any Except or return statement.

# The Global keyword: is used to modify the variable outside of the current scope.

# The ‘enumerate’ function adds counter to an iterable and returns it.
list1 = ["Harry", "Rohan", "Astitv", "Subham", "Deepak"]
for i,item in enumerate(list1):
    print(f"The value at index {i} is {item}") # Prints the items of list 1 with index

# List Comprehension is an elegant way to create lists based on existing lists.
list1 = [1,7,12,11,22,25]
list2 = [i for i in list1 if i > 8]
print(list2)
