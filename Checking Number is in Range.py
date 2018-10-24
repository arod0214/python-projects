num = int(input("Enter a number between 0 and 1000:"))
while num < 0 or num > 1000:
    print("Your number is out of range!")
    num = int(input("Enter a number between 0 and 1000:"))

print("Your number is",str(num)+".")

