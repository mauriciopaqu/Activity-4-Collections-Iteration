# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: Mauricio Padilla
# Date: October 5, 2026

# SCENARIO
# You are developing a registration system for a small event
# The organizers have a list of registered attendees and need to check whether someone is permitted to enter.




# TODO 1: Create a while loop thap that continues until all guests are checked in.

    # TODO 2: Ask the user to enter their name

    # TODO 3: Iterate through guest list and check whether their name appears in the registered guests list

    # TODO 4: If registered and they're not already in checked in, add their name to the checked-in list and print a welcome message

    # TODO 5: Otherwise, Display an appropriate message for unregistered guests

    # TODO 6: Print the updated checked-in list

# TODO 7: Print a message telling us that all guests have successfully checked in!

# EXPECTED OUTPUT:
# [ "Alice", "Bob"]
# What is your name:  "Alice"
#    Welcome Alice!
#    Checked In Guests: [ Alice ]
# What is your name:  "Fred"
#    Sorry Fred, your name isn't on the list.
#    Checked In Guests: [ Alice ]
# What is your name:  "Bob"
#    Welcome Bob!
#    Checked In Guests: [ Alice, Bob ]
# All guests have been checked in!


registered_guests = [
    "Alice",
    "Bob"
]

checked_in = []

while len(checked_in) < len(registered_guests):

    name = input("What is your name: ")

    if name in  registered_guests:

        if name not in checked_in:
            checked_in.append(name)
            print("Welcome", name + "!")
        else:
            print(name, "is already checked in.")

    else:
        print("Sorry", name + ", your name isn't on the list.")

    print("Checked In Guests:", checked_in)

print("All guests have been checked in!")

