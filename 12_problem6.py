# Write a program to find the greatest of four numbers entered by the user
nums = []
for i in range(4):
    val = int(input("Enter a number: "))
    nums.append(val)
print(nums)

result = nums[0]
for i in range(3):
    if(result <= nums[i+1]):
        result = nums[i+1]
print(result)


# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”
# Write a program to detect these spams.
spam = ["Make a lot of money" , "buy now", "subscribe this", "click this"]
message = input("Write your comment here: ")

for i in spam:
    if(i in message):
        print("This is a spam comment!")
        exit()
# print("I \u2764  Python")
print("\N{HEAVY BLACK HEART}")
