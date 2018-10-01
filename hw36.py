toDo = input("Enter a list of things to do (separated by commas):")
li = toDo.split(",")
lis = len(li)
for i in range(lis):
    print(str(i+1)+str("."),li[i])

