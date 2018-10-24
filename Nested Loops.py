# Write a program that asks the user for a positive number. Print out from 1 to that number on a single line, that number of times. You can assume the user always enters a valid number.

# You do not have to use main() or a function for this program.

num = int(input("Enter a positive number:"))
for i in range(1,num+1):
    for j in range(1, num+1):
        print(j*1,end=" ")
    print()
        
