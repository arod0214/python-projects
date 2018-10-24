# Write a program that asks the user for their first and last name, and prints out the number of characters in their name.

# Your code should have a function called getNumCharacters(firstName,lastName) that takes the two names as parameters and returns the total number of characters in them (assume there are no spaces).


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



