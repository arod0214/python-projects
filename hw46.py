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
