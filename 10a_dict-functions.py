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
