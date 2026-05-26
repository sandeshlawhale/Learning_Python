# Practice Project: Random Chore Assignment Emailer
# This program randomly assigns chores to people
# and sends them emails with their assigned chores.

import random
import smtplib

# Dictionary of people and email addresses
people = {
    'Alice': 'alice@example.com',
    'Bob': 'bob@example.com',
    'Carol': 'carol@example.com',
    'David': 'david@example.com'
}

# List of chores
chores = [
    'Wash Dishes',
    'Clean Bathroom',
    'Vacuum House',
    'Walk the Dog'
]

# Connect to SMTP server
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# Start encryption
smtpObj.starttls()

# Login to email account
smtpObj.login(
    'your_email@gmail.com',
    'your_app_password'
)

# Assign chores randomly
for person, email in people.items():

    # Select random chore
    randomChore = random.choice(chores)

    # Remove assigned chore
    chores.remove(randomChore)

    # Email message
    body = f'''
Subject: Your Assigned Chore

Hello {person},

Your chore for this week is:

{randomChore}

Thank you.
'''

    # Send email
    smtpObj.sendmail(
        'your_email@gmail.com',
        email,
        body
    )

    print(f'Email sent to {person}')

# Disconnect from SMTP server
smtpObj.quit()

print('\nAll chore assignment emails sent successfully.')