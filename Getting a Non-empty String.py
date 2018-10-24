# Write a program that asks the user to enter a string. If the user enters an empty string, your program should continue prompting the user for a new string until they enter a non-empty string. Your program should then print out the string entered.

# Hint:  An empty string is represented as "" in Python.

# You do not have to use main() or a function for this program.


string = input("Enter a non-empty string:")
x = range(0,1001)
while string == "":
    print("Your string was empty.")
    string = input("Enter a non-empty string:")

print("You entered the string:",string)
    


