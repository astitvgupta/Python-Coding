# Write a program using functions to find greatest of three numbers.
def compare():
    a = int(input(f"Enter a: "))
    b = int(input(f"Enter b: "))
    c = int(input(f"Enter c: "))

    if((a>=b) and (a>=c)):
        return a
    elif((b>=a) and (b>=c)):
        return b
    elif((c>=b) and (c>=a)):
        return c

print("Enter any 3 numbers to compare: ")
print(f"{compare()} is the greatest of all.")


# Write a recursive function to calculate the sum of first n natural numbers.
def nsum(num):
    if(num == 1):
        return 1
    else:
        result = 0
        result = num + nsum(num-1)
        return result
    
num = int(input("Enter a number: "))
print(f"The sum of {num} natural numbers will be {nsum(num)}")


# Write a python program using function to convert Celsius to Fahrenheit.
def f_to_c(f):
    c = ((f-32)/9)*5
    return c

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")


# Write a python function to remove a given word from a list ad strip it at the same time.
def removed(l1, word='a'):
    for item in l1:
        if(word in item):
            print(f"Removed: {item}")
            l1.remove(item)
            print(f"Updated list: {l1}")
        
    return l1

l1 = ["Astitv", "Chetan", "a", "Shubham", "Asmit", "Aayush", "Deepak", "Anant"]
print(f"Original list: {l1}")
print(f"Final list: {removed(l1)}")

# # Output -> Removed: Chetan
# #           Removed: Shubham
# #           Removed: Aayush
# #           Removed: Deepak
# #           ['Astitv', 'Rohan', 'Anant', 'Asmit']

# def rem(l, word):
#     newl = []
#     for item in l:
#         if (item != word):
#             newl.append(item.strip(word))
#     return newl
    
# l = ["Harry", "Rohan", "Shubham", "an"]
# print(f"{rem(l, "an")}")
