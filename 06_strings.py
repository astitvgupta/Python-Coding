# Strings are immutable which means that you can't change them by running functions on them.

name = "astitv"
# name[2] = "m" # Because strings are immutable.

print(len(name));
print(name[4]);
# Start from index 1 all the way to 4 (excluding 4)
print(name[1: 4]);

# print(name[-4:-1]) # Similar as [len(name)-4 : len(name)-1]
print(name[2: 5])
# Similar as name[0:5]
print(name[ :5])
# Similar as name[1:len(name)]
print(name[1: ])
print(name)
val = "abcdefghijklmnopqrstuvwxyz"
print(len(val))
print(val[0: 25: 4])

print(name.startswith("as"))
print(name.capitalize())


# Escape seuence characters in python.
print("\a")
# Output: Beep sound (in some environments)
print("\N{grinning face}")
# Output: 😀 (if supported)
