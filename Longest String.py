# Write a function called getLongest(...) that takes two strings as parameters (the input) and returns (outputs) the longest string. If the two strings are the same length, return either one.

# You should also write a main method to test your function by asking the user for two strings, calling (using) your function to find the longest, and printing it to the screen.

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
