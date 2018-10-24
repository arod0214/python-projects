# Write a program that asks the user for the name of a text file, and then prints to the screen the first character of each line in that file. If the line is blank, print an empty line.

# Hint: First get your program to pass Tests 1 and 2, which do not have blank lines in the file. Then add in the code to handle blank lines for Test 3.

# You do not have to use main() or a function for this program.

fileref = input("Enter a file name:")
file = open(fileref, 'r')
print("The first letters fo the lines in your file are:")
for line in file:
    print(line[0])
