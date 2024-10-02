class Employee:
    def __init__(self):
        print("Constructor of Employee.")

class Manager(Employee):
    def __init__(self):
        super().__init__() # super() method is used to access the constructor of a super class in the derived class.
        print("Constructor of Manager.")

    a = 32
    @classmethod # @classmethod decorator is used to create a class method.
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

obj = Manager()
obj.a = 54
obj.show()


# @property decorator, @name.setter and @name.getter methods in Python.
class Coder: # Encapsulation: grouping of multiple methods into a single unit (class).
    @property # The method name with ‘@property’ decorator is called getter method.
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

obj = Coder()
# Abstraction: hiding the implementation details from the user.
obj.name = "Astitv Gupta" # Code execution: 33 -> (22,23,24) -> (26,27,28,29) -> 34 -> 35
print(obj.name) 
print(obj.fname, obj.lname)


# Operator overloading in Python.
class Calculate:
    def __init__(self, n):
        self.n = n

    def __add__(self, m): 
        # print(self.n, m.n)
        print(f"sum = {self.n + m.n}")

obj1 = Calculate(5)
# obj2 = Calculate(7) # Operators in Python can be overloaded using dunder methods.
# print(obj1 + obj2) # These methods are called when a given operator(+) is used on the objects.
obj1.__add__(7) # Similar to (obj1 + obj2)

# __str__() is used to set what gets displayed upon calling str(obj)
# __len__() # used to set what gets displayed upon calling .__len__() or len(obj)
