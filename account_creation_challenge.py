# Author: tr00ls
# Description: A Python program that simulates a simple login system, that stores created username and password as variables, and gives you 3 tries to log in, with your newly created credentials!
# This was pretty fun and a little hard to make! I made this as a part of a challenge while learning Python :)
# There are built-in are conditions for username and password strength, though it would be possible to ennumerate usernames, from the error messages in the login section.

import string

while True:
    username = input("To register for account, please create a username: ")

    if len(username) > 12:
        print("Username over 12 characters, please try again")
        continue
    if not username.find(" ") == -1:
        print("Username can't contain spaces, please try again")
        continue
    if not username.isalpha():
        print("Username can't contain numbers, please try again")
        continue
    print(f"Welcome {username}")
    break

while True:
    psswd = input("Please create a password: ")
    psswd.find(" ")

    if len(psswd) < 8:
        print("Your password must be atleast 8 characters long, please try again")
        continue
    elif not any(char.isupper() for char in psswd):
        print("Your password must have one uppercase character, please try again")
        continue
    elif not any(char.isdigit() for char in psswd):
        print("Your password must have one digit, please try again")
        continue
    elif not any(char in string.punctuation for char in psswd):
        print("Your password must contain a special character, please try again")
        continue
    print("Password is strong!")
    break

print("Your account has been created, please log in")

login_attempt_counter = 0

while True:
    login_attempt_username = input("Username: ")
    if login_attempt_username != username:
        print("Wrong Username")
        login_attempt_counter += 1 
        if login_attempt_counter == 3:
            print("3 wrong attempts, please start over")
            break
        continue
    elif login_attempt_username == username:
        login_attempt_psswd = input("Password: ")
        if login_attempt_psswd != psswd:
            print("Wrong Password")
            login_attempt_counter += 1
            if login_attempt_counter == 3:
                print("3 wrong attempts, please start over")
                break
            continue
        print(f"Welcome to your account {username}") 
    break



