# Write a program that asks the user how many letters they want to enter. Ask the user to enter that many letters, and display as a string in the reverse order they were entered.

# You do not have to use main() or a function for this program.

# Hint:  think about how you can change the accumulator pattern to add letters in the front of the string instead of the back.


letters = int(input("How many letters will you enter?"))
stringSoFar = ""
for i in range(letters):
    letter = input("Enter a letter:")
    stringSoFar = letter + stringSoFar

print("Your string backwards is",stringSoFar+".")
