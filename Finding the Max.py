# Write a program that implements the following pseudocode.  This code asks the user for 10 numbers and prints out the largest number entered. 

# 1. Ask the user for a number and store it as maxSoFar
# 2. Repeat 9 times:
# 3.      Ask the user for a number and store it as num
# 4.      if num > maxSoFar:
# 5.           replace the old value in maxSoFar by num
# 6. print out that the largest number entered is maxSoFar
 

# You do not have to use main() or a function for this program.


maxSoFar = int(input("Enter a number:"))
for i in range(9):
    num = int(input("Enter a number:"))
    if num > maxSoFar:
        maxSoFar = num

print("The largest number entered is",str(maxSoFar)+".")
