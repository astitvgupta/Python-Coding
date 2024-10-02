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


# Given an integer n, print the following values for each integer i from 1 to n:
# Decimal, Octal, Hexadecimal(capitalized), Binary equivalents.
num = int(input())
length = len(bin(num)[2: ]) # To remove "0o" prefix count from the length.
# print(bin(num), space)

for i in range(1, num+1):
    d = str(i)
    o = oct(i)
    h = hex(i)
    b = bin(i)
    
    print(d.rjust(length, " "), o[2: ].rjust(length, " "), h[2: ].upper().rjust(length, " "), b[2: ].rjust(length, " "))


# You are given an integer, . Your task is to print an alphabet rangoli of size. (Rangoli is a form of Indian folk art based on creation of patterns). Different sizes of alphabet rangoli are shown below: {size = 3}
    # ----c----
    # --c-b-c--
    # c-b-a-b-c
    # --c-b-c--
    # ----c----
def print_rangoli(size):
    import string
    
    # Prepare the alphabet slice and create the pattern list
    alphabet = string.ascii_lowercase
    pattern = []

    for i in range(size):
        # Select the required letters
        chars = alphabet[size-1:i:-1] + alphabet[i:size]
        # Join them with hyphens
        row = '-'.join(chars)
        # Center the row based on the total width
        pattern.append(row.center(4*size - 3, '-'))

    # Print the pattern: top to middle, then middle to bottom
    print('\n'.join(pattern + pattern[-2::-1]))
# Example usage
n = int(input())
print_rangoli(n)


def minion_game(string):
    kevin = []
    stuart = []
    count = 0
    for i in string:
        if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            for j in range(len(string)-count):
                kevin.append(string[count : count+j+1])
        else:
            for k in range(len(string)-count):
                stuart.append(string[count : count+k+1])
        count += 1

    print(kevin)
    print(stuart)
    if(len(kevin) > len(stuart)):
        print(f"Kevin {len(kevin)}")
    elif(len(kevin) < len(stuart)):
        print(f"Stuart {len(stuart)}")
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)


def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    for i in range(len(string)):
        if(string[i] in vowels):
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    
    if(kevin > stuart):
        print(f"Kevin {kevin}")
    elif(kevin < stuart):
        print(f"Stuart {stuart}")
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)



