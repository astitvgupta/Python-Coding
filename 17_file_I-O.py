# File opening modes in Python:-
# r –> open for reading.
# w -> open for writing.
# a -> open for appending.
# + -> open for updating.
# rb -> open for read in binary mode.
# rt -> open for read in text mode.

f = open("17a_file.txt", "r") # Mode of opening (Read mode by default)
data = f.read()
print(data)
f.close()

# str = "I'm learning Python programming."
# f2 = open("myfile.txt", "w")
# insert = f2.write(str)
# f2.close()

f3 = open("17a_file.txt")
val = f3.readline()
print(val, type(val))
f3.close()

str2 = "\nI'm learning Python programming."
f4 = open("17a_file.txt", "a")
insert = f4.write(str2)
f4.close()

# 'with' keyword for opening files.
with open("17a_file.txt", "r") as f5:
    print(f5.read()) # It'll automatically close the file after the complete execution of the code, written inside the indentation.