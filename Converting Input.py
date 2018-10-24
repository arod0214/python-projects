# Write a program that implements the pseudocode ("informal high-level description of the operating principle of a computer program or other algorithm") below:

# 1.  Ask the user for the size of their apartment in square feet (size)
# 2.  Convert the size to square meters using the formula:  convertedSize = size * 0.092903
# 3.  Print out the converted size.



size = input("What is the size of your apartment in square feet?")
convertedSize = float(size) * 0.092903
print("Your apartment is",convertedSize,"square meters.")
              
