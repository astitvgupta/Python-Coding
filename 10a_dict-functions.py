# A dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# 0 <= marks[i] <= 100
# Length of marks array = 3
# Input Format: The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained by a student, each value separated by a space.

n = int(input())
students = {}
# marks = [] # External declaration of marks[] list will cause in anonymous results.

for i in range(0, n):
    # name = input(f"Enter name: ")
    # marks = []
    # for val in range(0, 3):
    #     x = int(input())
    #     marks.append(x)
    name, *score = input().split() # This line reads a student’s name followed by their scores, as input by the user.
    marks = list(map(float, score)) # This line converts the list of strings in {score} into a list of floats.
    students.update({name:marks})

query_name = input()
val2 = students.get(query_name)
avg_marks = sum(val2)/3
print("{:.2f}".format(avg_marks)) # It's used to print the value of {avg_marks} formatted to two decimal places.
# print(f"{round(avg_marks, 2)}")

# print(dir(set))
# Output: ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']