# Write a program to store 5 fruits in a list entered by the user.

fruits = []
item1 = input("Enter the fruits name: ")
fruits.append(item1)
item2 = input("Enter the fruits name: ")
fruits.append(item2)
item3 = input("Enter the fruits name: ")
fruits.append(item3)
item4 = input("Enter the fruits name: ")
fruits.append(item4)
item5 = input("Enter the fruits name: ")
fruits.append(item5)
print(fruits);


# Write a program to sum a list with 5 numbers and sort it also.
numbers = [3,6,2,9,1]
numbers.sort()
print(numbers)

sum = 0
for i in numbers:
    sum = sum + i
print(sum)