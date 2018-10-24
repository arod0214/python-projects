# Write a program that asks the user to enter a list of things to do, with the tasks separated by commas (",").

# Your program should then print out the tasks in a numbered list.

# You do not have to use main() or a function for this program. 

toDo = input("Enter a list of things to do (separated by commas):")
li = toDo.split(",")
lis = len(li)
for i in range(lis):
    print(str(i+1)+str("."),li[i])

