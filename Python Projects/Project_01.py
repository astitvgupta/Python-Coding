import random
# value = ["stone", "paper", "scissor"]
# print(value)
# player1 = print(random.choice(value))
# Computer = print(random.choice(value))

value = {1 : "stone",
         2 : "paper",
         3 : "scissor"}
print(value)
you = value.get(int(input("Enter your choice: ")))
computer = value.get(random.choice([1, 2, 3]))
print(f"You: {you}\nComputer: {computer}")

# Use key:value pairs of Dictionary.
# value = {1 : "stone",
#          2 : "paper",
#          3 : "scissor"}
# print(value.items())
# You = value.get(int(input("You choice: ")))
# Computer = value.get(int(input("Computer choice: ")))

if(you == computer):
    print("It's a draw!")
elif(you == "stone" and computer == "paper"):
    print("Computer wins \N{grinning face}")
elif(you == "stone" and computer == "scissor"):
    print("You wins \N{grinning face}")
elif(you == "paper" and computer == "scissor"):
    print("Computer wins \N{grinning face}")
elif(you == "paper" and computer == "stone"):
    print("You wins \N{grinning face}")
elif(you == "scissor" and computer == "stone"):
    print("Computer wins \N{grinning face}")
elif(you == "scissor" and computer == "paper"):
    print("You wins \N{grinning face}")

