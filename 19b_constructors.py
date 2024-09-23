class Employee:
    lang = "Java"
    salary = "2000$"

    # __init__() method is also known as constructor.
    def __init__(self): #A dunder method which is automatically called whenever an object is created.
        print("I'm creating an object.")

rohan = Employee()
print(rohan.name, rohan.lang, rohan.salary)


class Employee:
    lang = "Java"
    salary = "2000$"

    def __init__(self, name, lang, salary): # It takes 'self' argument and can also take further arguments.
        self.name = name
        self.lang = lang
        self.salary = salary
        print("I'm creating an object.")

gauri = Employee("Gauri Sharma", "Python", "4500$")
gauri.name # Creating an instance(object) attribute.
print(gauri.name, gauri.lang, gauri.salary)
