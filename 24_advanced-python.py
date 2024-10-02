# Walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
    # Output: List is too long (5 elements, expected <= 3)


# Type definitions in Python
age: int = 25 # Variable type hint

# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"
print(greeting("Astitv")) # Usage


from typing import List, Tuple, Dict, Union
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types
identifier: Union[str, int] = "ID123" # identifier = 12345; Also valid

print(type(identifier), identifier)


# Dictionary merge and update operators.
# New operators | and |= allow for merging and updating dictionaries.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}
