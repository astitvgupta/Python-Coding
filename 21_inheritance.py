# Inheritance is a way of creating a new class from an existing class.
from random import randint

class Employee:
    company = "Microsoft"
    name = ""
    age = randint(22, 30)
    def show(self):
        print(f"The Employee name is {self.name} and the age is {self.age}.")

class Programmer(Employee):
    lang = "Python"
    def showLang(self):
        print(f"The Employee {self.name} is good with {self.lang} language.")

class Salary(Programmer):
    company = "Microsoft | Github"
    def showSalary(self, salary):
        print(f"The salary package of {salary}/month is great for the company like {self.company}")

obj = Salary()
obj.name = "Astitv"
obj.show()
obj.showLang()
obj.showSalary(45000)
print(Employee.company)