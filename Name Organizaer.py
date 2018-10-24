# Write a program that prompts the user to enter a list of names. Each person's name is separated from the next by a semi-colon (`;') and the names are entered lastName, firstName. Your program should then print out the names, one per line, with the first names first followed by the last names.

# You do not have to use main() or a function for this program.

names = input("Enter a list of names:")
print("You entered:")
namesList = names.split(";")
n = len(namesList)
for i in range(n):
    name = namesList[i].split(",")
    first = name[1].strip()
    last = name[0].strip()
    print(first,last)
