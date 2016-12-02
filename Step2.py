from datetime import datetime
today = datetime.today()
time = datetime.now()

print "Today is", today.strftime('%A, %B %d, %Y') + "   " + time.__format__('%I:%M:%S %p')
print "================="
print "1.  Returning Customer"
print "2.  New Customer"
print "3.  Guest"
print "================="
option = 0


def new():
    print "You selected New Customer. \n"


def returning():
    print "You selected Returning Customer. \n"


def guest():
    print "Hello valued customer, thank you for shopping with us today. How may I be of service to you? \n"


def error():
    print ValueError('Please select 1 for Returning Customer, 2 for New Customer, or 3 for Guest')

while option < 1 or option > 3:
    option = (int(raw_input("Choose a customer type, enter 1, 2, or 3: \n")))
    if option == 1:
        returning()
    elif option == 2:
        new()
    elif option == 3:

        guest()
    else:
        error()
