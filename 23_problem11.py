# Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class TwoDvector:
    # i = int(input("i: "))
    # j = int(input("j: "))
    def __init__(self, i, j):
        self.i = i
        self.j = j
        print(f"2-D vector: {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    # k = int(input("k: "))

    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
        print(f"3-D vector: {self.i}i + {self.j}j + {self.k}k")

# obj1 = TwoDvector(3, 4)
obj2 = ThreeDvector(2, 7, 5) # Code execution: 19 -> 13 -> 14 -> (5,6,7,8) -> 15 -> 16


# Create a class 'Employee' and add salary and increment properties to it.
# Write a method 'salaryAfterIncrement' method with a @property decorator with a setter which changes the value of increment based on the salary.
class Employee:
    salary = 2000
    increment = 15

    @property
    def salaryAfterIncrement(self):
        return f"The salary after increment: {round(self.salary + self.salary * (self.increment/100))}$"

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, cur_salary):
        self.increment = round((cur_salary/self.salary -1) * 100)

obj = Employee()
print(f"{obj.salaryAfterIncrement} with {obj.increment}% increment.") # Code execution: 37 -> (28,29,30)

obj.salaryAfterIncrement = 2500 # # Code execution: 40 -> (28,29,30) -> (32,33,34) -> 41
print(f"Increment in the salary of 2500$: {obj.increment}%")


# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them.
class Complex:
    def __init__(self, a, b):
        self.r = a
        self.i = b

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        img = self.r * c2.i + self.i * c2.r
        return Complex(real, img)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

    # def __add__(self, c, d):
    #     print(f"c2 = {c} + {d}i")
    #     real = self.a + c
    #     img = self.b + d
    #     print(f"c1 + c2 = {real} + {img}i")
        
c1 = Complex(2, 3)
c2 = Complex(4, 5)
print(f"c1 = {c1} \nc2 = {c2}")
print(f"c1 + c2 = {c1 + c2}") # Similar to c1.__add__(4, 5)
print(f"c1 * c2 = {c1 * c2}") # Similar to c1.__mul__(4, 5)
# c1.__add__(4, 5)


# Override the __len__() method on vector of problem 5 to display the dimension of the vector.
class Vector:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
obj = Vector([1, 2, 3])
print(len(obj))
