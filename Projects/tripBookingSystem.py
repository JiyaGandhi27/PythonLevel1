sourceLocations = ["Delhi","Mumbai","Kolkata","Dehradun"]
destinationLocations = ["Delhi","Mumbai","Kolkata","Dehradun"]

mode = ["Bus","Rail","Air"]

print("\n",sourceLocations,"\nWhat is your current location?\nSelect as per the order: ")
departureLocation = sourceLocations[int(input("Select location: "))-1]
print(departureLocation)

for i in destinationLocations:
    if i == departureLocation:
        destinationLocations.remove(i)

print("\n",destinationLocations,"\nWhat is your destination location?\nSelect number as per the order: ")
destination = destinationLocations[int(input("Select destination: "))-1]
print(destination)

print("\n",mode,"\nSelect your mode of transport: ")
modeTransport = mode[int(input("Select your mode of transport: : "))-1]
print("\nYou've selected",modeTransport,"as your means of travel")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
phoneNumber = input("Enter your mobile number: ")
dateOfJourney = input("Enter your dateof Journey in DD/MM/YYYY format: ")
numberOfTickets = int(input("Enter the number of tickets: "))
email = input("Enter your e-mail address for us to share you the tickets: ")

def ticketCreation(destination , numberOfTickets , source , mode):
    total = 0 
    ticketFair = 0

    if source == "Delhi" and destination == "Mumbai":
        ticketFair = 1000
    if source == "Delhi" and destination == "Kolkata":
        ticketFair = 1200
    if source == "Delhi" and destination == "Dehradun":
        ticketFair = 800

    if source == "Mumbai" and destination == "Delhi":
        ticketFair = 1250
    if source == "Mumbai" and destination == "Kolkata":
        ticketFair = 1100
    if source == "Mumbai" and destination == "Dehradun":
        ticketFair = 1800
    
    if source == "Kolkata" and destination == "Delhi":
        ticketFair = 1450
    if source == "Kolkata" and destination == "Mumbai":
        ticketFair = 1150
    if source == "Kolkata" and destination == "Dehradun":
        ticketFair = 1550 

    if source == "Dehradun" and destination == "Delhi":
        ticketFair = 800
    if source == "Dehradun" and destination == "Mumbai":
        ticketFair = 1600
    if source == "Dehradun" and destination == "Kolkata":
        ticketFair = 1800

    ticketPrice = fairing(mode, ticketFair)

    if numberOfTickets > 1:
        for i in range(numberOfTickets-1):
            additionalTicket = int(input("Please enter the age of other passenger: "))
            if additionalTicket < 10:
                total = total + ticketPrice/1.5
            else:
                total += ticketPrice
    total += ticketPrice
    return total

def fairing(mode, price):
    classes = ["Standard", "First", "Middle", "Economy"]

    ticketPrice = 0

    if mode == "Bus":
        fair_class = classes[3]

    elif mode == "Air":
        print("\n",classes,"\nPlease select a class.\nSelect number as per the order: ")
        fair_class = classes[int(input("Select class:"))-1]
        print(fair_class)

    elif mode == "Rail":
        print("\n",classes,"\nPlease select a class.\nSelect number as per the order: ")
        fair_class = classes[int(input("Select class:"))-1]
        print(fair_class)

    if fair_class == "Economy":
        ticketPrice = price
    elif fair_class == "Standard":
        ticketPrice = 1.5*price
    elif fair_class == "Middle":
        ticketPrice = 2*price
    elif fair_class == "First":
        ticketPrice = 3*price
    else:
        print("Invalid Selection")
    return ticketPrice

def ticketChecking(destination, source, numberOfTickets, mode):
    
    if destination == source:
        print("Error! Soure location cannot be same as the destination..")
        return 0, False
    
    else:
        total = ticketCreation(destination, numberOfTickets, source, mode)
        return total, True

total, check = ticketChecking(destination, departureLocation, numberOfTickets, modeTransport)

if check == True:
    print("\nName: ", name,
    "\nNumber Of Tickets: ", numberOfTickets,
    "\nDate Of Journey: ", dateOfJourney,
    "\nAge: ", age,
    "\nYour ticket total: ", total,
    "\nThank you forbooking your ticket. WE will be sending you a confirmation e-mail soon........")