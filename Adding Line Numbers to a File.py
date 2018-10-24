# Write a program that asks the user for a file containing a (different) program and a name for an output file. Your program should then write the program, with line numbers to the output file. For example, if the input file is:

# def main():
#	for i in range(10):
#		print("I love python")
#	print("Good bye!")
# Then the output file would be:

# 1	 def main():
# 2		for i in range(10):
# 3			print("I love python")
# 4		print("Good bye!")
# Hint: to preserve the spacing, also write a TAB ('\t') after the number on each line.

name = input("Enter a file name to open:")
file = open(name,'r')
output = open("outputfile.txt",'w')
i=0
for line in file:
    i = i +1
    output.write(str(i))
    output.write("\t")
    output.write(line)
    output.write("\n")

file.close()
output.close()
