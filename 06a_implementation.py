# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa for "Www.HackerRank.com"
def swap_case(s):
    shit = ""
    for i in s:
        if(i.upper() == i):
            # print(i.lower(), end='')
            shit += i.lower()
        elif(i.lower() == i):
            # print(i.upper(), end='')
            shit += i.upper()
        else:
            pass
    return shit

s = input()
result = swap_case(s)
print(result)
# string = str(lst)
# print(type(string), string)


# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
lst = []
def split_and_join(line):
    lst = line.split(" ")
    return ("-".join(lst))
        
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
def count_substring(string, sub_string):
    val = 0
    for i in string:
        if(string.find(sub_string) != -1):
            index = string.find(sub_string)
            string = string[index+1:] # Consider this line most important.
            val += 1
            
    return val

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa for "Www.HackerRank.com"
def swap_case(s):
    shit = ""
    for i in s:
        if(i.upper() == i):
            # print(i.lower(), end='')
            shit += i.lower()
        elif(i.lower() == i):
            # print(i.upper(), end='')
            shit += i.upper()
        else:
            pass
    return shit

s = input()
result = swap_case(s)
print(result)
# string = str(lst)
# print(type(string), string)


# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
lst = []
def split_and_join(line):
    lst = line.split(" ")
    return ("-".join(lst))
        
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
def count_substring(string, sub_string):
    val = 0
    for i in string:
        if(string.find(sub_string) != -1):
            index = string.find(sub_string)
            string = string[index+1:] # Consider this line most important.
            val += 1
            
    return val

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
# Your task is to replace the blank (______) with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust((thickness-1), " ") + c + (c*i).ljust((thickness-1), " "))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center((thickness*2), " ") + (c*thickness).center((thickness*6), " "))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center((thickness*6), " "))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center((thickness*2), " ") + (c*thickness).center((thickness*6), " "))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust((thickness), " ") + c + (c*(thickness-i-1)).ljust((thickness), " ")).rjust((thickness*6), " "))


# 
import textwrap
def wrap(string, max_width):
    lst = textwrap.wrap(string, width=max_width)
    new_str = ""
    for i in lst:
        new_str += i + "\n"
    return new_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
def solve(s):
    lst = s.split(" ")
    new_lst = []
    # new_str = ""

    for i in lst:
        i = i.capitalize()
        new_lst.append(i)
        # new_str += i + " "

    return " ".join(new_lst)
    # return new_str

name = input()
result = solve(name)
print(result)
