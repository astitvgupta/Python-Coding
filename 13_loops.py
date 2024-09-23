for i in range(5):
    print(i)

for i in range(1,9):
    if (i == 2): # if i is 2, the iteration is skipped
        continue
    elif (i == 7):
        break # # this will print number till 6
    print(i)

for i in range(0, 20, 4):
    print(i)


elements = (74, 35, "Zebra", 345.06, "Astitv", 52, 69)
for i in elements:
    print(i)

# str = "Astitv"
for i in "Astitv":
    print(i)


l= [1,7,8]
for item in l:
    print(item)
else:
    print("done") # this is printed when the loop exhausts!

for item in l:
    pass # without pass, the program will throw an error