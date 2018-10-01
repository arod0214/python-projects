names = input("Enter a list of names:")
print("You entered:")
namesList = names.split(";")
n = len(namesList)
for i in range(n):
    name = namesList[i].split(",")
    first = name[1].strip()
    last = name[0].strip()
    print(first,last)
