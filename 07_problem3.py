# Write a program to fill in a letter template given below with name and date
name = input("Enter your name: ")
date = input("Enter the date: ")
# Use of 'f' string
print(f'''Dear {name},
You are selected!
{date}''')


# Write a program to detect double space in a string
string = "a b c d e f  g h i j k l m  n o p  q r s t u v  w x y z "
print(string)
print(string.find("  "))
print(string.replace("  ", " "))