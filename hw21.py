def getFine(speedLimit,actualSpeed):
    fine = 0
    if actualSpeed <= speedLimit:
        fine = 0
    elif 1 <= actualSpeed - speedLimit <= 15:
        fine = 100
    else:
        fine = int(100 + 5*(actualSpeed - speedLimit))
    return fine
        

def main():
    speedLimit = int(input("Enter the speed limit in miles:"))
    actualSpeed = int(input("Enter the actual speed in miles:"))
    fine = getFine(speedLimit,actualSpeed)
    print("The fine is",fine + ".")

if __name__ == "__main__":
    main()
