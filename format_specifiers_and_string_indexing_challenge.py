# Author: tr00ls
# Description: This script is a nametag generator for a conference! I made this as a challenge!
# Each attendee provides their full name and ticket number, and the script will generate a formatted name tag.

while True:
    name = input("Enter your full name: ").title()
    if len(name) > 14:
        print("Your name can't be  over 14 characters, please shorten it for the nametag")
        continue
    break
ticket = int(input("Enter your ticket number: "))


name_parts = name.split()
initials = f"({name_parts[0][0]}.{name_parts[1][0]})" if len(name_parts) > 1 else ""
box_width = 25

print("-" * (box_width +2))
print(f"| Name: {name} {initials}".ljust(box_width) + " |")
print(f"| Ticket No: {ticket:05d}".ljust(box_width) + " |")
print("-" * (box_width +2))