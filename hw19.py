letters = int(input("How many letters will you enter?"))
stringSoFar = ""
for i in range(letters):
    letter = input("Enter a letter:")
    stringSoFar = letter + stringSoFar

print("Your string backwards is",stringSoFar+".")
