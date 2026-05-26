# This file explains how to connect and send emails using SMTP in Python.
# Topics covered:
# 1. Connecting to SMTP server
# 2. Sending SMTP hello message
# 3. Logging into SMTP server
# 4. Sending email
# 5. Disconnecting from SMTP server


# SMTP - used for sending emails

import smtplib

# Connect to SMTP server
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS encryption , with tls data become encrepted
smtpObj.starttls()

# Send hello message
smtpObj.ehlo()

# Login to email account
smtpObj.login('your_name@gmail.com', 'your_password')

# Send email
smtpObj.sendmail(
    'sender@gmail.com',
    'reciever@gmail.com',
    'Subject: Test Email\n\nHello, this is a test email.\nFrom the SMTP python script'
)

print('Email sent successfully.')

# Disconnect from SMTP server
smtpObj.quit()