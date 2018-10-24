def getNumCharacters(firstName,lastName):
    x = len(firstName)
    y = len(lastName)
    return x+y

def main():
    firstName = input("Enter your first name:")
    lastName = input("Enter your last name:")
    print("There are",getNumCharacters(firstName,lastName),"characters in your full name.")

if __name__ == "__main__":
    main()



