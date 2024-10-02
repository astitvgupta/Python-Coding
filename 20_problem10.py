# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    print("Employee details...")
    company = "Microsoft"
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        print(f"{name} | {age} | {gender} | {salary}")

astitv = Programmer("Astitv Gupta", 24, "Male", 42000)


# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def ticket(self, From, to):
        print(f"Ticket is booked in train No. {self.trainNo} from {From} to {to}.")

    def getStatus(self):
        print(f"Train No. {self.trainNo} is running on time!")

    def getFair(self, From, to):
        print(f"Ticket fair in train No. {self.trainNo} from {From} to {to} is {randint(200, 3000)}₹")

    @staticmethod
    def greet():
        print(f"Happy journey...\N{grinning face}")

obj = Train(18420)
obj.ticket("Kanpur", "Katra")
obj.getStatus()
obj.getFair("Kanpur", "Katra")
obj.greet()


# Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:

    def __init__(self, num):
        self.num = num
        print(f"Square of {self.num}: {pow(self.num, 2)}")
        print(f"Cube of {self.num}: {pow(self.num, 3)}")
        print(f"Squareroot of {self.num}: {pow(self.num, 1/2)}")

val1 = Calculator(4)


# Create a class with a class attribute a; create an object from it and set 'a' directly using 'object.a = 0'. Does this change the class attribute?
class Demo:
    a = 4

obj = Demo()
print(obj.a) # Prints the class attribute because instance attribute is not present.
obj.a = 0 # Instance attribute is set.
print(obj.a) # Prints the instance attribute because instance attribute is present.
print(Demo.a) # Prints the class attribute.
