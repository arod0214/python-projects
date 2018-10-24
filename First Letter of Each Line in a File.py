fileref = input("Enter a file name:")
file = open(fileref, 'r')
print("The first letters fo the lines in your file are:")
for line in file:
    print(line[0])
