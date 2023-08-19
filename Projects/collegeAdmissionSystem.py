import random

print("\nSchool admission Form\n")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
dob = input("Please enter your date of birth: ")
email = input("Please enter your email address: ")
contact = int(input("Please enter your contact number: "))
city = ""
sub2 = ""

#choosing stream
def course():
    stream = ["Arts", "Commerce", "Science"]

    print("\n", stream,"\nPlease select a stream.\nSelect number as per the order: ")
    sub = stream[int(input("Select your stream:"))-1]
    print("\nYou've selected", sub, "as your stream.")

    if sub == "Science":
        sci()
    elif sub == "Commerce":
        commerce()
    else:
        arts()
    return sub

# for streams in science
def sci():

    sci = ["Medical" , "Non-Medical"]

    print("\n", sci,"\nPlease select a stream.\nSelect number as per the order: ")
    sub2 = sci[int(input("Select your stream:"))-1]
    print("\nYou've selected", sub2, "as your course.")

    if sub2 == "Medical":
        medical()
    else:
        nonMedical()
    return sub2

#for subjects in medical
def medical():

    print("\n")
    physics = int(input("Enter your grades in physics: "))
    chemistry = int(input("Enter your grades in chemistry: "))
    biology = int(input("Enter your grades in biology: "))
    english = int(input("Enter your grades in english: "))

    percentage = (physics + chemistry + biology + english)/400*100

    print("Your percentage is",percentage)

    sub2 = med()

    return percentage,sub2

#for subjects in commerce
def commerce():

    print("\n")
    accountancy = int(input("Enter your grades in accountancy: "))
    business = int(input("Enter your grades in business: "))
    economics = int(input("Enter your grades in economics: "))
    history = int(input("Enter your grades in history: "))

    percentage = (accountancy + business + economics + history)/400*100

    print("Your percentage is",percentage)

    sub2 = com()

    return percentage,sub2

#for subjects in arts
def arts():

    print("\n")
    sociology = int(input("Enter your grades in sociology: "))
    psychology = int(input("Enter your grades in psychology: "))
    economics = int(input("Enter your grades in economics: "))
    history = int(input("Enter your grades in history: "))

    percentage = (sociology + psychology + economics + history)/400*100

    print("Your percentage is",percentage)

    sub2 = artsCourse()

    return percentage,sub2

#for subjects in non-medical
def nonMedical():

    print("\n")
    physics = int(input("Enter your grades in physics: "))
    chemistry = int(input("Enter your grades in chemistry: "))
    maths = int(input("Enter your grades in maths: "))
    english = int(input("Enter your grades in english: "))

    percentage = (physics + chemistry + maths + english)/400*100

    print("Your percentage is",percentage)

    sub2 = nonMed()
    return percentage,sub2

#for courses in commerce

def com():
    
    com = ["B.COM" , "BBA" , "LLB" , "CA" , "CS" , "CMA"]

    print("\n", com,"\nPlease select a course.\nSelect number as per the order: ")
    sub2 = com[int(input("Select your course:"))-1]
    print("\nYou've selected", sub2, "as your course.")

    return sub2

#for courses in medical

def med():
    
    med = ["MBBS" , "BDS" , "BAMS" , "BSMS" , "BHMS"]

    print("\n", med,"\nPlease select a course.\nSelect number as per the order: ")
    sub3 = med[int(input("Select your course:"))-1]
    print("\nYou've selected", sub3, "as your course.")

    location()

    return sub3

#for courses in non-medical

def nonMed():
    
    nonMed = ["BTech" , "BSc" , "BBA" , "BS" , "BCA"]

    print("\n", nonMed,"\nPlease select a course.\nSelect number as per the order: ")
    sub3 = nonMed[int(input("Select your course:"))-1]
    print("\nYou've selected", sub3, "as your course.")

    location()

    return sub3

#for courses in arts

def artsCourse():
    
    art = ["BA" , "BMS" , "BBS" , "BBA" , "BFA"]

    print("\n", art,"\nPlease select a stream.\nSelect number as per the order: ")
    sub2 = art[int(input("Select your stream:"))-1]
    print("\nYou've selected", sub2, "as your course.")

    return sub2

#for choosing location
def location():
    
    cities = ["Delhi" , "Kolkata" , "Mumbai" , "Bengalore"]

    print("\n", cities,"\nPlease select a location.\nWe have these locations available for your course.\nSelect number as per the order: ")
    city = cities[int(input("Select your preferred city:"))-1]
    print("\nYou've selected", city, "as your preferred city.")

    return city    

#for generating Roll no.
max_length = 6

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

combinedList = numbers

randomNumbers = random.choice(numbers)

password = randomNumbers

for i in range(max_length-1):
    password = password + random.choice(combinedList)


def streamChecking(age):

    if age < 17:
        print("There are no seats available for you because you're young to get admission in a college.")
        return 0, False

    else:
        sub = course()
        city = location()

        return sub,city, True
    

sub,city, check = streamChecking(age)

if check == True:
    print("\nName:", name,
          "\nAge:", age,
          "\nDate of Birth:", dob,
          "\nEmail:", email,
          "\nContact:", contact,
          "\nStream:", sub,
          "\nLocation:", city,          
          "\nYour Roll Number is: ", password)
    print("Thank you! for filling this form. We will send you an email for details about the college. You will recieve a confirmation call about your admission.")