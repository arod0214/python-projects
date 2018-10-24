def isExcited(string):
    if string.count("!")== 0:
        return False
    else:
        return True

def main():
    string = input("Enter a string:")
    print("Your string ends with an exclamation mark:",isExcited(string))

if __name__ == "__main__":
    main()
