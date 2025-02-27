child_ticket = 10
normal_ticket = 20
senior_ticket = 15

ticket = input("Welcome to the theme park! Do you have a valid ticket?: ").upper().strip()
valid_ticket = ticket in ("YES", "Y")
invalid_ticket = ticket in ("NO", "N")

if valid_ticket:
    print("Welcome to the theme park! Enjoy your stay")
elif invalid_ticket:
    buy_ticket = input("You will have to buy a ticket to enter. Would you like to buy a ticket?: ").upper().strip()
    if buy_ticket in ("YES", "Y"):
        age = int(input("How old are you? (Used to determine your ticket price): "))
        ticket_category = "Ages 0-5 years are free" if age <= 5 else f"Childrens Tickets (Ages 6-12) are ${child_ticket}" if age <= 12 else f"Normal Tickets (Ages 13-59) are ${normal_ticket}" if age <= 60 else f"Senior Tickets (60+) are ${senior_ticket}"
        print(f"{ticket_category}. Enjoy your stay!")
    elif buy_ticket in ("NO", "N"):
        print("Okay, we hope to see you again soon! Have a nice day!")
    else:
        print("Your input was not a valid number, please try again...")
else:
    print("I did not understand, please try again...")

