# Write a program that computes the fine for a speeding ticket. Your program should ask the user to enter the speed limit and the speed the vehicle was going. The program should then call a function call getFine(speedLimit,actualSpeed) that takes the two speeds as parameters and returns the fine amount as an integer in dollars. This should then be printed to the screen.

# The fine is calculated as follows:

# if actualSpeed is equal to or less than speedLimit, there is no fine and the function should return 0

# if the vehicle is traveling 1-15 miles over the speed limit, the fine is $100

# if the vehicle is traveling 16 or more miles over the speed limit, the fine is $100 + $5*(actualSpeed - speedLimit)


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
