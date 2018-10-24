# Write a program that asks the user for the name of a text file, and then prints to the screen each of the lines in the file in upper case letters.

# You do not have to use main() or a function for this program. 

fileref = input("Enter a file name:")
file = open(fileref, 'r')
for line in file:
    cap = line.upper
    print(line,end="")
