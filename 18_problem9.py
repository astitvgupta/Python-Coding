# Write a program to read the text from a given file ‘poetry.txt’ and find out whether it contains the word ‘alive’
with open("18a_poetry.txt") as f:
    # f.read().find("alive")
    if("alive" in f.read()):
        print("I'm still learning Python!")
    else:
        print("I'm done with the Python...")


# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
import random

print("We are playing a Hi-score game...")
score = random.randint(1, 100)
print(f"Your score: {score}")

with open("18b_hi-score.txt", "r") as f:
    hiscore = f.read()
    if(hiscore != ""):
        hiscore = int(hiscore) # Because f.read() returns a string type values.
    else:
        hiscore = 0
    
if(score > hiscore):
    # Write this hiscore to the file.
    with open("18b_hi-score.txt", "w") as f:
        f.write(f"New Hi-score: {str(score)}")


# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13–year old.
def generate_table(n):
    with open(f"Tables/18c_table-{n}.txt", "w") as f:
        for j in range(1, 11):
            table = f"{n} X {j} = {n*j}\n"
            f.write(table)

for i in range(2, 21):
    generate_table(i)


# A file contains some censored words multiple times. You need to write a program which replace this word with ##### by updating the same file.
words = ["fuck", "shit"]

with open("18c_censored.txt", "r") as f:
    text = f.read()

for new in words:
    text = text.replace(new, "*" * len(new))

with open("18c_censored.txt", "w") as f:
    f.write(text)


# Write a program to mine a log file and find out the line number contains word ‘python’.
count = 0
with open("18c_censored.txt", "r") as f:
    while(True):
        line = f.readline()
        count += 1

        if("furious" in line):
            print(f"\"furious\" is present in line number {count}.")
            break
        else:
            pass


# Write a program to make a copy of a text file "18c_censored.txt"
with open("18c_censored.txt", "r") as f:
    content = f.read()
    # print(content)

with open("18d_copy.txt", "w") as f:
    f.write(content)

with open("18d_copy.txt", "w") as f:
    f.write("") # Write a program to wipe out the content of a file using python.

# Write a python program to rename a file to "renamed_by_python.txt".
with open("18c_censored.txt", "r") as f:
    content = f.read()

with open("18d_copy.txt", "w") as f:
    f.write(content)
# To rename a file, Copy the content of actual file to another file "renamed_by_python.txt" and then delete the original file by using (os module) or (sh-util module).
