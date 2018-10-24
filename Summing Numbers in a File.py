numFile = input("Enter the file name:")
file = open(numFile,'r')
summ = 0
for line in file:
    li = line.split(",")
    for i in range(len(li)):
        summ = float(summ) + float(li[i])

print("The sum of your numbers is",str(summ)+".")
