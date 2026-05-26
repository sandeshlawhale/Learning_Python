#! python 3
# pw.py - a secure password locker program (very secure!)

PASSWORDS = {
    "email": "adsfj;ladfsinvue*dsalfk)()",
    "blog": "uoeqrwiy75243,kadfs';",
    "luggage": "1234"
}

import sys, pyperclip

if len(sys.argv) < 2:
    print("usage: python 6.4 pw.py [accoung] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("password for " + account + " copied to your clipboard")
else:
    print("password for " + account + " are not stored in locker")
