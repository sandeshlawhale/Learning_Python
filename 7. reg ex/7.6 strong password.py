# strongPassword.py - check the password  is strong or not

import re

def checkPassword(password):
    passRegex = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z0-9@()_${}]{8,}$')
    mo = passRegex.match(password)
    return mo != None


print("Try if a password is strong enough or not.")
while True:
    print("Enter your password (Enter nothing to stop):")
    passkey = input()

    if passkey == "":
        break

    if checkPassword(passkey):
        print("Your Password is strong")
    else: 
        print("Your password is not strong enough.")