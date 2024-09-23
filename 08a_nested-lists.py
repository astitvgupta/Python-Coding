# Nested list statements.
# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

students = [['Harry', 37], ['Berry', 37], ['Tina', 36], ['Akriti', 45], ['Harsh', 42]]
# print(students[1][1])

stu_list = []
grade = []
num = int(input())

for i in range(0, num):
    name = students[i][0]
    score = int(students[i][1])
    stu_list.append([name, score]) # Stores students data in stu_list[] list.
    grade.append(score)

print(stu_list)
grade.sort()
print(f"Sorted grade-list: {grade}")

for i in range(0, num):
    if(grade[i] < grade[i+1]):
        x = grade[i+1]
        break
    else:
        pass

print(f"2nd lowest = {x}")
weak_stud = []

for item in stu_list:
    if(x == item[1]):
        weak_stud.append(item[0]) # It'll sort the students name alphabetically.
    else:
        pass

weak_stud.sort()
for i in weak_stud:
    print(i)
