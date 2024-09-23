# Solving a problem by creating object is one of the most popular approaches in programming. This is called object-oriented programming.
# This concept focuses on using reusable code (DRY Principle).
import random

class Employee:
    print("Employee details: ")

    lang = "Python" # Class attributes.
    age = random.randint(25, 50)
    def getsalary(self): 
        # self refers to the instance of a class. It's automatically passed with a function is called from an object.
        print("Work harder for better increments...")
        amount = random.randint(500, 5000)
        return amount
    
    @staticmethod
    def greet():
        print("Hellow, I'm creating a static method.")

# Creating objects for the Employee class.
astitv = Employee()
astitv.name = "Astitv Gupta" # instance(object) attribute.
print(f"{astitv.name} | {astitv.lang}")
Employee.age = 28
print(f"Age: {astitv.age}\n")

# Note: Instance(object) attributes, take preference over class attributes during assignment & retrieval.
harry = Employee()
harry.name = "Harry bhai"
print(f"{harry.name} | {harry.lang}")
print(f"Salary: {harry.getsalary()}$") # harry.getsalary() evaluated like Employee.getsalary(harry)
harry.greet()