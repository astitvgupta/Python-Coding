def greet(): # Function definition
    name = input("Enter your name: ")

    print(f"Namashkar, {name} ji")
    print("Sher, Cheeta hi kehte hain! \N{grinning face}")

greet() # Function call


# Recursion using functions in Python
def factorial(a):
    if(a==0 or a==1):
        return 1
    else:
        result = a * factorial(a-1)
        return result

num = int(input("Enter the number: "))
print(f"Factorial of {num}: {factorial(num)}")
