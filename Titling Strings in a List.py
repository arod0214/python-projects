# Write a function called titleList that takes as a parameter a list of strings and returns a list containing each string capitalized as a title.

# You should also write a main method to test your function by asking the user for a list of strings, converting that input into an actual list, passing it to your function, and print the returned list.

def titleList(strLst):
    li = strLst.title()
    
    return lst

def main():
    strings = input("Enter a list of strings separated by commas:")
    strings = li.split(",")
    newList = titleList(strings)
    print("Your new list is",newList)

if __name__ == "__main__":
    main()
