# Write a program that asks the user to enter a Metrocard balance, and prints out how many more subway trips the user can take. Assume each subway trip costs $2.75.

# Your code should include a function called getNumTrips(balance) which takes in one parameter called balance, which holds the balance of the Metrocard. Your function should return the number of subway trips that can be taken with that balance.


def getNumTrips(balance):
    trip = 2.75
    numOfTrips = int(balance // trip)
    return numOfTrips

def main():
    balance = float(input("Enter your Metrocard balance:"))
    print("You can take", getNumTrips(balance), "more trips on the subway.")

if __name__ == "__main__":
    main()
