def getLongest(firstString,secondString):
    first = len(firstString)
    second = len(secondString)
    if first > second:
        print(firstString, "is the longest string.")
    else:
        print(secondString, "is the longest string.")
     

def main():
    firstString = input("Enter a string:")
    secondString = input("Enter a string:")
    getLongest(firstString,secondString)
    

if __name__ == "__main__":
    main()
