# Write a function called getFare that takes as two parameters: the zone and the ticket type (in that order), and returns the Copenhagen Transit fare.

# If the zone is 2 or smaller and the ticket type is "adult", the fare is 23.
# If the zone is 2 or smaller and the ticket type is "child", the fare is 11.5.
# If the zone is 3 and the ticket type is "adult", the fare is 34.5.
# If the zone is 3 or 4 and the ticket type is "child", the fare is 23.
# If the zone is 4 and the ticket type is "adult", the fare is 46.
# If the zone is greater than 4, return a negative number (since your calculator does not handle inputs that high).


def getFare(zone,ticketType):
    zone = 0
    fare = 0
    if zone <= 2 and ticketType == "adult":
        fare = fare + 23
    elif zone <= 2 and ticketType == "child":
        fare = fare + 11.5
    elif zone == 3 and ticketType == "adult":
        fare = fare + 34.5
    elif zone == 3 and ticketType == "child":
        fare = fare + 23
    elif zone == 4 and ticketType == "adult":
        fare = fare + 46
    elif zone == 4 and ticketType == "child":
        fare = fare + 23
    elif zone > 4:
        print("-1")
    return int(fare)
    
def main():
    zone = input("What is the zone?")
    ticketType = input("What is the ticket type (adult/child)?")
    print("The fare is",getFare(zone,ticketType),"krone.")

if __name__ == "__main__":
    main()
