# Write a program that asks the user to enter a number between 0 and 1000, inclusive (that is, including the end points 0 and 1000). If they enter a number out of range, print a message that the number is out of range and prompt them again for a number between 0 and 1000, inclusive. When the user enters a number in range, print the number to the screen and end the program.

# You do not have to use main() or a function for this program.


num = int(input("Enter a number between 0 and 1000:"))
while num < 0 or num > 1000:
    print("Your number is out of range!")
    num = int(input("Enter a number between 0 and 1000:"))

print("Your number is",str(num)+".")

