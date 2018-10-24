fileref = input("Enter a file name:")
file = open(fileref, 'r')
for line in file:
    cap = line.upper
    print(line,end="")
