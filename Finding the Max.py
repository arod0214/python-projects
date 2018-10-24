maxSoFar = int(input("Enter a number:"))
for i in range(9):
    num = int(input("Enter a number:"))
    if num > maxSoFar:
        maxSoFar = num

print("The largest number entered is",str(maxSoFar)+".")
