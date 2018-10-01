##Write a program that asks the user for the name of an input file and the name of an output file.
##Your program should replace all occurrences of "NY" in the input file text with "New York",
##all occurrences of "NJ" with "New Jersey", andall occurrences of "CT" with "Connecticut"
##and write the results to the output file.

fileref = open("input.txt",'r')

file = open("output.txt",'w')

for line in fileref:
    file.write(line.replace("NY","New York").replace("NJ","New Jersey").replace("CT","Connecticut"))

fileref.close()
file.close()
