# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# Initialize your list and read in the value of followed by lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
# Constraint: The elements added to the list must be integers.

n = int(input())
list = []

for i in range(0, 12):
    command, *value = input().split(" ")
    # n = list(map(int, value)) # TypeError: 'list' object is not callable.

    match command:
        case "insert":
            list.insert(int(value[0]), int(value[1]))
        case "append":
            list.append(int(value[0]))
        case "remove":
            list.remove(int(value[0]))
        case "sort":
            list.sort()
        case "pop":
            list.pop()
        case "reverse":
            list.reverse()
        case "print":
            print(list)

# Sample Input:
            # 12
            # insert 0 5
            # insert 1 10
            # insert 0 6
            # print
            # remove 6
            # append 9
            # append 1
            # sort
            # print
            # pop
            # reverse
            # print
# Sample Output:
            # [6, 5, 10]
            # [1, 5, 9, 10]
            # [9, 5, 1]