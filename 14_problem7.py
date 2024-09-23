# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l:
    if(i.startswith("S")):
        print(f"Good Afternoon, {i}")


# Write a program to print reverse multiplication table of a given number using while loop.
a = int(input("Enter a number: "))
l1 = []
for i in range(1, 11):
    l1.append(a*i)

l1.reverse()
j = 0
while(j<10):
    print(l1[j])
    j += 1


# Write a program to find whether a given number is prime or not.
num = int(input("Enter a number: "))

for i in range(2, round(num/2) + 1):
    if(num%i == 0):
        print(f"{num} is not a prime number.")
        exit()   
print(f"{num} is a prime number.")


# Write a program to calculate the factorial of a given number using for loop.
num = int(input("Enter a number: "))
result = 1
for i in range(1, num + 1):
    result = result * i
print(f"Factorial of {num} is {result}")


# Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(f" "*(n-i), "*"*(2*i-1))

