def getNumTrips(balance):
    trip = 2.75
    numOfTrips = int(balance // trip)
    return numOfTrips

def main():
    balance = float(input("Enter your Metrocard balance:"))
    print("You can take", getNumTrips(balance), "more trips on the subway.")

if __name__ == "__main__":
    main()
