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
