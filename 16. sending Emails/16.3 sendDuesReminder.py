# Project: Sending Members Due Reminder Emails
# This program reads member data from an Excel file,
# finds members who have not paid dues,
# and sends personalized reminder emails.

import openpyxl
import smtplib
import os
os.chdir('.\\16. sending Emails')

# Load Excel workbook
workbook = openpyxl.load_workbook('members_dues_records.xlsx')

# Select active sheet
sheet = workbook.active

# Connect to SMTP server
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS encryption
smtpObj.starttls()

# Login to email account
smtpObj.login(
    'your_email@gmail.com',
    'your_password'
)

# Loop through rows in spreadsheet
for row in range(2, sheet.max_row + 1):

    # Get member name
    name = sheet['A' + str(row)].value

    # Get member email
    email = sheet['B' + str(row)].value

    # Get payment status
    paymentStatus = sheet['C' + str(row)].value

    # Send reminder if dues not paid
    if paymentStatus != 'paid':

        print('Sending reminder email to:', email)

        # Email body
        body = f'''
Subject: Membership Due Reminder

Dear {name},

Our records show that your membership dues are unpaid.
Please make the payment as soon as possible.

Thank you.
'''

        # Send email
        smtpObj.sendmail(
            'your_email@gmail.com',
            email,
            body
        )

# Disconnect from SMTP server
smtpObj.quit()

print('Reminder emails sent successfully.')