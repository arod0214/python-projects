# Write a program that asks the user for the name of a file. You may assume that every line of the contains floating point numbers separated by commas. Your program should print out the sum of the numbers in the file.

# For example, if your file nums.txt contained:

# -2.5, 2.0
# 8.0
# 100.0, 3.0, 5.1, 3.7
# 6.5

# Then a sample run of your program would look like:

# Enter the file name:nums.txt
# The sum of your numbers is 125.8.
 
# Hint: first sum up a single line, and then extend to an entire file.


numFile = input("Enter the file name:")
file = open(numFile,'r')
summ = 0
for line in file:
    li = line.split(",")
    for i in range(len(li)):
        summ = float(summ) + float(li[i])

print("The sum of your numbers is",str(summ)+".")
